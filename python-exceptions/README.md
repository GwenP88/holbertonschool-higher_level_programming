![Python Exceptions Banner](assets/banner.png)

# Python - Exceptions

## Description
This project is an introduction to **exception handling in Python**.  
It focuses on understanding the difference between errors and exceptions, learning how to handle runtime errors properly using `try`, `except`, `else`, and `finally`, and knowing when and how to raise exceptions intentionally.

Exception handling is a key concept in Python that allows programs to **fail gracefully**, avoid crashes, and manage unexpected situations such as invalid user input, division by zero, or accessing elements out of range.

---

## Resources
Read or watch:
- Errors and Exceptions (Python documentation)
- Learn to Program 11 – Static & Exception Handling (from minute 7)

---

## Learning Objectives
At the end of this project, you should be able to explain, without external help:

- Why Python programming is awesome
- The difference between errors and exceptions
- What exceptions are and how to use them
- When exceptions should be used
- How to correctly handle an exception
- The purpose of catching exceptions
- How to raise a built-in exception
- When and why to implement a clean-up action after an exception

---

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- OS: Ubuntu 20.04 LTS
- Python version: `python3` (3.8.5)
- All files must end with a new line
- The first line of all files must be exactly:
  ```
  #!/usr/bin/python3
  ```
- A README.md file at the root of the project is mandatory
- Code must follow pycodestyle (version 2.7.*)
- All files must be executable
- File length will be tested using wc
- No module imports allowed unless explicitly stated
- Use of try / except is mandatory where required
- Use of len() and type() is forbidden where specified

---

## Project Structure

python-exceptions/
├── 0-safe_print_list.py
├── 1-safe_print_integer.py
├── 2-safe_print_list_integers.py
├── 3-safe_print_division.py
├── 4-list_division.py
├── 5-raise_exception.py
├── 6-raise_exception_msg.py
└── README.md

---

## Tasks

### 0. Safe list printing
**File:** `0-safe_print_list.py`

- Prints `x` elements of a list  
- Uses `try / except`  
- Does not use `len()`  
- Returns the real number of elements printed  
- Handles cases where `x` is greater than the list size  

---

### 1. Safe printing of an integers list
**File:** `1-safe_print_integer.py`

- Prints an integer using `"{:d}".format()`  
- Returns `True` if the value is an integer, otherwise `False`  
- Uses `try / except`  
- Does not use `type()`  

---

### 2. Print and count integers
**File:** `2-safe_print_list_integers.py`

- Prints the first `x` elements of a list  
- Only integers are printed; other types are silently ignored  
- Uses `try / except`  
- Does not use `len()`  
- Returns the number of integers printed  
- Raises an exception if the list is too short  

---

### 3. Integers division with debug
**File:** `3-safe_print_division.py`

- Divides two integers  
- Uses `try / except / finally`  
- Prints the result in the `finally` block  
- Returns the division result or `None` if an error occurs  

---

### 4. Divide a list
**File:** `4-list_division.py`

- Divides elements of two lists index by index  
- Returns a new list of size `list_length`  
- Handles the following cases:
  - Wrong type → prints `wrong type`
  - Division by zero → prints `division by 0`
  - Index out of range → prints `out of range`
- Uses `try / except / finally`  
- If a division fails, the result is `0`  

---

### 5. Raise exception
**File:** `5-raise_exception.py`

- Raises a `TypeError`  
- No module imports allowed  

---

### 6. Raise a message
**File:** `6-raise_exception_msg.py`

- Raises a `NameError` with a custom message  
- No module imports allowed  

---

## Author

**Gwenaelle PICHOT**  
Student at Holberton School  
Track: Higher Level Programming  
Project: Python - Exceptions



