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
from itertools import repeat

FEMALE_CONFIG = [
    {
        'id': 1,
        'name': 'Background',
        'directory': '00_Background',
        'skeleton_block': False,
        'only_skeleton': False,
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
        'only_skeleton': False,
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
        'only_skeleton': False,
        'no_facedeco_block': False,
        'required': True,
        'rarity_weights': None,
        'parity_path': None
    },
    {
        # 125 images
        # 9 elements

        # Classic: 2
        # Converse: 6
        # Barefoot: 8
        # Flipflops: 48
        # HighHeels: 40
        # Joker 5
        # Pirateboot: 5
        # Rubberboot: 6
        # Uggboot: 5

        # Other 4 each 7=> 28
        'id': 4,
        'name': 'Shoes',
        'directory': '03_Shoes',
        'skeleton_block': False,
        'only_skeleton': False,
        'no_facedeco_block': False,
        'required': True,
        'rarity_weights': list(repeat(24, 2)) + list(repeat(8, 6)) + list(repeat(6, 8)) + list(repeat(1, 48)) + list(repeat(1, 40)) + list(repeat(10, 5)) + list(repeat(10, 5)) + list(repeat(8, 6)) + list(repeat(10, 5))
        ,
        'parity_path': None
    },
    {
        'id': 5,
        'name': 'Hair',
        'directory': '04_Hair',
        'skeleton_block': False,
        'only_skeleton': False,
        'no_facedeco_block': False,
        'required': True,
        # Hair rarities are defined under 'constants.py'
        'rarity_weights': None,
        'parity_path': '04_Hair'
    },
    {
        # 44 images
        # 10 objects
        # ===============
        # Lips: 14 => 3 * 14
        # Soother: 14 => 1 * 14
        # Others: 2 each => 8* 7 * 2
        'id': 6,
        'name': 'Mouth',
        'directory': '05_Mouth',
        'skeleton_block': True,
        'only_skeleton': False,
        'no_facedeco_block': False,
        'required': True,
        'rarity_weights': list(repeat(7, 4)) + list(repeat(3, 14)) + list(repeat(7, 6)) + list(repeat(1, 14)) + list(repeat(7, 6)),
        'parity_path': None
    },
    {
        'id': 7,
        'name': 'Skeleton Mouth',
        'directory': '05_2_Skeleton_Mouth',
        'skeleton_block': False,
        'only_skeleton': True,
        'no_facedeco_block': False,
        'required': False,
        'rarity_weights': [100, 2, 2, 2, 2, 2, 2],
        'parity_path': '06_2_Skeleton_Mouth'
    },
    {
        # 92 images
        # 14 elements
        ##################
        # Bow: 2
        # Buttons: 10
        # Cross: 2
        # CrossEyed: 2
        # Dots: 2
        # Hearts: 14
        # Lashed: 14
        # Manga: 8
        # Points: 2
        # Shining: 14
        # Stars: 12
        # Stonde: 2
        # Cyclops: 2
        # Illidan: 8


        'id': 8,
        'name': 'Eyes',
        'directory': '06_Eyes',
        'skeleton_block': True,
        'only_skeleton': False,
        'no_facedeco_block': False,
        'required': True,
        'rarity_weights': list(repeat(14, 2)) + list(repeat(3, 10)) + list(repeat(14, 6)) + list(repeat(2, 28)) + list(repeat(4, 8)) + list(repeat(14, 2)) + list(repeat(2, 14)) + list(repeat(3, 12)) + list(repeat(14, 4)) + list(repeat(3, 8)),
        'parity_path': None
    },
    {
        'id': 9,
        'name': 'Skeleton Eyes',
        'directory': '06_2_Skeleton_Eyes',
        'skeleton_block': False,
        'only_skeleton': True,
        'no_facedeco_block': False,
        'required': False,
        'rarity_weights': [200, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'parity_path': '07_2_Skeleton_Eyes'
    },
    {
        # 16 images
        # 5 elements
        # 50% face deco
        'id': 10,
        'name': 'Face-Decoration',
        'directory': '07_Facedeko',
        'skeleton_block': False,
        'only_skeleton': False,
        'no_facedeco_block': True,
        'required': False,
        'rarity_weights': [70] + list(repeat(4, 4)) + list(repeat(5, 3)) + list(repeat(8, 2)) + list(repeat(3, 6)) + list(repeat(4, 1)),
        'parity_path': None
    },
    {
        'id': 11,
        'name': 'Hair-Extensions',
        'directory': '08_HairExtensions',
        'skeleton_block': False,
        'only_skeleton': False,
        'no_facedeco_block': False,
        'required': False,
        'rarity_weights': [100, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
        'parity_path': None
    },
    {
        # 36 images
        # 8 elements
        # total points: 278
        # 70% nothing, 30% hats => 649
        'id': 12,
        'name': 'Hats',
        'directory': '09_Hats',
        'skeleton_block': False,
        'only_skeleton': False,
        'no_facedeco_block': False,
        'required': False,
        'rarity_weights': [649] + list(repeat(7, 5)) + list(repeat(9, 4)) + list(repeat(9, 4)) + list(repeat(7, 5)) + list(repeat(7, 4)) + list(repeat(9, 4)) + list(repeat(9, 4)) + list(repeat(6, 6)),
        'parity_path': '10_Hats'
    },
    {
        # 65 images
        # 11 elements
        # total points: 710
        # 70 % nothing, 30% deco =>
        'id': 13,
        'name': 'Head-Decoration',
        'directory': '10_Headdeko',
        'skeleton_block': False,
        'only_skeleton': False,
        'no_facedeco_block': False,
        'required': False,
        'rarity_weights': [1657] + list(repeat(13, 5)) + list(repeat(16, 4)) + list(repeat(22, 6)) + list(repeat(11, 6)) + list(repeat(5, 15)) + list(repeat(22, 3)) + list(repeat(16, 4)) + list(repeat(16, 4)) + list(repeat(4, 12)) + list(repeat(11, 6)),
        'parity_path': '11_Headdeko'
    },
    {
        'id': 14,
        'name': 'Left-Hand Back',
        'directory': '11_Lefthand-Back',
        'skeleton_block': False,
        'only_skeleton': False,
        'no_facedeco_block': False,
        'required': False,
        'rarity_weights': [100, 0, 0, 0, 0],  # all values must be set to '0' here
        'parity_path': '12_Lefthand-Back'
    },
    {
        # 56 images
        # 11 elements
        # total points: 625
        # 50% nothing => 625
        ############
        'id': 15,
        'name': 'Left-Hand Thing',
        'directory': '12_Lefthand-Thing',
        'skeleton_block': False,
        'only_skeleton': False,
        'no_facedeco_block': False,
        'required': True,
        'rarity_weights': [625] + list(repeat(11, 5)) + list(repeat(9, 6)) + list(repeat(8, 7)) + list(repeat(9, 6)) + list(repeat(11, 5)) + list(repeat(18, 3)) + list(repeat(11, 5)) + list(repeat(9, 6)) + list(repeat(9, 6)) + list(repeat(18, 3)) + list(repeat(16, 4)),
        'parity_path': '13_Lefthand-Thing'
    },
    {
        'id': 16,
        'name': 'Left-Hand Front',
        'directory': '13_Lefthand-Front',
        'skeleton_block': False,
        'only_skeleton': False,
        'no_facedeco_block': False,
        'required': False,
        'rarity_weights': [100, 0, 0, 0, 0],  # all values must be set to '0' here
        'parity_path': '14_Lefthand-Front'
    },
    {
        'id': 17,
        'name': 'Right-Hand Back',
        'directory': '14_Righthand-Back',
        'skeleton_block': False,
        'only_skeleton': False,
        'no_facedeco_block': False,
        'required': False,
        'rarity_weights': [100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # all values must be set to '0' here
        'parity_path': None
    },
    {
        'id': 18,
        'name': 'Right-Hand Thing',
        'directory': '15_Righthand-Thing',
        'skeleton_block': False,
        'only_skeleton': False,
        'no_facedeco_block': False,
        'required': True,
        'rarity_weights': None,
        'parity_path': '16_Righthand-Thing'
    },
    {
        'id': 19,
        'name': 'Right-Hand Front',
        'directory': '16_Righthand-Front',
        'skeleton_block': False,
        'only_skeleton': False,
        'no_facedeco_block': False,
        'required': False,
        'rarity_weights': [100, 0, 0, 0, 0, 0, 0, 0, 0],  # all values must be set to '0' here
        'parity_path': '17_Righthand-Front'
    }
]
