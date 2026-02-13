![Python Data Structures Banner](assets/banner.png)

# Python – Data Structures: Lists, Tuples

## Description
This project is part of the **Holberton School – Higher Level Programming** curriculum.  
It focuses on understanding and using **Python data structures**, mainly **lists** and **tuples**, through a series of practical functions.

The goal is to learn how to manipulate collections of data efficiently while respecting strict coding constraints and style guidelines.

---

## Usage / Execution
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

## Project Progress

<p align="center">
  <img src="assets/progress_barre_100.gif" alt="Mandatory tasks progress" width="80%">
</p>

<p align="center">
  <sub>Mandatory tasks completion: 100%</sub>
</p>

---

## Learning Objectives

During this project, I learned what lists are and how to use them efficiently to store and manipulate multiple values in a single variable. 
I discovered the similarities between lists and strings (they both love being indexed) as well as their differences (lists are flexible, strings… much less).

I learned how to use common list methods without fighting with the documentation every five minutes, and how lists can behave like stacks or queues depending on how you use them. 
I also learned what list comprehensions are, and how they make the code shorter, cleaner, and slightly more satisfying to read.

I learned what tuples are and when it is smarter to use them instead of lists, especially when data should not be modified. 
Along the way, I understood what a sequence is in Python, how tuple packing and sequence unpacking work, and how the `del` statement can make things disappear (sometimes a bit too efficiently).

---

## Requirements

- **Language:** Python 3.8.5  
- **OS:** Ubuntu 20.04 LTS  
- **Editors:** `vi`, `vim`, `emacs`
- All files must:
  - End with a new line
  - Start with `#!/usr/bin/python3`
  - Be executable
  - Follow **pycodestyle** (version 2.7.\*)
- No external modules allowed unless specified
- File length is checked using `wc`

---

## Project Progress

<p align="center">
  <img src="assets/progress-mandatory-100.gif" alt="Mandatory tasks progress" width="80%">
</p>

<p align="center">
  <sub>Mandatory tasks completion: 100%</sub>
</p>

---

## Tasks Overview

## Task "0" - "Import a simple function from a simple file"
- **Task status:** mandatory
- **Task objectives:** Import `add` from `add_0.py` and print `1 + 2 = 3`.
- **Task constraint:**
  - Define `a = 1` and `b = 2` on separate lines.
  - Use formatted `print`.
  - Use `add_0` only once.
  - No `*`, no `__import__`.
  - Must not execute when imported.
- **Expected behavior:** Output exactly `1 + 2 = 3`.
- **Files:** `python-import_modules/0-add.py`


## Task "1" - "My first toolbox!"
- **Task status:** mandatory
- **Task objectives:** Import math functions and print operations.
- **Task constraint:**
  - Define `a = 10`, `b = 5` (separate lines).
  - Use only `a` and `b`.
  - Max 4 `print`.
  - Use `calculator_1` once.
  - No `*`, no `__import__`.
  - Must not execute when imported.
- **Expected behavior:**
  - `10 + 5 = 15`
  - `10 - 5 = 5`
  - `10 * 5 = 50`
  - `10 / 5 = 2`
- **Files:** `python-import_modules/1-calculation.py`


## Task "2" - "How to make a script dynamic!"
- **Task status:** mandatory
- **Task objectives:** Print number and list of CLI arguments.
- **Task constraint:**
  - Use `len(argv)`.
  - Correct singular/plural.
  - Number arguments starting at 1.
  - Must not execute when imported.
- **Expected behavior:** Matches given format.
- **Files:** `python-import_modules/2-args.py`


## Task "3" - "Infinite addition"
- **Task status:** mandatory
- **Task objectives:** Add all CLI arguments.
- **Task constraint:**
  - Cast with `int()`.
  - Print total.
  - Must not execute when imported.
- **Expected behavior:** Works with large numbers.
- **Files:** `python-import_modules/3-infinite_add.py`


## Task "4" - "Who are you?"
- **Task status:** mandatory
- **Task objectives:** Print public names from `hidden_4.pyc`.
- **Task constraint:**
  - File in `/tmp/`.
  - Alphabetical order.
  - Exclude names starting with `__`.
  - Must not execute when imported.
- **Expected behavior:** One name per line.
- **Files:** `/tmp/4-hidden_discovery.py`


## Task "5" - "Everything can be imported"
- **Task status:** mandatory
- **Task objectives:** Import and print variable `a`.
- **Task constraint:**
  - No `*`, no `__import__`.
  - Must not execute when imported.
- **Expected behavior:** Prints `98`.
- **Files:** `python-import_modules/5-variable_load.py`


## Task "6" - "Build my own calculator!"
- **Task status:** advanced
- **Task objectives:** Handle basic operations from CLI.
- **Task constraint:**
  - Usage: `./100-my_calculator.py a operator b`
  - Valid operators: `+ - * /`
  - Invalid args → print usage, exit 1.
  - Unknown operator → error message, exit 1.
  - No `*`, no `__import__`.
  - Must not execute when imported.
- **Expected behavior:** `<a> <operator> <b> = <result>`
- **Files:** `python-import_modules/100-my_calculator.py`


## Task "7" - "Easy print"
- **Task status:** advanced
- **Task objectives:** Print `#pythoniscool`.
- **Task constraint:**
  - Max 2 lines.
  - No `print`, `eval`, `open`, `import sys`.
- **Expected behavior:** Prints `#pythoniscool`.
- **Files:** `python-import_modules/101-easy_print.py`


## Task "8" - "ByteCode -> Python #3"
- **Task status:** advanced
- **Task objectives:** Reproduce given bytecode logic.
- **Task constraint:**
  - Implement `magic_calculation(a, b)`.
  - Follow exact bytecode behavior.
- **Expected behavior:** Same logic as provided bytecode.
- **Files:** `python-import_modules/102-magic_calculation.py`


## Task "9" - "Fast alphabet"
- **Task status:** advanced
- **Task objectives:** Print uppercase alphabet.
- **Task constraint:**
  - Max 3 lines.
  - No loops.
  - No conditionals.
  - No `str.join()`.
  - No string literal.
  - No system calls.
- **Expected behavior:** `ABCDEFGHIJKLMNOPQRSTUVWXYZ`
- **Files:** `python-import_modules/103-fast_alphabet.py`
---

## Author

**Gwenaelle PICHOT**  
Student at Holberton School  
Track: Higher Level Programming  
Project: Python - Date & structure (part 1)
