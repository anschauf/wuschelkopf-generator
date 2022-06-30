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
        'id': 4,
        'name': 'Shoes',
        'directory': '03_Shoes',
        'required': True,
        'skeleton_block': False,
        'only_skeleton': False,
        'no_facedeco_block': False,
        'rarity_weights': None,
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
        'rarity_weights': None,
        'parity_path': '04_Hair'
    },
    {
        'id': 6,
        'name': 'Chin-Decoration',
        'directory': '05_Chindeko',
        'skeleton_block': False,
        'only_skeleton': False,
        'no_facedeco_block': False,
        'required': False,
        'rarity_weights': None,
        'parity_path': None
    },
    {
        'id': 7,
        'name': 'Mouth',
        'directory': '06_Mouth',
        'skeleton_block': True,
        'only_skeleton': False,
        'no_facedeco_block': False,
        'required': True,
        'rarity_weights': None,
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
        'id': 9,
        'name': 'Eyes',
        'directory': '07_Eyes',
        'skeleton_block': True,
        'only_skeleton': False,
        'no_facedeco_block': False,
        'required': True,
        'rarity_weights': None,
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
        'rarity_weights': None,
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
        'rarity_weights': [100, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
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
        'rarity_weights': None,
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
        'rarity_weights': None,
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
        'rarity_weights': None,
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
        'rarity_weights': None,
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