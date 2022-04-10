#!/usr/bin/env python
# coding: utf-8

# Import required libraries
from PIL import Image
import pandas as pd
import numpy as np
import time
import os
import random
from progressbar import progressbar

import warnings

import constants

warnings.simplefilter(action='ignore', category=FutureWarning)

# Import configuration file
from config import MALE_CONFIG, FEMALE_CONFIG

male_assets_path = os.path.join('assets', 'male')
female_assets_path = os.path.join('assets', 'female')


# Parse the configuration file and make sure it's valid
def parse_config(config, gender_folder):
    # Input traits must be placed in the assets folder. Change this value if you want to name it something else.

    # Loop through all layers defined in CONFIG
    for layer in config:

        # Go into assets/ to look for layer folders
        layer_path = os.path.join(os.path.join('assets', gender_folder), layer['directory'])

        # Get trait array in sorted order
        traits = sorted([trait for trait in os.listdir(layer_path) if trait[0] != '.'])

        # If layer is not required, add a None to the start of the traits array
        if not layer['required']:
            traits = [None] + traits

        # Generate final rarity weights
        if layer['rarity_weights'] is None:
            rarities = [1 for x in traits]
        elif layer['rarity_weights'] == 'random':
            rarities = [random.random() for x in traits]
        elif type(layer['rarity_weights'] == 'list'):
            assert len(traits) == len(
                layer['rarity_weights']), "Make sure you have the current number of rarity weights"
            rarities = layer['rarity_weights']
        else:
            raise ValueError("Rarity weights is invalid")

        rarities = get_weighted_rarities(rarities)

        # Re-assign final values to main CONFIG
        layer['rarity_weights'] = rarities
        layer['cum_rarity_weights'] = np.cumsum(rarities)
        layer['traits'] = traits
    return config


# Weight rarities and return a numpy array that sums up to 1
def get_weighted_rarities(arr):
    return np.array(arr) / sum(arr)


# Generate a single image given an array of filepaths representing layers
def generate_single_image(filepaths, assets_path, output_filename=None):
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


# Generate a single image with all possible traits
# generate_single_image(['Background/green.png', 
#                        'Body/brown.png', 
#                        'Expressions/standard.png',
#                        'Head Gear/std_crown.png',
#                        'Shirt/blue_dot.png',
#                        'Misc/pokeball.png',
#                        'Hands/standard.png',
#                        'Wristband/yellow.png'])


# Get total number of distinct possible combinations
def get_total_combinations():
    total = 1
    for layer in MALE_CONFIG:
        total = total * len(layer['traits'])
    return total


# Select an index based on rarity weights
def select_index(cum_rarities, rand):
    cum_rarities = [0] + list(cum_rarities)
    for i in range(len(cum_rarities) - 1):
        if rand >= cum_rarities[i] and rand <= cum_rarities[i + 1]:
            return i

    # Should not reach here if everything works okay
    return None


# Generate a set of traits given rarities
def generate_trait_set_from_config(skin_tone: str, hair_color, config):
    trait_set = []
    trait_paths = []

    for layer in config:
        # Extract list of traits and cumulative rarity weights
        traits, cum_rarities = layer['traits'], layer['cum_rarity_weights']

        # skip layer if it is blocked by the Skeleton-block
        if skin_tone is constants.skeleton_skin and layer.get(constants.skeleton_block):
            continue

        # Generate a random number
        rand_num = random.random()

        # Select an element index based on random number and cumulative rarity weights
        idx = select_index(cum_rarities, rand_num)

        # Adapt the trait according to the skin-tone and the hair-color
        chosen_trait = traits[idx]
        if chosen_trait is not None and chosen_trait.startswith(constants.skin_adapt_pretag):
            chosen_trait = f'{constants.skin_adapt_pretag}_{chosen_trait.split("_")[1]}_{skin_tone}.png'
        elif chosen_trait is not None and chosen_trait.startswith(constants.hair_adapt_pretag):
            chosen_trait = f'{constants.hair_adapt_pretag}_{chosen_trait.split("_")[1]}_{hair_color}.png'

        # Handle isAlive
        if skin_tone is constants.ghost_skin:
            if chosen_trait is not None and chosen_trait.startswith(constants.is_alive_adapt_pretag):
                chosen_trait = f'{constants.is_alive_adapt_pretag}_{chosen_trait.split("_")[1]}_{constants.not_alive_posttag}.png'
        else:
            if chosen_trait is not None and chosen_trait.startswith(constants.is_alive_adapt_pretag):
                chosen_trait = f'{constants.is_alive_adapt_pretag}_{chosen_trait.split("_")[1]}_{constants.alive_posttag}.png'

        # Handle Skelet-sensible adaption
        if chosen_trait is not None and chosen_trait.startswith(constants.is_skeletive_pretag):
            if skin_tone is constants.skeleton_skin:
                chosen_trait = f'{constants.is_skeletive_pretag}_{chosen_trait.split("_")[1]}_{constants.skelet_posttag}.png'
            else:
                chosen_trait = f'{constants.is_skeletive_pretag}_{chosen_trait.split("_")[1]}_{constants.basic_posttag}.png'


        # Add selected trait to trait set
        trait_set.append(chosen_trait)

        # Add trait path to trait paths if the trait has been selected
        if chosen_trait is not None:
            trait_path = os.path.join(layer['directory'], chosen_trait)
            trait_paths.append(trait_path)

    return trait_set, trait_paths


