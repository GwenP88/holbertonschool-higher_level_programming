![Python Data Structures Banner](assets/banner.png)

# Python - More Data Structures: Set, Dictionary

## Description
This project focuses on practicing **Python data structures** beyond lists and tuples, especially:
- **Sets** (unique elements, set operations)
- **Dictionaries** (key/value pairs, iteration, updates)
- **Lambda functions** and functional tools like **map**, **filter**, and **reduce**

---

## Learning Objectives
By the end of this project, you should be able to explain:
- Why Python programming is awesome
- What **sets** are, how to use them, and their common methods
- When to use **sets vs lists**
- How to iterate over a set
- What **dictionaries** are, how to use them, and when to use them vs lists/sets
- What a **key** is in a dictionary
- How to iterate over a dictionary
- What a **lambda** function is
- What **map**, **filter**, and **reduce** do (and when to use them)

---

## Requirements
- Allowed editors: `vi`, `vim`, `emacs`
- OS: Ubuntu 20.04 LTS
- Python version: `python3` (3.8.5)
- All files must end with a new line
- First line of all files: `#!/usr/bin/python3`
- `README.md` is mandatory at the root of the project directory
- Code style: `pycodestyle` (version 2.7.\*)
- All files must be executable
- File length will be checked using `wc`
- No importing modules (unless explicitly allowed in a task)

---

## Project Progress

<p align="center">
  <img src="assets/progress_barre_100.gif" alt="Mandatory tasks progress" width="80%">
</p>

<p align="center">
  <sub>Mandatory tasks completion: 100% ---  Advanced tasks completion: 100%</sub>
</p>

---

## Project Files & Tasks

### 0. Squared simple
**File:** `0-square_matrix_simple.py`  
**Prototype:** `def square_matrix_simple(matrix=[]):`  
Creates a **new matrix** where each integer is squared (original matrix unchanged).

---

### 1. Search and replace
**File:** `1-search_replace.py`  
**Prototype:** `def search_replace(my_list, search, replace):`  
Returns a **new list** where all occurrences of `search` are replaced by `replace`.

---

### 2. Unique addition
**File:** `2-uniq_add.py`  
**Prototype:** `def uniq_add(my_list=[]):`  
Adds **each unique integer only once** and returns the total sum.

---

### 3. Present in both
**File:** `3-common_elements.py`  
**Prototype:** `def common_elements(set_1, set_2):`  
Returns a set of elements **present in both** sets.

---

### 4. Only differents
**File:** `4-only_diff_elements.py`  
**Prototype:** `def only_diff_elements(set_1, set_2):`  
Returns a set of elements present in **only one** of the sets.

---

### 5. Number of keys
**File:** `5-number_keys.py`  
**Prototype:** `def number_keys(a_dictionary):`  
Returns the **number of keys** in a dictionary.

---

### 6. Print sorted dictionary
**File:** `6-print_sorted_dictionary.py`  
**Prototype:** `def print_sorted_dictionary(a_dictionary):`  
Prints the dictionary with keys sorted **alphabetically** (first level only).

---

### 7. Update dictionary
**File:** `7-update_dictionary.py`  
**Prototype:** `def update_dictionary(a_dictionary, key, value):`  
Replaces or adds a key/value in a dictionary and returns the updated dictionary.

---

### 8. Simple delete by key
**File:** `8-simple_delete.py`  
**Prototype:** `def simple_delete(a_dictionary, key=""):`  
Deletes a key from a dictionary if it exists (otherwise no change).

---

### 9. Multiply by 2
**File:** `9-multiply_by_2.py`  
**Prototype:** `def multiply_by_2(a_dictionary):`  
Returns a **new dictionary** with all integer values multiplied by 2.

---

### 10. Best score
**File:** `10-best_score.py`  
**Prototype:** `def best_score(a_dictionary):`  
Returns the key with the **highest integer value**. Returns `None` if input is `None` or empty.

---

### 11. Multiply by using map
**File:** `11-multiply_list_map.py`  
**Prototype:** `def multiply_list_map(my_list=[], number=0):`  
Returns a new list with all values multiplied by `number`, **without loops**, using `map`.  
Constraint: file must be **max 3 lines**.

---

### 12. Roman to Integer
**File:** `12-roman_to_int.py`  
**Prototype:** `def roman_to_int(roman_string):`  
Converts a Roman numeral string to an integer.
- Assumes range: **1 to 3999**
- If `roman_string` is not a string or is `None`, return `0`

---

## Advanced Tasks

### 13. Weighted Average! (#advanced)
Write a function that returns the weighted average of all integers tuple `(score, weight)`.

**Prototype:** `def weight_average(my_list=[]):`

**Requirements:**
- Returns `0` if the list is empty
- You are not allowed to import any module

**Repository:**
- **File:** `100-weight_average.py`
- **Directory:** `python-more_data_structures`

---

### 14. Squared by using map (#advanced)
Write a function that computes the square value of all integers of a matrix using `map`.

**Prototype:** `def square_matrix_map(matrix=[]):`

**Requirements:**
- Matrix is a 2D array
- Returns a new matrix of the same size
- Each value is the square of the input value
- Initial matrix must not be modified
- You are not allowed to import any module
- You must use `map`
- You are not allowed to use `for` or `while`
- File must be maximum 3 lines

**Repository:**
- **File:** `101-square_matrix_map.py`
- **Directory:** `python-more_data_structures`

---

### 15. Delete by Value (#advanced)
Write a function that deletes keys with a specific value in a dictionary.

**Prototype:** `def complex_delete(a_dictionary, value):`

**Requirements:**
- If the value doesn’t exist, the dictionary won’t change
- All keys having the searched value must be deleted
- You are not allowed to import any module

**Repository:**
- **File:** `102-complex_delete.py`
- **Directory:** `python-more_data_structures`

---

## Author

**Gwenaelle PICHOT**  
Student at Holberton School  
Track: Higher Level Programming  
Project: Python - Data & Structures (part 2)

