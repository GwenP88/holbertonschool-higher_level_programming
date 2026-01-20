#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    else:
        pair = iter(a_dictionary.items())
        best_key, max_score = next(pair)
        for key, value in pair:
            if max_score < value:
                max_score = value
                best_key = key
        return best_key  
