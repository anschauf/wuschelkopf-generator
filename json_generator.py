import constants
import re


def create_attribute_json(all_trait_sets, all_trait_paths, general_traits):

    attributes = list()
    for i, trait_set in enumerate(all_trait_sets):
        trait_paths = all_trait_paths[i]
        general_trait = general_traits[i]

        if general_trait[constants.is_female]:
            attributes.append(_create_female_json(trait_set, trait_paths, general_trait))
        else:
            attributes.append(_create_male_json(trait_set, trait_paths, general_trait))
    return attributes


def _create_male_json(trait_set, trait_paths, general_trait):
    attributes = list()

    attributes.extend([
        {
            constants.trait_type: constants.base,
            constants.value: 'Dark' if general_trait[constants.skin] == 'choco' else general_trait[constants.skin].capitalize()
        },
        {
            constants.trait_type: constants.background_color,
            constants.value: trait_set[0].replace('.png', '')
        },
        {
            constants.trait_type: constants.clothing,
            constants.value: _clean_image_name(trait_set[3]),
        }
    ])

    if not general_trait[constants.skin] == constants.skeleton_skin:
        attributes.append({constants.trait_type: constants.mouth, constants.value: _clean_image_name(trait_set[4])})

    return attributes


def _create_female_json(trait_set, trait_paths, general_trait):
    return {
        constants.background_color: trait_set[0].replace('.png', ''),

    }


def _clean_image_name(image_name: str):
    image_name = _extract_middle_part(image_name)
    image_name = image_name.replace('.png', '')
    image_name = re.split("([A-Z][^A-Z]*)", image_name)
    image_name[0] = image_name[0].capitalize()
    image_name = ' '.join(image_name)
    return image_name.replace('_', ' ').strip()


def _extract_middle_part(image_name: str):
    image_split = image_name.split('_')
    return image_split[1] if(len(image_split) >= 2) else image_name
