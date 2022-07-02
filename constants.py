import os

# indication that the file name must be change according to skin-tone
skin_adapt_pretag = 'SKIN'
skeleton_skin = 'Skeleton'
ghost_skin = 'Ghost'
skin_tones = ['choco', ghost_skin, 'light', skeleton_skin]

male_assets_path = os.path.join('assets', 'male')
female_assets_path = os.path.join('assets', 'female')

# Gender
female_path = 'female'
male_path = 'male'

# Hair color
hair_adapt_pretag = 'HAIR'
hairs = ['Black', 'Blue', 'Brown', 'Burning', 'Green', 'Grey', 'Lime', 'Orange', 'Purple', "Rainbow", 'Red', 'ShiningGreen', 'ShiningOrange', 'ShiningPurple', 'Yellow']

# Ghost or alive
is_alive_adapt_pretag = 'IsAlive'
alive_posttag = 'Basic'
not_alive_posttag = 'Ghost'

# Config blocks
skeleton_block = 'skeleton_block'
only_skeleton = 'only_skeleton'
nofacedeco_block = 'no_facedeco_block'

#Skeleton adaption
is_skeletive_pretag = 'IsSkeletive'
skelet_posttag = 'Skelet'
basic_posttag = 'Basic'

# Multi-Hand (Right Hand)
is_multi_hand_pretag = 'MULTI-SKIN'

# No face deco
is_alive_no_facedeco_pretag = 'IsAliveNoFaceDeco'
no_facedeco_pretag = 'NoFaceDeco'

# Open/ closed shoe naked start
is_naked_shoes = 'IsNakedShoes'
is_hair_naked_shoes = 'IsHairNakedShoes'
is_skin_naked_shoes = 'IsSkinNakedShoes'
naked_shoes_tag = 'HasNakedShoes'
naked_open = 'Open'
naked_closed = 'Closed'


front = 'front'
back = 'back'

# JSON params
is_female = 'is_female'
skin = 'skin'
hair_color = 'hair_color'

trait_type = 'trait_type'
value = 'value'
base = 'Base'
background_color = 'Background-Color'
shoes = 'Shoes'
hair_color_text = 'Hair-Color'
gender_text = 'Gender'
clothing = 'Clothing'
mouth = 'Mouth'
eyes = 'Eyes'
face_deco_text = 'Face-Decoration'
chin_deco_text = 'Chin-Decoration'
hat_text = 'Hat'
hair_extension_text = 'Hair-Extension'
hair_deco_text = 'Hair-Decoration'
left_hand_text = 'Left-Hand'
right_hand_text = 'Right-Hand'

###################################################
# Constant rarities
#####################################################
skeleton_eyes_chance = 80
skeleton_mouth_chance = 80

# alphabetically ordered
skink_colors_rarities = [36, 16, 36, 8]
hair_colors_rarities = [8, 8, 8, 2, 8, 8, 8, 8, 8, 5, 8, 3, 3, 3, 8]