def generate_images2(edition, male_config, female_config, count, drop_dup=True):


    # Define output path to output/edition {edition_num}
    op_path = os.path.join('output', 'edition ' + str(edition), 'images')

    # Will require this to name final images as 000, 001,...
    zfill_count = len(str(count - 1))

    # Create output directory if it doesn't exist
    if not os.path.exists(op_path):
        os.makedirs(op_path)

    # Create the images
    for n in progressbar(range(count)):

        # Generate random constants for the NFT (skin-tone, gender, hair)
        is_female = True if random.randint(0, 1) > 0 else False
        skin_tone = get_random_from_values(constants.skin_tones)
        hair_color = get_random_from_values(constants.hairs)

        config = female_config if is_female else male_config
        assets_path = female_assets_path if is_female else male_assets_path

        # Set image name
        image_name = str(n).zfill(zfill_count) + '.png'

        # Get a random set of valid traits based on rarity weights
        trait_sets, trait_paths = generate_trait_set_from_config(skin_tone, hair_color, config)

        # Generate the actual image
        generate_single_image(trait_paths, assets_path, os.path.join(op_path, image_name))


def get_random_from_values(values):
    rand_int = random.randint(0, len(values) - 1)
    return values[rand_int]


# Generate the image set. Don't change drop_dup
# def generate_images(edition, count, drop_dup=True):
#     # Initialize an empty rarity table
#     rarity_table = {}
#     for layer in MALE_CONFIG:
#         rarity_table[layer['name']] = []
#
#     # Define output path to output/edition {edition_num}
#     op_path = os.path.join('output', 'edition ' + str(edition), 'images')
#
#     # Will require this to name final images as 000, 001,...
#     zfill_count = len(str(count - 1))
#
#     # Create output directory if it doesn't exist
#     if not os.path.exists(op_path):
#         os.makedirs(op_path)
#
#     # Create the images
#     for n in progressbar(range(count)):
#
#         # Set image name
#         image_name = str(n).zfill(zfill_count) + '.png'
#
#         # Choose skin-tone
#         skin_tone = constants.skin_tones[1]
#
#         # Get a random set of valid traits based on rarity weights
#         trait_sets, trait_paths = generate_trait_set_from_config(skin_tone)
#
#         # Generate the actual image
#         generate_single_image(trait_paths, os.path.join(op_path, image_name))
#
#         # Populate the rarity table with metadata of newly created image
#         for idx, trait in enumerate(trait_sets):
#             if trait is not None:
#                 rarity_table[MALE_CONFIG[idx]['name']].append(trait[: -1 * len('.png')])
#             else:
#                 rarity_table[MALE_CONFIG[idx]['name']].append('none')
#
#     # Create the final rarity table by removing duplicate creat
#     rarity_table = pd.DataFrame(rarity_table).drop_duplicates()
#     print("Generated %i images, %i are distinct" % (count, rarity_table.shape[0]))
#
#     if drop_dup:
#         # Get list of duplicate images
#         img_tb_removed = sorted(list(set(range(count)) - set(rarity_table.index)))
#
#         # Remove duplicate images
#         print("Removing %i images..." % (len(img_tb_removed)))
#
#         # op_path = os.path.join('output', 'edition ' + str(edition))
#         for i in img_tb_removed:
#             os.remove(os.path.join(op_path, str(i).zfill(zfill_count) + '.png'))
#
#         # Rename images such that it is sequentialluy numbered
#         for idx, img in enumerate(sorted(os.listdir(op_path))):
#             os.rename(os.path.join(op_path, img), os.path.join(op_path, str(idx).zfill(zfill_count) + '.png'))
#
#     # Modify rarity table to reflect removals
#     rarity_table = rarity_table.reset_index()
#     rarity_table = rarity_table.drop('index', axis=1)
#     return rarity_table


# Main function. Point of entry
def main():
    print("Checking assets...")
    male_config = parse_config(MALE_CONFIG, 'male')
    female_config = parse_config(FEMALE_CONFIG, 'female')

    print("Assets look great! We are good to go!")
    print()

    tot_comb = get_total_combinations()
    print("You can create a total of %i distinct avatars" % (tot_comb))
    print()

    print("How many avatars would you like to create? Enter a number greater than 0: ")
    while True:
        num_avatars = int(input())
        if num_avatars > 0:
            break

    print("What would you like to call this edition?: ")
    edition_name = input()

    print("Starting task...")
    # rt = generate_images2(edition_name, male_config, female_config, num_avatars)
    generate_images2(edition_name, male_config, female_config, num_avatars)

    # print("Saving metadata...")
    # rt.to_csv(os.path.join('output', 'edition ' + str(edition_name), 'metadata.csv'))

    print("Task complete!")


# Run the main function
main()
