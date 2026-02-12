#!/usr/bin/env python3
"""Save Python objects to JSON files and load them back."""
import json


def serialize_and_save_to_file(data, filename):
    """Serialize data to JSON and save it to a file."""
    with open(filename, "w", encoding='utf-8') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Load JSON from a file and deserialize it into a Python object."""
    with open(filename, "r") as f:
        return json.load(f)
