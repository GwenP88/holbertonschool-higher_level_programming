#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """
    value_set = set()
    for value_1 in set_1:
        if value_1 not in set_2:
            value_set.add(value_1)
    for value_2 in set_2:
        if value_2 not in set_1:
            value_set.add(value_2)
    return value_set
    """
    return set_1 ^ set_2
