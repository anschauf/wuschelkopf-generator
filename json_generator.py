import constants
import re
import json


def create_attribute_json(all_trait_sets, all_trait_paths, general_traits):
    attributes = list()
    for i, trait_set in enumerate(all_trait_sets):
        trait_paths = all_trait_paths[i]
        general_trait = general_traits[i]
        attributes.append(_create_single_attribute_json(trait_set, trait_paths, general_trait))
    return json.dumps(attributes)


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
            constants.value: _clean_image_name(trait_set[2]),
        },
        {
            constants.trait_type: constants.shoes,
            constants.value: _clean_image_name(trait_set[3]),
        }
    ])

    if not general_trait[constants.is_female]:
        if trait_set[5 + skip_iter] is not None:
            attributes.append({
                constants.trait_type: constants.chin_deco_text,
                constants.value: _clean_image_name(trait_set[5 + skip_iter])
            })
        skip_iter += 1

    mouth_folder_start = '06'
    if general_trait[constants.is_female]:
        mouth_folder_start = '05'

    eyes_folder_start = '07'
    if general_trait[constants.is_female]:
        eyes_folder_start = '06'

    mouth_trait = None
    mouth_trait_pos = 5 + skip_iter
    eye_trait = None
    eye_trait_pos = mouth_trait_pos + 1

    if trait_paths[mouth_trait_pos].startswith(mouth_folder_start):
        # mouth trait
        mouth_trait = trait_set[mouth_trait_pos]
    else:
        mouth_trait_pos += 1
        if trait_paths[mouth_trait_pos].startswith(mouth_folder_start):
            mouth_trait = trait_set[mouth_trait_pos]

    if trait_paths[eye_trait_pos].startswith(eyes_folder_start):
        eye_trait = trait_set[eye_trait_pos]
    elif trait_paths[eye_trait_pos + 1].startswith(eyes_folder_start):
        eye_trait = trait_set[eye_trait_pos + 1]

    mouth_trait = trait_set[5 + skip_iter]
    eye_trait = trait_set[6 + skip_iter]

    if mouth_trait is not None:
        attributes.append(
            {
                constants.trait_type: constants.mouth,
                constants.value: _clean_image_name(mouth_trait)
            }
        )

    if eye_trait is not None:
        attributes.append(
            {
                constants.trait_type: constants.eyes,
                constants.value: _clean_image_name(eye_trait)
            }
        )

        if str(eye_trait).startswith(constants.is_alive_no_facedeco_pretag):
            skip_iter += 1
        else:
            skip_iter += 2

    if trait_set[5 + skip_iter] is not None and \
            not str(eye_trait).startswith(constants.is_alive_no_facedeco_pretag):
        attributes.append(
            {
                constants.trait_type: constants.face_deco_text,
                constants.value: _clean_image_name(trait_set[5 + skip_iter])
            }
        )

    if trait_set[6 + skip_iter] is not None:
        attributes.append({
            constants.trait_type: constants.hair_extension_text,
            constants.value: _clean_image_name(trait_set[6 + skip_iter])
        })

    if trait_set[7 + skip_iter] is not None:
        attributes.append({
            constants.trait_type: constants.hat_text,
            constants.value: _clean_image_name(trait_set[7 + skip_iter])
        })

    if trait_set[8 + skip_iter] is not None:
        attributes.append({
            constants.trait_type: constants.hair_deco_text,
            constants.value: _clean_image_name(trait_set[8 + skip_iter])
        })


    lefhand_item = trait_set[10 + skip_iter]
    if lefhand_item is not None:
        attributes.append({
            constants.trait_type: constants.left_hand_text,
            constants.value: _clean_image_name(lefhand_item)
        })
        if not str(lefhand_item).startswith(constants.is_multi_hand_pretag):
            skip_iter -= 1

    if trait_set[14 + skip_iter] is not None:
        clean_img_name = str(_clean_image_name(trait_set[14 + skip_iter]))

        if clean_img_name != 'H  O  L  D  S  T  R  A  I  G  H  T' and clean_img_name != 'R  I  G  H  T  S  I  D  E':
            attributes.append({
                constants.trait_type: constants.right_hand_text,
                constants.value: _clean_image_name(trait_set[14 + skip_iter])
            })
    return attributes


def _create_female_json(trait_set, trait_paths, general_trait):
    return {
        constants.background_color: trait_set[0].replace('.png', ''),

    }


def _clean_image_name(originale_image_name: str):
    image_name = _extract_middle_part(originale_image_name)
    image_name = image_name.replace('.png', '')
    image_name = re.split("([A-Z][^A-Z]*)", image_name)
    image_name[0] = image_name[0].capitalize()
    image_name = ' '.join(image_name)
    return image_name.replace('_', ' ').strip()


def _extract_middle_part(image_name: str):
    if image_name is None:
        print("Image name is None")
        return image_name
    else:
        image_split = image_name.split('_')
        return image_split[1] if (len(image_split) >= 2) else image_name
