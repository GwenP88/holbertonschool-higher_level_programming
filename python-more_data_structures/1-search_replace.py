#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for value in my_list:
        if value == search:
            value = replace
            new_list.append(value)
        else:
            new_list.append(value)
    return new_list
