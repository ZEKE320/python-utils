from collections import defaultdict


def update_set_val(word_dict: defaultdict, key: str, values: set) -> None:
    word_dict[key].update(values)


def invert_dict(input_dict: defaultdict) -> dict:
    output_dict = {}
    for key, values in input_dict.items():
        for value in values:
            output_dict[value].add(key)
    return output_dict
