# This file MUST be configured in order for the code to run properly

# Make sure you put all your input images into an 'assets' folder. 
# Each layer (or category) of images must be put in a folder of its own.

# CONFIG is an array of objects where each object represents a layer
# THESE LAYERS MUST BE ORDERED.

# Each layer needs to specify the following
# 1. id: A number representing a particular layer
# 2. name: The name of the layer. Does not necessarily have to be the same as the directory name containing the layer images.
# 3. directory: The folder inside assets that contain traits for the particular layer
# 4. required: If the particular layer is required (True) or optional (False). The first layer must always be set to true.
# 5. rarity_weights: Denotes the rarity distribution of traits. It can take on three types of values.
#       - None: This makes all the traits defined in the layer equally rare (or common)
#       - "random": Assigns rarity weights at random. 
#       - array: An array of numbers where each number represents a weight. 
#                If required is True, this array must be equal to the number of images in the layer directory. The first number is  the weight of the first image (in alphabetical order) and so on...
#                If required is False, this array must be equal to one plus the number of images in the layer directory. The first number is the weight of having no image at all for this layer. The second number is the weight of the first image and so on...

# Be sure to check out the tutorial in the README for more details.                

MALE_CONFIG = [
    {
        'id': 1,
        'name': 'Background',
        'directory': '00_Background',
        'required': True,
        'rarity_weights': None,
    },
    {
        'id': 2,
        'name': 'Shoes',
        'directory': '01_Shoes',
        'required': True,
        'rarity_weights': None,
    },
    {
        'id': 3,
        'name': 'Body',
        'directory': '02_Body',
        'required': True,
        'rarity_weights': None,
    },
    {
        'id': 4,
        'name': 'Clothes',
        'directory': '03_Clothes',
        'required': True,
        'rarity_weights': None,
    },
    {
        'id': 5,
        'name': 'Mouth',
        'directory': '04_Mouth',
        'required': True,
        'rarity_weights': None,
    },
    {
        'id': 6,
        'name': 'Eyes',
        'directory': '05_Eyes',
        'required': True,
        'rarity_weights': None,
    },
    {
        'id': 7,
        'name': 'Hair',
        'directory': '06_Hair',
        'required': True,
        'rarity_weights': None,
    },
    {
        'id': 8,
        'name': 'Face-Decoration',
        'directory': '07_Facedeko',
        'required': False,
        'rarity_weights': None,
    },
    {
        'id': 9,
        'name': 'Chin-Decoration',
        'directory': '08_Chindeko',
        'required': False,
        'rarity_weights': None,
    },
    {
        'id': 10,
        'name': 'Hair-Extensions',
        'directory': '09_HairExtensions',
        'required': False,
        'rarity_weights': None,
    },
    {
        'id': 11,
        'name': 'Hats',
        'directory': '10_Hats',
        'required': False,
        'rarity_weights': None,
    },
    {
        'id': 12,
        'name': 'Head-Decoration',
        'directory': '11_Headdeko',
        'required': False,
        'rarity_weights': None,
    },
    {
        'id': 13,
        'name': 'Left-Hand',
        'directory': '12_Lefthand',
        'required': True,
        'rarity_weights': None,
    },
    {
        'id': 14,
        'name': 'Right-Hand',
        'directory': '13_Righthand',
        'required': True,
        'rarity_weights': None,
    },
]

FEMALE_CONFIG = [
    {
        'id': 1,
        'name': 'Background',
        'directory': '00_Background',
        'required': True,
        'rarity_weights': None,
    },
    {
        'id': 2,
        'name': 'Shoes',
        'directory': '01_Shoes',
        'required': True,
        'rarity_weights': None,
    },
    {
        'id': 3,
        'name': 'Body',
        'directory': '02_Body',
        'required': True,
        'rarity_weights': None,
    },
    {
        'id': 4,
        'name': 'Clothes',
        'directory': '03_Clothes',
        'required': True,
        'rarity_weights': None,
    },
    {
        'id': 5,
        'name': 'Mouth',
        'directory': '04_Mouth',
        'required': True,
        'rarity_weights': None,
    },
    {
        'id': 6,
        'name': 'Eyes',
        'directory': '05_Eyes',
        'required': True,
        'rarity_weights': None,
    },
    {
        'id': 7,
        'name': 'Hair',
        'directory': '06_Hair',
        'required': True,
        'rarity_weights': None,
    },
    {
        'id': 8,
        'name': 'Face-Decoration',
        'directory': '07_Facedeko',
        'required': False,
        'rarity_weights': None,
    },
    {
        'id': 9,
        'name': 'Hair-Extensions',
        'directory': '08_HairExtensions',
        'required': False,
        'rarity_weights': None,
    },
    {
        'id': 10,
        'name': 'Hats',
        'directory': '09_Hats',
        'required': False,
        'rarity_weights': None,
    },
    {
        'id': 11,
        'name': 'Head-Decoration',
        'directory': '10_Headdeko',
        'required': False,
        'rarity_weights': None,
    },
    {
        'id': 12,
        'name': 'Left-Hand',
        'directory': '11_Lefthand',
        'required': True,
        'rarity_weights': None,
    },
    {
        'id': 13,
        'name': 'Right-Hand',
        'directory': '12_Righthand',
        'required': True,
        'rarity_weights': None,
    },
]
