import os
import time
import random

import numpy as np
from progressbar import progressbar
from PIL import Image

import constants
from configs.general_configs import multi_hand_configs


def generate_images(edition, male_config, female_config, count, drop_dup=True):
    # Define output path to output/edition {edition_num}
    op_path = os.path.join('output', 'edition ' + str(edition), 'images')

    # Will require thi30s to name final images as 000, 001,...
    zfill_count = len(str(count - 1))

    # Create output directory if it doesn't exist
    if not os.path.exists(op_path):
        os.makedirs(op_path)

    all_trait_sets = list()
    all_trait_paths = list()
    general_traits = list()
    # Create the images
    for n in progressbar(range(count)):
        # Generate random constants for the NFT (skin-tone, gender, hair)
        is_female = True if random.randint(0, 1) > 0 else False
        skin_tone = _get_random_from_values_with_weights(constants.skin_tones, constants.skink_colors_rarities)
        hair_color = _get_random_from_values_with_weights(constants.hairs, constants.hair_colors_rarities)

        config = female_config if is_female else male_config
        assets_path = constants.female_assets_path if is_female else constants.male_assets_path

        # Set image name
        image_name = str(n).zfill(zfill_count) + '.png'

        # Get a random set of valid traits based on rarity weights
        trait_sets, trait_paths = _generate_trait_set_from_config(skin_tone, hair_color, config)
        all_trait_sets.append(trait_sets)
        all_trait_paths.append(trait_paths)
        # collect general traits to pass to the json generator
        general_traits.append({constants.is_female: is_female, constants.skin: skin_tone,
                               constants.hair_color: hair_color})
        # Generate the actual image
        _generate_single_image(trait_paths, assets_path, os.path.join(op_path, image_name))

    return all_trait_sets, all_trait_paths, general_traits


def _get_random_from_values(values):
    rand_int = random.randint(0, len(values) - 1)
    return values[rand_int]


def _get_random_from_values_with_weights(values, weights):
    if len(values) != len(weights):
        raise ValueError("Values and weights must have the same lenght")

    cumulated_weights = np.cumsum(weights)
    rand_int = random.randint(0, sum(weights))

    i = 0
    while cumulated_weights[i] < rand_int:
        i += 1

    return values[i]


# Generate a set of traits given rarities
def _generate_trait_set_from_config(skin_tone: str, hair_color, config):
    trait_set = []
    trait_paths = []

    no_facedeco = False
    naked_shoes = False

    for layer_index, layer in enumerate(config):
        # Extract list of traits and cumulative rarity weights
        traits, cum_rarities = layer['traits'], layer['cum_rarity_weights']

        # Skip layer if no-face deco has before set to True by any layer and current layer is face deco.
        if no_facedeco and layer.get(constants.nofacedeco_block):
            continue

        if skin_tone is constants.skeleton_skin:
            # Skeleton
            if layer.get(constants.skeleton_block):
                continue
        else:
            # Not Skeleton -> but layer is only meant for a skeleton, skip it.
            if layer.get(constants.only_skeleton):
                continue

        # skip layer if it is blocked by the Skeleton-block
        if skin_tone is constants.skeleton_skin and layer.get(constants.skeleton_block):
            continue

        # Generate a random number
        rand_num = random.random()

        # Select an element index based on random number and cumulative rarity weights
        idx = _select_index(cum_rarities, rand_num)

        # Adapt the trait according to the skin-tone and the hair-color
        chosen_trait = traits[idx]
        if chosen_trait is not None and (
                chosen_trait.startswith(constants.skin_adapt_pretag) or chosen_trait.startswith(
            constants.is_skin_naked_shoes)):
            skin_pretag = chosen_trait.split("_")[0]
            chosen_trait = f'{skin_pretag}_{chosen_trait.split("_")[1]}_{skin_tone}.png'

        elif chosen_trait is not None and (
                chosen_trait.startswith(constants.hair_adapt_pretag) or chosen_trait.startswith(
            constants.is_hair_naked_shoes)):
            hair_pretag = chosen_trait.split("_")[0]
            chosen_trait = f'{hair_pretag}_{chosen_trait.split("_")[1]}_{hair_color}.png'

        # Handle Noface deco & IsAlive
        if chosen_trait is not None and (
                chosen_trait.startswith(constants.is_alive_no_facedeco_pretag) or chosen_trait.startswith(
            constants.no_facedeco_pretag)):
            no_facedeco = True

        # Handle NakedShoes config
        if chosen_trait is not None and \
                (
                        chosen_trait.startswith(constants.is_naked_shoes) or
                        chosen_trait.startswith(constants.is_hair_naked_shoes) or
                        chosen_trait.startswith(constants.is_skin_naked_shoes)
                ):
            naked_shoes = True

        if chosen_trait is not None and chosen_trait.startswith(constants.naked_shoes_tag):
            if naked_shoes:
                chosen_trait = f'{chosen_trait.split("_")[0]}_{chosen_trait.split("_")[1]}' \
                               f'_{constants.naked_open}'
            else:
                chosen_trait = f'{chosen_trait.split("_")[0]}_{chosen_trait.split("_")[1]}' \
                               f'_{constants.naked_closed}'

            chosen_trait += f'{skin_tone}.png'

        # Handle isAlive
        if skin_tone is constants.ghost_skin:
            if chosen_trait is not None and chosen_trait.startswith(constants.is_alive_adapt_pretag):
                chosen_trait = f'{chosen_trait.split("_")[0]}_{chosen_trait.split("_")[1]}' \
                               f'_{constants.not_alive_posttag}.png'
        else:
            if chosen_trait is not None and chosen_trait.startswith(constants.is_alive_adapt_pretag):
                chosen_trait = f'{chosen_trait.split("_")[0]}_{chosen_trait.split("_")[1]}' \
                               f'_{constants.alive_posttag}.png'

        # Handle Skelet-sensible adaption
        if chosen_trait is not None and chosen_trait.startswith(constants.is_skeletive_pretag):
            if skin_tone is constants.skeleton_skin:
                chosen_trait = f'{constants.is_skeletive_pretag}_{chosen_trait.split("_")[1]}' \
                               f'_{constants.skelet_posttag}.png'
            else:
                chosen_trait = f'{constants.is_skeletive_pretag}_{chosen_trait.split("_")[1]}' \
                               f'_{constants.basic_posttag}.png'

        # Handle multi-hand logic or append the normal right hand trait.
        if chosen_trait is not None and chosen_trait.startswith(constants.is_multi_hand_pretag):
            trait_set, trait_paths = _append_multi_hand(chosen_trait, trait_set, trait_paths, skin_tone, config,
                                                        layer_index)

        else:
            # Add selected trait to trait set
            trait_set.append(chosen_trait)
            # Add trait path to trait paths if the trait has been selected
            if chosen_trait is not None:
                trait_path = os.path.join(layer['directory'], chosen_trait)
                trait_paths.append(trait_path)

    return trait_set, trait_paths


