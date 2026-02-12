#!/usr/bin/env python3
"""Convert CSV data to JSON"""
import csv
import json


def convert_csv_to_json(filename_csv):
    """Convert a CSV file to JSON and write it to data.json"""
    try:
        with open(filename_csv, "r", encoding="utf-8") as fcsv:
            reader = csv.DictReader(fcsv)
            liste = []
            for row in reader:
                liste.append(row)
            with open("data.json", "w", encoding="utf-8") as fjson:
                json.dump(liste, fjson)
        return True
    except (FileNotFoundError):
        return False
