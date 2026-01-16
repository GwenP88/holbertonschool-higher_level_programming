#!/usr/bin/python3

# NOTE: This script depends on the provided compiled module `hidden_4.pyc`.
# The `.pyc` file is Python-version specific (compiled for the Holberton sandbox, typically Python 3.8),
# so importing it may fail locally on a different Python version (e.g. 3.12) with "bad magic number".
# Run it in the Holberton sandbox (or with Python 3.8) to get the expected output.


import hidden_4

if __name__ == "__main__":
    names = sorted(dir(hidden_4))
    for name in names:
        if not name.startswith("__"):
            print("{}".format(name))
