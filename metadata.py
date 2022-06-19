#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import time
import os
from progressbar import progressbar
import json
from copy import deepcopy

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


# Base metadata. MUST BE EDITED!!!!!!!!!!!!!!!.
BASE_IPFS_PATH = 'QmeQWkvits2KQKfFPAcL3MqCQJTSpTYCEcRhthzQRJ9T3z'
BASE_IMAGE_URL = f"https://ipfs.io/ipfs/{BASE_IPFS_PATH}"
BASE_NAME = "Wuschelkopf #"

BASE_JSON = {
    "name": BASE_NAME,
    "description": "The Wuschelkopf NFT collection on Ethereum",
    "image": BASE_IMAGE_URL,
    "attributes": [],
}


# Get metadata and JSON files path based on edition
def generate_paths(edition_name):
    edition_path = os.path.join('output', 'edition ' + str(edition_name))
    metadata_path = os.path.join(edition_path, 'metadata.json')
    json_path = os.path.join(edition_path, 'json')

    return edition_path, metadata_path, json_path

# Function to convert snake case to sentence case
def clean_attributes(attr_name):
    
    clean_name = attr_name.replace('_', ' ')
    clean_name = list(clean_name)
    
    for idx, ltr in enumerate(clean_name):
        if (idx == 0) or (idx > 0 and clean_name[idx - 1] == ' '):
            clean_name[idx] = clean_name[idx].upper()
    
    clean_name = ''.join(clean_name)
    return clean_name


# Function to get attribure metadata
def get_attribute_metadata(metadata_path):

    with open(metadata_path, 'r') as f:
        # Read attribute data from metadata file
        attributes = json.load(f)

    # Get zfill count based on number of images generated
    # -1 according to nft.py. Otherwise not working for 100 NFTs, 1000 NTFs, 10000 NFTs and so on
    zfill_count = len(str(len(attributes)))

    return attributes, zfill_count

# Main function that generates the JSON metadata
def main():

    # Get edition name
    print("Enter edition you want to generate metadata for: ")
    while True:
        edition_name = input()
        edition_path, metadata_path, json_path = generate_paths(edition_name)

        if os.path.exists(edition_path):
            print("Edition exists! Generating JSON metadata...")
            break
        else:
            print("Oops! Looks like this edition doesn't exist! Check your output folder to see what editions exist.")
            print("Enter edition you want to generate metadata for: ")
            continue
    
    # Make json folder
    if not os.path.exists(json_path):
        os.makedirs(json_path)
    
    # Get attribute data and zfill count
    all_attributes, zfill_count = get_attribute_metadata(metadata_path)
    
    for idx, ones_attributes in progressbar(enumerate(all_attributes)):
    
        # Get a copy of the base JSON (python dict)
        item_json = deepcopy(BASE_JSON)
        
        # Append number to base name
        item_json['name'] = item_json['name'] + str(idx)

        # Append image PNG file name to base image path
        item_json['image'] = item_json['image'] + '/' + str(idx).zfill(zfill_count) + '.png'
        
        # Add attributes to the item
        item_json['attributes'].extend(ones_attributes)
        
        # Write file to json folder
        item_json_path = os.path.join(json_path, str(idx))
        with open(item_json_path, 'w') as f:
            json.dump(item_json, f)

# Run the main function
main()
