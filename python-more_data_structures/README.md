# Python - More Data Structures: Set, Dictionary

> Sets, dicts, lambdas, and the magical trio of map/filter/reduce — because lists alone just aren't enough.

---

## 📝 Description

This project takes my Python data structure skills up a notch. I move beyond lists and tuples to explore sets, dictionaries, and functional programming tools like `map`, `filter`, and `lambda`. From squaring matrix values without a single loop to converting Roman numerals to integers on a whiteboard, this project challenges me to think more abstractly and write more expressive, Pythonic code.

---

## 🎯 Learning Objectives

By the end of this project, I am able to explain what sets are, how to use them, and when to prefer them over lists or dictionaries. I understand how to iterate over a set and use its most common methods. I can work with dictionaries, understand what keys are, iterate over key-value pairs, and know when a dictionary is the right tool for the job. I also understand what lambda functions are and how to apply `map`, `filter`, and `reduce` to transform and process data without explicit loops.

---

## 🛠️ Technologies Used

This project is written entirely in Python 3 (version 3.8.5), running on Ubuntu 20.04 LTS. The `functools` module may be used for `reduce`. Code style is enforced with pycodestyle 2.7.*. One advanced task uses `map` exclusively — no `for` or `while` loops allowed.

---

## ⚙️ Requirements

- OS: Ubuntu 20.04 LTS
- Python version: `python3` (3.8.5)
- All files must end with a new line
- The first line of all files must be exactly: `#!/usr/bin/python3`
- A README.md file at the root of the project is mandatory
- Code must follow pycodestyle (version 2.7.*)
- All files must be executable
- No module imports allowed unless explicitly stated

---

## 🚀 Installation

```bash
git clone https://github.com/GwenP88/holbertonschool-higher_level_programming.git
cd holbertonschool-higher_level_programming/python-more_data_structures
```

---

## ▶️ Usage / Execution

All Python scripts can be executed in two ways:

### 1. Direct execution
Make the file executable and run it directly:
```bash
chmod +x filename.py
./filename.py
```

### 2. Using Python interpreter
Run the script with Python:
```bash
python3 filename.py
```

---

## 📊 Project Progress

<p align="center">
<img src="assets/progress_barre_100.gif" alt="Mandatory tasks progress" width="80%">
</p>

<p align="center">
<sub>Mandatory tasks completion: 100% --- Advanced tasks completion: 100%</sub>
</p>

---

## ✨ Features

### Task 0 - Squared simple

- Mandatory
- Compute the square of all integers in a 2D matrix and return a new matrix
- No imports; the original matrix must not be modified; regular loops or `map` allowed
- Returns a new matrix of the same size with each value squared

**Files:** `0-square_matrix_simple.py`

---

### Task 1 - Search and replace

- Mandatory
- Replace all occurrences of a given element with another in a new list
- No imports
- Returns a new list with all matching elements replaced; original list unchanged

**Files:** `1-search_replace.py`

---

### Task 2 - Unique addition

- Mandatory
- Add all unique integers in a list (each integer counted only once)
- No imports
- Returns the sum of all distinct integers in the list

**Files:** `2-uniq_add.py`

---

### Task 3 - Present in both

- Mandatory
- Return a set of elements that appear in both input sets
- No imports
- Returns the intersection of the two sets

**Files:** `3-common_elements.py`

---

### Task 4 - Only differents

- Mandatory
- Return a set of elements that appear in only one of the two input sets
- No imports
- Returns the symmetric difference of the two sets

**Files:** `4-only_diff_elements.py`

---

### Task 5 - Number of keys

- Mandatory
- Return the number of keys in a dictionary
- No imports
- Returns an integer representing the total number of keys

**Files:** `5-number_keys.py`

---

### Task 6 - Print sorted dictionary

- Mandatory
- Print a dictionary's key-value pairs sorted alphabetically by key (first level only)
- No imports; all keys are assumed to be strings
- Keys are printed in alphabetical order with their associated values

**Files:** `6-print_sorted_dictionary.py`

---

### Task 7 - Update dictionary

- Mandatory
- Replace or add a key-value pair in a dictionary
- No imports; if the key exists, its value is updated; otherwise it is created
- Returns the updated dictionary

**Files:** `7-update_dictionary.py`

---

### Task 8 - Simple delete by key

- Mandatory
- Delete a key from a dictionary; if the key doesn't exist, the dictionary is unchanged
- No imports
- Returns the updated dictionary

**Files:** `8-simple_delete.py`

---

### Task 9 - Multiply by 2

- Mandatory
- Return a new dictionary with all integer values multiplied by 2
- No imports; the original dictionary is not modified
- Returns a new dictionary with doubled values

**Files:** `9-multiply_by_2.py`

---

### Task 10 - Best score

- Mandatory
- Return the key with the highest integer value in a dictionary
- No imports; returns `None` if the dictionary is empty or `None`
- Returns the key associated with the maximum value

**Files:** `10-best_score.py`

---

### Task 11 - Multiply by using map

- Mandatory
- Return a new list with all values multiplied by a given number, using `map` — no loops
- No imports; file must be 3 lines maximum
- Returns a new list of the same length with each element multiplied

**Files:** `11-multiply_list_map.py`

---

### Task 12 - Roman to Integer

- Mandatory
- Convert a Roman numeral string to an integer (values between 1 and 3999)
- No Google allowed — whiteboard first; returns `0` if input is not a string or is `None`
- Returns the integer value corresponding to the Roman numeral

**Files:** `12-roman_to_int.py`

---

### Task 13 - Weighted average!

- Advanced
- Return the weighted average of a list of `(score, weight)` tuples
- No imports; returns `0` if the list is empty
- Returns the computed weighted average as a float

**Files:** `100-weight_average.py`

---

### Task 14 - Squared by using map

- Advanced
- Square all values in a 2D matrix using `map` only — no `for`, no `while`, max 3 lines
- No imports; original matrix must not be modified
- Returns a new squared matrix of the same dimensions

**Files:** `101-square_matrix_map.py`

---

### Task 15 - Delete by value

- Advanced
- Delete all keys in a dictionary that have a specific value
- No imports; if the value doesn't exist, the dictionary is unchanged
- Returns the updated dictionary with all matching keys removed

**Files:** `102-complex_delete.py`

---

## 🤝 Contributions & Acknowledgements

Thanks to the Holberton School staff and students who made the whiteboard Roman numeral challenge feel slightly less terrifying. You know who you are.

---

## 👤 Author

**Gwenaelle PICHOT**
- Student at Holberton School
- Track: holbertonschool-higher_level_programming
- Project: python-more_data_structures