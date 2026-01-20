#!/usr/bin/python3
def common_elements(set_1, set_2):
    """
    value_set = set()
    for value in set_1:
        if value in set_2:
            value_set.add(value)
    return value_set
    """
    return set_1 & set_2
