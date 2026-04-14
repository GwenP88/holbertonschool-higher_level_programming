# Python - Data Structures: Lists, Tuples

> From zero to hero with lists and tuples — Python's most essential data containers.

---

## 📝 Description

This project is my deep dive into Python's built-in data structures: lists and tuples. I explore how to manipulate, iterate, and transform sequences in Python — from printing integers in reverse to swapping variables with a single elegant line. Along the way, I also get comfortable with the differences between mutable lists and immutable tuples, and learn when to use each one wisely.

---

## 🎯 Learning Objectives

By the end of this project, I am able to explain what lists are and how to use them effectively, including their most common methods. I understand the differences and similarities between strings and lists, and I know how to use lists as stacks and queues. I can write list comprehensions and use them to produce clean, readable code. I also understand what tuples are, when to prefer them over lists, and how to leverage tuple packing and sequence unpacking. Finally, I know how to use the `del` statement to remove items from a list.

---

## 🛠️ Technologies Used

This project is written entirely in Python 3 (version 3.8.5), running on Ubuntu 20.04 LTS. No external libraries or modules are used — just pure Python and its built-in tools. Code style is enforced with pycodestyle 2.7.*.

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
cd holbertonschool-higher_level_programming/python-data_structures
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
<sub>Mandatory tasks completion: 100%</sub>
</p>

---

## ✨ Features

### Task 0 - Print a list of integers

- Mandatory
- Print all integers of a list, one per line, using `str.format()`
- No imports, no casting to strings — `str.format()` only
- Each integer is printed on its own line

**Files:** `0-print_list_integer.py`

---

### Task 1 - Secure access to an element in a list

- Mandatory
- Retrieve an element from a list at a given index safely
- Returns `None` for negative or out-of-range indices; no `try/except` allowed
- Returns the element at the specified index, or `None` if invalid

**Files:** `1-element_at.py`

---

### Task 2 - Replace element

- Mandatory
- Replace an element at a specific position in a list
- Returns the original list unchanged if `idx` is negative or out of range; no `try/except`
- The list is modified in place and the updated list is returned

**Files:** `2-replace_in_list.py`

---

### Task 3 - Print a list of integers... in reverse!

- Mandatory
- Print all integers of a list in reverse order, one per line, using `str.format()`
- No imports, no casting to strings
- Each integer is printed from last to first

**Files:** `3-print_reversed_list_integer.py`

---

### Task 4 - Replace in a copy

- Mandatory
- Replace an element at a specific position without modifying the original list
- Returns a copy of the list unchanged if `idx` is negative or out of range; no `try/except`
- The original list remains untouched; a new modified list is returned

**Files:** `4-new_in_list.py`

---

### Task 5 - Can you C me now?

- Mandatory
- Remove all occurrences of `c` and `C` from a string
- No imports, no use of `str.replace()`
- Returns the cleaned string with all `c`/`C` characters removed

**Files:** `5-no_c.py`

---

### Task 6 - Lists of lists = Matrix

- Mandatory
- Print a matrix of integers, formatted with `str.format()`
- No imports, no casting to strings
- Each row is printed on its own line with space-separated integers

**Files:** `6-print_matrix_integer.py`

---

### Task 7 - Tuples addition

- Mandatory
- Add two tuples element by element and return a new tuple of 2 integers
- Missing elements default to `0`; extra elements beyond index 1 are ignored
- Returns a tuple with the summed first and second elements of each input

**Files:** `7-add_tuple.py`

---

### Task 8 - More returns!

- Mandatory
- Return a tuple containing the length of a string and its first character
- If the string is empty, the first character value should be `None`
- Returns a tuple `(length, first_char)`

**Files:** `8-multiple_returns.py`

---

### Task 9 - Find the max

- Mandatory
- Find the biggest integer in a list without using the built-in `max()`
- No imports; returns `None` for an empty list
- Returns the maximum integer found in the list

**Files:** `9-max_integer.py`

---

### Task 10 - Only by 2

- Mandatory
- Return a new list of booleans indicating whether each element is divisible by 2
- No imports; the new list must be the same size as the original
- Each position contains `True` if divisible by 2, `False` otherwise

**Files:** `10-divisible_by_2.py`

---

### Task 11 - Delete at

- Mandatory
- Delete the item at a specific index in a list without using `pop()`
- If `idx` is negative or out of range, the list is returned unchanged
- The item is removed in place and the modified list is returned

**Files:** `11-delete_at.py`

---

### Task 12 - Switch

- Mandatory
- Swap the values of variables `a` and `b` in exactly 5 lines of code
- Code must be inserted at line 4; the entire file must be exactly 5 lines
- Outputs the swapped values: `a=10 - b=89`

**Files:** `12-switch.py`

---

## 🤝 Contributions & Acknowledgements

Big thanks to the Holberton School community and fellow students for the collaborative debugging sessions and the occasional "why doesn't this work?!" moments that turned into learning gold.

---

## 👤 Author

**Gwenaelle PICHOT**
- Student at Holberton School
- Track: holbertonschool-higher_level_programming
- Project: python-data_structures