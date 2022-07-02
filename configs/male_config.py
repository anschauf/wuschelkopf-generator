from itertools import repeat

MALE_CONFIG = [
    {
        'id': 1,
        'name': 'Background',
        'directory': '00_Background',
        'required': True,
        'skeleton_block': False,
        'only_skeleton': False,
        'no_facedeco_block': False,
        'rarity_weights': None,
        'parity_path': '00_Background'
    },
    {
        # 94 images => 96
        #  13 elements
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
        'rarity_weights': list(repeat(24, 4)) + list(repeat(19, 5)) + list(repeat(3, 30)) + list(repeat(96, 1)) + list(repeat(24, 4)) + list(repeat(19, 5)) + list(repeat(10, 10)) + list(repeat(10, 10)) + list(repeat(24, 4)) + list(repeat(19, 5)) + list(repeat(19, 5)) + list(repeat(24, 4)) + list(repeat(14, 7)),
        'parity_path': None
    },
    {
        # 84 images
        # 8 elements
        'id': 4,
        'name': 'Shoes',
        'directory': '03_Shoes',
        'required': True,
        'skeleton_block': False,
        'only_skeleton': False,
        'no_facedeco_block': False,
        'rarity_weights':  list(repeat(42, 2)) + list(repeat(14, 6)) + list(repeat(11, 8)) + list(repeat(2, 48)) + list(repeat(17, 5)) + list(repeat(21, 4)) + list(repeat(14, 6)) + list(repeat(17, 5)),
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
        # 34 images
        # 3 elements
        # 420 points => 50% = 420
        'id': 6,
        'name': 'Chin-Decoration',
        'directory': '05_Chindeko',
        'skeleton_block': False,
        'only_skeleton': False,
        'no_facedeco_block': False,
        'required': False,
        'rarity_weights': [420] + list(repeat(12, 15)) + list(repeat(12, 15)) + list(repeat(15, 4)),
        'parity_path': None
    },
    {
        # 28 images
        # 9 elements
        'id': 7,
        'name': 'Mouth',
        'directory': '06_Mouth',
        'skeleton_block': True,
        'only_skeleton': False,
        'no_facedeco_block': False,
        'required': True,
        'rarity_weights': list(repeat(14, 10)) + list(repeat(3, 12)) + list(repeat(14, 6)),
        'parity_path': None
    },
    {
        'id': 8,
        'name': 'Skeleton Mouth',
        'directory': '06_2_Skeleton_Mouth',
        'skeleton_block': False,
        'only_skeleton': True,
        'no_facedeco_block': False,
        'required': False,
        'rarity_weights': [100, 2, 2, 2, 2, 2, 2],
        'parity_path': '05_2_Skeleton_Mouth'
    },
    {
        # 80 images
        # 11 elements
        'id': 9,
        'name': 'Eyes',
        'directory': '07_Eyes',
        'skeleton_block': True,
        'only_skeleton': False,
        'no_facedeco_block': False,
        'required': True,
        'rarity_weights': list(repeat(40, 2)) + list(repeat(8, 10)) + list(repeat(40, 6)) + list(repeat(6, 14)) + list(repeat(10, 8)) + list(repeat(40, 2)) + list(repeat(6, 14)) + list(repeat(7, 12)) + list(repeat(40, 4)) + list(repeat(10, 8)),
        'parity_path': None
    },
    {
        'id': 10,
        'name': 'Skeleton Eyes',
        'directory': '07_2_Skeleton_Eyes',
        'skeleton_block': False,
        'only_skeleton': True,
        'no_facedeco_block': False,
        'required': False,
        'rarity_weights': [200, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        'parity_path': '06_2_Skeleton_Eyes'
    },
    {
        'id': 11,
        'name': 'Face-Decoration',
        'directory': '08_Facedeko',
        'skeleton_block': False,
        'only_skeleton': False,
        'no_facedeco_block': True,
        'required': False,
        'rarity_weights': [70] + list(repeat(4, 4)) + list(repeat(5, 3)) + list(repeat(8, 2)) + list(repeat(3, 6)) + list(repeat(4, 1)),
        'parity_path': None
    },
    {
        'id': 12,
        'name': 'Hair-Extensions',
        'directory': '09_HairExtensions',
        'skeleton_block': False,
        'only_skeleton': False,
        'no_facedeco_block': False,
        'required': False,
        'rarity_weights': [70, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
        'parity_path': None
    },
    {
        'id': 13,
        'name': 'Hats',
        'directory': '10_Hats',
        'skeleton_block': False,
        'only_skeleton': False,
        'no_facedeco_block': False,
        'required': False,
        'rarity_weights': [649] + list(repeat(7, 5)) + list(repeat(9, 4)) + list(repeat(9, 4)) + list(repeat(7, 5)) + list(repeat(7, 4)) + list(repeat(9, 4)) + list(repeat(9, 4)) + list(repeat(6, 6)),
        'parity_path': '09_Hats'
    },
    {
        'id': 14,
        'name': 'Head-Decoration',
        'directory': '11_Headdeko',
        'skeleton_block': False,
        'only_skeleton': False,
        'no_facedeco_block': False,
        'required': False,
        'rarity_weights': [1657] + list(repeat(13, 5)) + list(repeat(16, 4)) + list(repeat(22, 6)) + list(repeat(11, 6)) + list(repeat(5, 15)) + list(repeat(22, 3)) + list(repeat(16, 4)) + list(repeat(16, 4)) + list(repeat(4, 12)) + list(repeat(11, 6)),
        'parity_path': '10_Headdeko'
    },
    {
        'id': 15,
        'name': 'Left-Hand Back',
        'directory': '12_Lefthand-Back',
        'skeleton_block': False,
        'only_skeleton': False,
        'no_facedeco_block': False,
        'required': False,
        'rarity_weights': [100, 0, 0, 0, 0],  # all values must be set to '0' here
        'parity_path': '11_Lefthand-Back'
    },
    {
        'id': 16,
        'name': 'Left-Hand Thing',
        'directory': '13_Lefthand-Thing',
        'skeleton_block': False,
        'only_skeleton': False,
        'no_facedeco_block': False,
        'required': True,
        'rarity_weights': [625] + list(repeat(11, 5)) + list(repeat(9, 6)) + list(repeat(8, 7)) + list(repeat(9, 6)) + list(repeat(11, 5)) + list(repeat(18, 3)) + list(repeat(11, 5)) + list(repeat(9, 6)) + list(repeat(9, 6)) + list(repeat(18, 3)) + list(repeat(16, 4)),
        'parity_path': '12_Lefthand-Thing'
    },
    {
        'id': 17,
        'name': 'Left-Hand Front',
        'directory': '14_Lefthand-Front',
        'skeleton_block': False,
        'only_skeleton': False,
        'no_facedeco_block': False,
        'required': False,
        'rarity_weights': [100, 0, 0, 0, 0],  # all values must be set to '0' here
        'parity_path': '13_Lefthand-Front'
    },
    {
        'id': 18,
        'name': 'Right-Hand Back',
        'directory': '15_Righthand-Back',
        'skeleton_block': False,
        'only_skeleton': False,
        'no_facedeco_block': False,
        'required': False,
        'rarity_weights': [100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # all values must be set to '0' here
        'parity_path': '14_Righthand-Back'
    },
    {
        'id': 19,
        'name': 'Right-Hand Thing',
        'directory': '16_Righthand-Thing',
        'skeleton_block': False,
        'only_skeleton': False,
        'no_facedeco_block': False,
        'required': True,
        'rarity_weights': list(repeat(18, 5)) + list(repeat(23, 4)) + list(repeat(30, 3)) + list(repeat(90, 1)) + list(repeat(18, 5)) + list(repeat(90, 1)) + list(repeat(13, 7)) + list(repeat(18, 5)) + list(repeat(23, 4)) + list(repeat(45, 2)) + list(repeat(18, 5)) + list(repeat(23, 4)) + list(repeat(15, 6)) + list(repeat(90, 1)) + list(repeat(15, 6)) + list(repeat(6, 8)) + list(repeat(23, 4)) + list(repeat(180, 4)) + list(repeat(6, 8)) + list(repeat(180, 4)),
        'parity_path': '15_Righthand-Thing'
    },
    {
        'id': 20,
        'name': 'Right-Hand Front',
        'directory': '17_Righthand-Front',
        'skeleton_block': False,
        'only_skeleton': False,
        'no_facedeco_block': False,
        'required': False,
        'rarity_weights': [100, 0, 0, 0, 0, 0, 0, 0, 0],  # all values must be set to '0' here
        'parity_path': '16_Righthand-Front'
    }
]