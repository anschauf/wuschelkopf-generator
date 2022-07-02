import os

import character_generation_configs
from image_generator import _generate_single_image

gender = 'female'
color = 'Blue'
skin = 'choco'

# filename = f'hair_{color}_Chinballs_{skin}_{gender}.png'
filename = f'no_background_choco_mage_female.png'
genderpath = os.path.join('assets', gender)



def main():
    output_path = os.path.join('output', 'chosen_generation', 'images')
    male_configs = [
        '00_Background\\Green.png',
        f'01_Body\\SKIN_Standard_{skin}.png',
        f'02_Clothes\\IsHairNakedShoes_Adam_{color}.png',
        f'03_Shoes\\HasNakedShoes_Barefoot_Open{skin}.png',
        f'04_Hair\\HAIR_Standard_{color}.png',
        f'05_Chindeko\\HAIR_Beard_{color}.png',
        '06_Mouth\\IsAlive_OneTooth_Basic.png',
        '07_Eyes\\IsAlive_HeartsBlue_Basic.png',
        '10_Hats\\FezDefault.png',
        f'11_Headdeko\\HAIR_Sheep_{color}.png',
        f'12_Lefthand-Back\\SKIN_HOLDSTRAIGHT_{skin}.png',
        '13_Lefthand-Thing\\MULTI-SKIN_WalkingstickWhite_HOLDSTRAIGHT.png',
        f'14_Lefthand-Front\\SKIN_HOLDSTRAIGHT_{skin}.png',
        f'15_Righthand-Back\\SKIN_HOLDSTRAIGHT_{skin}.png',
        '16_Righthand-Thing\\MULTI-SKIN_PennonMint_HOLDSTRAIGHT.png',
        f'17_Righthand-Front\\SKIN_HOLDSTRAIGHT_{skin}.png'
    ]

    female_configs = [
        '00_Background\\Lightblue.png',
        f'01_Body\\SKIN_Standard_{skin}.png',
        '02_Clothes\\BikerPurple.png',
        f'03_Shoes\\HasNakedShoes_HighHeelsRed_Closed{skin}.png',
        f'04_Hair\\HAIR_Standard_{color}.png',
        '05_Mouth\\IsAlive_Fangs_Basic.png',
        # 'Skeleton_Mouth\\BlingGold.png',
        '06_Eyes\\IsAlive_ShiningPurple_Basic.png',
        # 'Skeleton_Eyes\\Rubinleft.png',
        '07_Facedeko\\Tattoo.png',
        # '09_Hats\\WizardhatRed.png',
        f'10_Headdeko\\SKIN_ElvenearsAndHornsWhite_{skin}.png',
        f'11_Lefthand-Back\\SKIN_HOLDSTRAIGHT_{skin}.png',
        '12_Lefthand-Thing\\MULTI-SKIN_WalkingstickWhite_HOLDSTRAIGHT.png',
        f'13_Lefthand-Front\\SKIN_HOLDSTRAIGHT_{skin}.png',
        f'14_Righthand-Back\\SKIN_HOLDSTRAIGHT_{skin}.png',
        '15_Righthand-Thing\\MULTI-SKIN_MagicWandWhite_HOLDSTRAIGHT.png',
        f'16_Righthand-Front\\SKIN_HOLDSTRAIGHT_{skin}.png'
    ]


    if not os.path.exists(output_path):
        os.makedirs(output_path)

    configs = male_configs
    if gender == 'female':
        configs = female_configs

    # _generate_single_image(configs, genderpath, os.path.join(output_path, filename))
    _generate_single_image(character_generation_configs.choco_mage_female, genderpath, os.path.join(output_path, filename))
    print("Generated")


# Run the main function
if __name__ == "__main__":
    main()
