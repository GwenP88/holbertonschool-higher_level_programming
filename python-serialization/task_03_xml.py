#!/usr/bin/env python3
"""Serialize a flat dictionary to XML and deserialize it back"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Write a dictionary to an XML file"""
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """Read an XML file and return its content as a dictionary"""
    tree_2 = ET.parse(filename)
    root = tree_2.getroot()
    data = {}
    for child in root:
        data[child.tag] = child.text
    return data
