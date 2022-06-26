import os
from image_generator import _generate_single_image

filename = 'chosen3.png'
gender = 'male'
genderpath = os.path.join('assets', gender)


def main():
    output_path = os.path.join('output', 'chosen_generation', 'images')
    configs = [
        '00_Background\\Green.png',
        '01_Body\\SKIN_Standard_light.png',
        '02_Clothes\\IsHairNakedShoes_Adam_Orange.png',
        '03_Shoes\\HasNakedShoes_Barefoot_Openlight.png',
        '04_Hair\\HAIR_Standard_Orange.png',
        '06_Mouth\\IsAlive_SootherGreen_Basic.png',
        '07_Eyes\\IsAlive_HeartsBlue_Basic.png',
        '08_Facedeko\\Tattoo.png',
        '10_Hats\\FezDefault.png',
        '11_Headdeko\\SKIN_ElvenearsAndHornsWhite_light.png',
        '12_Lefthand-Back\\SKIN_HOLDSTRAIGHT_light.png',
        '13_Lefthand-Thing\\MULTI-SKIN_GiraffaDefault_HOLDSTRAIGHT.png',
        '14_Lefthand-Front\\SKIN_HOLDSTRAIGHT_light.png',
        '15_Righthand-Back\\SKIN_HOLDSTRAIGHT_light.png',
        '16_Righthand-Thing\\MULTI-SKIN_PennonMint_HOLDSTRAIGHT.png',
        '17_Righthand-Front\\SKIN_HOLDSTRAIGHT_light.png'
    ]

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    _generate_single_image(configs, genderpath, os.path.join(output_path, filename))
    print("Generated")


# Run the main function
if __name__ == "__main__":
    main()
