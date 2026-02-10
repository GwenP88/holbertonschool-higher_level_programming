#!/usr/bin/python3
"""Save a Python object to a file in JSON format."""
import json


def save_to_json_file(my_obj, filename):
    """Write a JSON representation of an object to a file."""
    with open(filename, 'w', encoding="utf-8") as fichier:
        fichier.write(json.dumps(my_obj))
