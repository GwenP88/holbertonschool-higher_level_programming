def magic_string():
    magic_string.count += 1; text = "BestSchool, " * magic_string.count; return text[:-2]
magic_string.count = 0
