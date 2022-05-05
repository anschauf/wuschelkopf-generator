import constants
import re


def create_attribute_json(all_trait_sets, all_trait_paths, general_traits):
    attributes = list()
    for i, trait_set in enumerate(all_trait_sets):
        trait_paths = all_trait_paths[i]
        general_trait = general_traits[i]
        attributes.append(_create_single_attribute_json(trait_set, trait_paths, general_trait))
    return attributes


def _create_single_attribute_json(trait_set, trait_paths, general_trait):
    attributes = list()

    skip_iter = 0

    attributes.extend([
        {
            constants.trait_type: constants.gender_text,
            constants.value: 'Female' if general_trait[constants.is_female] else 'Male'
        },
        {
            constants.trait_type: constants.base,
            constants.value: 'Dark' if general_trait[constants.skin] == 'choco' else general_trait[
                constants.skin].capitalize()
        },
        {
            constants.trait_type: constants.hair_color_text,
            constants.value: general_trait[constants.hair_color]
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

    if general_trait[constants.skin] != constants.skeleton_skin:
        attributes.extend([
            {
                constants.trait_type: constants.mouth,
                constants.value: _clean_image_name(trait_set[4])
            },
            {
                constants.trait_type: constants.eyes,
                constants.value: _clean_image_name(trait_set[5])
            }
        ])
        skip_iter += 2

    if trait_set[5 + skip_iter]:
        attributes.append(
            {
                constants.trait_type: constants.face_deco_text,
                constants.value: _clean_image_name(trait_set[5 + skip_iter])
            }
        )

    if not general_trait[constants.is_female]:
        if trait_set[6 + skip_iter]:
            attributes.append({
                constants.trait_type: constants.chin_deco_text,
                constants.value: _clean_image_name(trait_set[6 + skip_iter])
            })
            skip_iter += 1

    if trait_set[6 + skip_iter]:
        attributes.append({
            constants.trait_type: constants.hair_extension_text,
            constants.value: _clean_image_name(trait_set[6 + skip_iter])
        })

    if trait_set[7 + skip_iter]:
        attributes.append({
            constants.trait_type: constants.hat_text,
            constants.value: _clean_image_name(trait_set[7 + skip_iter])
        })

    if trait_set[8 + skip_iter]:
        attributes.append({
            constants.trait_type: constants.hair_deco_text,
            constants.value: _clean_image_name(trait_set[8 + skip_iter])
        })

    if trait_set[9 + skip_iter]:
        attributes.append({
            constants.trait_type: constants.left_hand_text,
            constants.value: _clean_image_name(trait_set[9 + skip_iter])
        })

    if trait_set[12 + skip_iter]:
        attributes.append({
            constants.trait_type: constants.right_hand_text,
            constants.value: _clean_image_name(trait_set[12 + skip_iter])
        })



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
    return image_split[1] if (len(image_split) >= 2) else image_name
