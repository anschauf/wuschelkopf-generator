#!/usr/bin/env python
# coding: utf-8

# Import required libraries
import os
import random
import warnings

import numpy as np

import constants
from configs.female_config import FEMALE_CONFIG
from configs.male_config import MALE_CONFIG
import constants
from image_generator import generate_images
from json_generator import create_attribute_json

warnings.simplefilter(action='ignore', category=FutureWarning)

male_assets_path = os.path.join('assets', 'male')
female_assets_path = os.path.join('assets', 'female')


def parse_config(config, gender_folder):
    """
    Parse the configuration file and make sure it's valid
    :param config:
    :param gender_folder:
    :return:
    """
    # Input traits must be placed in the assets folder. Change this value if you want to name it something else.

    # Loop through all layers defined in CONFIG
    for layer in config:

        # Go into assets/ to look for layer folders
        layer_path = os.path.join(os.path.join('assets', gender_folder), layer['directory'])

        # Get trait array in sorted order
        traits = sorted([trait for trait in os.listdir(layer_path) if trait[0] != '.'])

        # Check for parity folder
        check_same_elements(layer, len(traits), gender_folder)

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
                layer['rarity_weights']), f"Incorrect Rarities: {layer['name']} - " \
                                          f"#Trains: {len(traits)}, #Rarities: {len(layer['rarity_weights'])}"
            rarities = layer['rarity_weights']
        else:
            raise ValueError("Rarity weights is invalid")

        rarities = get_weighted_rarities(rarities)

        # Re-assign final values to main CONFIG
        layer['rarity_weights'] = rarities
        layer['cum_rarity_weights'] = np.cumsum(rarities)
        layer['traits'] = traits
    return config


def check_same_elements(layer, number_of_traits, gender_folder):
    parity_prefix = constants.male_path if gender_folder == constants.female_path else constants.female_path

    if layer['parity_path'] is not None:
        parity_path = os.path.join('assets', parity_prefix, layer["parity_path"])

        other_number = len([trait for trait in os.listdir(parity_path) if trait[0] != '.'])

        assert other_number == number_of_traits, \
            f'Parity-Problem: {layer["name"]},' \
            f' in {gender_folder}: {number_of_traits},' \
            f' in {parity_prefix}: {other_number}'

        # Weight rarities and return a numpy array that sums up to 1


def get_weighted_rarities(arr):
    return np.array(arr) / sum(arr)


def get_total_combinations():
    """
    Get total number of distinct possible combinations
    :return:
    """
    total = 1
    for layer in MALE_CONFIG:
        total = total * len(layer['traits'])
    return total


# Main function. Point of entry
def main():
    print("Checking assets...")
    male_config = parse_config(MALE_CONFIG, constants.male_path)
    female_config = parse_config(FEMALE_CONFIG, constants.female_path)

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
    all_trait_sets, all_trait_paths, general_traits = generate_images(edition_name, male_config, female_config, num_avatars)

    print("Creating attribute-json")
    attributes_json = create_attribute_json(all_trait_sets, all_trait_paths, general_traits)
    print("Saving metadata...")
    with open(os.path.join('output', 'edition ' + str(edition_name), 'metadata.json'), 'w') as f:
        f.write(attributes_json)
    print("Task complete!")


# Run the main function
if __name__ == "__main__":
    main()