def _append_multi_hand(chosen_trait, trait_set, trait_paths, skin_tone, config, idx):
    multi_hand_key = chosen_trait.split("_")[2].split('.')[0]
    layers = multi_hand_configs[multi_hand_key]

    previous_layer = config[idx - 1]
    curren_layer = config[idx]
    following_layer = config[idx + 1]

    # Change back layer if necessary (if it should not be 'None')
    if constants.back in layers:
        trait_set.pop()

        trait_name = f'{constants.skin_adapt_pretag}_{multi_hand_key}_{skin_tone}.png'

        trait_set.append(trait_name)
        trait_paths.append(os.path.join(previous_layer['directory'], trait_name))

    # Add chosen layer
    # ignore empty image
    if chosen_trait.split('_')[1].startswith('AAA'):
        trait_set.append(None)
    else:
        trait_set.append(chosen_trait)

    trait_paths.append(os.path.join(curren_layer['directory'], chosen_trait))

    # Add front layer if necessary
    if constants.front in layers:
        trait_name = f'{constants.skin_adapt_pretag}_{multi_hand_key}_{skin_tone}.png'
        trait_set.append(trait_name)
        trait_paths.append(os.path.join(following_layer['directory'], trait_name))
    else:
        trait_set.append(None)

    return trait_set, trait_paths


# Select an index based on rarity weights
def _select_index(cum_rarities, rand):
    cum_rarities = [0] + list(cum_rarities)
    for i in range(len(cum_rarities) - 1):
        if rand >= cum_rarities[i] and rand <= cum_rarities[i + 1]:
            return i

    # Should not reach here if everything works okay
    return None


# Generate a single image given an array of filepaths representing layers
def _generate_single_image(filepaths, assets_path, output_filename=None):
    # Treat the first layer as the background
    bg = Image.open(os.path.join(assets_path, filepaths[0]))

    # Loop through layers 1 to n and stack them on top of another
    for filepath in filepaths[1:]:
        if filepath.endswith('.png'):
            img = Image.open(os.path.join(assets_path, filepath))
            bg.paste(img, (0, 0), img)

    # Save the final image into desired location
    if output_filename is not None:
        bg.save(output_filename)
    else:
        # If output filename is not specified, use timestamp to name the image and save it in output/single_images
        if not os.path.exists(os.path.join('output', 'single_images')):
            os.makedirs(os.path.join('output', 'single_images'))
        bg.save(os.path.join('output', 'single_images', str(int(time.time())) + '.png'))
