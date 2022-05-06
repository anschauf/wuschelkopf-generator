import os

# indication that the file name must be change according to skin-tone
skin_adapt_pretag = 'SKIN'
skeleton_skin = 'Skeleton'
ghost_skin = 'Ghost'
skin_tones = ['light', 'choco', ghost_skin, skeleton_skin]

male_assets_path = os.path.join('assets', 'male')
female_assets_path = os.path.join('assets', 'female')

# Gender
female_path = 'female'
male_path = 'male'

# Hair color
hair_adapt_pretag = 'HAIR'
hairs = ['Blue', 'Brown', 'Burning', 'Green', 'Grey', 'Purple', 'Red', 'Shining', 'Yellow', "Rainbow"]

# Ghost or alive
is_alive_adapt_pretag = 'IsAlive'
alive_posttag = 'Basic'
not_alive_posttag = 'Ghost'

# Skeleton block
skeleton_block = 'skeleton_block'

#Skeleton adaption
is_skeletive_pretag = 'IsSkeletive'
skelet_posttag = 'Skelet'
basic_posttag = 'Basic'

# Multi-Hand (Right Hand)
is_multi_hand_pretag = 'MULTI-SKIN'


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
