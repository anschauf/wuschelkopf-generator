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

FEMALE_CONFIG = [
    {
        'id': 1,
        'name': 'Background',
        'directory': '00_Background',
        'skeleton_block': False,
        'no_facedeco_block': False,
        'required': True,
        'rarity_weights': None,
        'parity_path': '00_Background'
    },
    {
        'id': 2,
        'name': 'Body',
        'directory': '01_Body',
        'skeleton_block': False,
        'no_facedeco_block': False,
        'required': True,
        'rarity_weights': None,
        'parity_path': '01_Body'
    },
    {
        'id': 3,
        'name': 'Clothes',
        'directory': '02_Clothes',
        'skeleton_block': False,
        'no_facedeco_block': False,
        'required': True,
        'rarity_weights': None,
        'parity_path': None
    },
    {
        'id': 4,
        'name': 'Shoes',
        'directory': '03_Shoes',
        'skeleton_block': False,
        'no_facedeco_block': False,
        'required': True,
        'rarity_weights': None,
        'parity_path': None
    },
    {
        'id': 5,
        'name': 'Hair',
        'directory': '04_Hair',
        'skeleton_block': False,
        'no_facedeco_block': False,
        'required': True,
        'rarity_weights': None,
        'parity_path': '04_Hair'
    },
    {
        'id': 6,
        'name': 'Mouth',
        'directory': '05_Mouth',
        'skeleton_block': True,
        'no_facedeco_block': False,
        'required': True,
        'rarity_weights': None,
        'parity_path': None
    },
    {
        'id': 7,
        'name': 'Eyes',
        'directory': '06_Eyes',
        'skeleton_block': True,
        'no_facedeco_block': False,
        'required': True,
        'rarity_weights': None,
        'parity_path': None
    },
    {
        'id': 8,
        'name': 'Face-Decoration',
        'directory': '07_Facedeko',
        'skeleton_block': False,
        'no_facedeco_block': True,
        'required': False,
        'rarity_weights': None,
        'parity_path': None
    },
    {
        'id': 9,
        'name': 'Hair-Extensions',
        'directory': '08_HairExtensions',
        'skeleton_block': False,
        'no_facedeco_block': False,
        'required': False,
        'rarity_weights': [100, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
        'parity_path': None
    },
    {
        'id': 10,
        'name': 'Hats',
        'directory': '09_Hats',
        'skeleton_block': False,
        'no_facedeco_block': False,
        'required': False,
        'rarity_weights': None,
        'parity_path': '10_Hats'
    },
    {
        'id': 11,
        'name': 'Head-Decoration',
        'directory': '10_Headdeko',
        'skeleton_block': False,
        'no_facedeco_block': False,
        'required': False,
        'rarity_weights': None,
        'parity_path': '11_Headdeko'
    },
    {
        'id': 12,
        'name': 'Left-Hand Back',
        'directory': '11_Lefthand-Back',
        'skeleton_block': False,
        'no_facedeco_block': False,
        'required': False,
        'rarity_weights': [100, 0, 0, 0, 0],  # all values must be set to '0' here
        'parity_path': '12_Lefthand-Back'
    },
    {
        'id': 13,
        'name': 'Left-Hand Thing',
        'directory': '12_Lefthand-Thing',
        'skeleton_block': False,
        'no_facedeco_block': False,
        'required': True,
        'rarity_weights': None,
        'parity_path': '13_Lefthand-Thing'
    },
    {
        'id': 14,
        'name': 'Left-Hand Front',
        'directory': '13_Lefthand-Front',
        'skeleton_block': False,
        'no_facedeco_block': False,
        'required': False,
        'rarity_weights': [100, 0, 0, 0, 0],  # all values must be set to '0' here
        'parity_path': '14_Lefthand-Front'
    },
    {
        'id': 15,
        'name': 'Right-Hand Back',
        'directory': '14_Righthand-Back',
        'skeleton_block': False,
        'no_facedeco_block': False,
        'required': False,
        'rarity_weights': [100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # all values must be set to '0' here
        'parity_path': None
    },
    {
        'id': 15,
        'name': 'Right-Hand Thing',
        'directory': '15_Righthand-Thing',
        'skeleton_block': False,
        'no_facedeco_block': False,
        'required': True,
        'rarity_weights': None,
        'parity_path': '16_Righthand-Thing'
    },
    {
        'id': 16,
        'name': 'Right-Hand Front',
        'directory': '16_Righthand-Front',
        'skeleton_block': False,
        'no_facedeco_block': False,
        'required': False,
        'rarity_weights': [100, 0, 0, 0, 0, 0, 0, 0, 0],  # all values must be set to '0' here
        'parity_path': '17_Righthand-Front'
    }
]
