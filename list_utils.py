def remove_duplicates_and_sort(word_list: list) -> list:
    word_set: set = set(word_list)
    no_duplication_list: list = list(word_set)
    return sorted(no_duplication_list)