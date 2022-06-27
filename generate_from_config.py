import os
from image_generator import _generate_single_image

gender = 'male'
color = 'ShiningOrange'
skin = 'Ghost'

filename = f'hair_{color}_Chinballs_{skin}_{gender}.png'
genderpath = os.path.join('assets', gender)



def main():
    output_path = os.path.join('output', 'chosen_generation', 'images')
    male_configs = [
        '00_Background\\Green.png',
        f'01_Body\\SKIN_Standard_{skin}.png',
        f'02_Clothes\\IsHairNakedShoes_Adam_{color}.png',
        f'03_Shoes\\HasNakedShoes_Barefoot_Open{skin}.png',
        f'04_Hair\\HAIR_Standard_{color}.png',
        f'05_Chindeko\\SKIN_Chinballs_{skin}.png',
        '06_Mouth\\IsAlive_SootherGreen_Basic.png',
        '07_Eyes\\IsAlive_HeartsBlue_Basic.png',
        '10_Hats\\FezDefault.png',
        f'11_Headdeko\\HAIR_Sheep_{color}.png',
        f'12_Lefthand-Back\\SKIN_HOLDSTRAIGHT_{skin}.png',
        '13_Lefthand-Thing\\MULTI-SKIN_GiraffaDefault_HOLDSTRAIGHT.png',
        f'14_Lefthand-Front\\SKIN_HOLDSTRAIGHT_{skin}.png',
        f'15_Righthand-Back\\SKIN_HOLDSTRAIGHT_{skin}.png',
        '16_Righthand-Thing\\MULTI-SKIN_PennonMint_HOLDSTRAIGHT.png',
        f'17_Righthand-Front\\SKIN_HOLDSTRAIGHT_{skin}.png'
    ]

    female_configs = [
        '00_Background\\Green.png',
        '01_Body\\SKIN_Standard_light.png',
        '02_Clothes\\BikerLime.png',
        '03_Shoes\\HasNakedShoes_Barefoot_Openlight.png',
        f'04_Hair\\HAIR_Standard_{color}.png',
        '05_Mouth\\IsAlive_SootherGreen_Basic.png',
        '06_Eyes\\IsAlive_HeartsBlue_Basic.png',
        '07_Facedeko\\Tattoo.png',
        f'08_HairExtensions\\HAIR_Pigtail_{color}.png',
        '09_Hats\\FezDefault.png',
        f'10_Headdeko\\HAIR_Sheep_{color}.png',
        '11_Lefthand-Back\\SKIN_HOLDSTRAIGHT_light.png',
        '12_Lefthand-Thing\\MULTI-SKIN_GiraffaDefault_HOLDSTRAIGHT.png',
        '13_Lefthand-Front\\SKIN_HOLDSTRAIGHT_light.png',
        '14_Righthand-Back\\SKIN_HOLDSTRAIGHT_light.png',
        '15_Righthand-Thing\\MULTI-SKIN_PennonMint_HOLDSTRAIGHT.png',
        '16_Righthand-Front\\SKIN_HOLDSTRAIGHT_light.png'
    ]


    if not os.path.exists(output_path):
        os.makedirs(output_path)

    configs = male_configs
    if gender == 'female':
        configs = female_configs

    _generate_single_image(configs, genderpath, os.path.join(output_path, filename))
    print("Generated")


# Run the main function
if __name__ == "__main__":
    main()
