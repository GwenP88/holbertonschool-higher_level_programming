#!/usr/bin/python3
def uniq_add(my_list=[]):
    total = 0
    value_list = []
    for value in my_list:
        if value not in value_list:
            total += value
            value_list.append(value)
    return total
