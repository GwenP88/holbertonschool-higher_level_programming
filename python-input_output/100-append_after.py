#!/usr/bin/python3
"""Insert text after matching lines in a file."""


def append_after(filename="", search_string="", new_string=""):
    """Insert new_string after each line
    containing search_string in filename.
    """
    with open(filename, 'r') as file_read:
        line_list = []
        for line in file_read:
            line_list.append(line)
            if search_string in line:
                line_list.append(new_string)
    with open(filename, 'w') as file_write:
        new_text = ''.join(line_list)
        file_write.write(new_text)
