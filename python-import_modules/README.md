![ChatGPT Introduction Banner](assets/banner.png)

# Python - Import & Modules

This project focuses on understanding how Python modules work, how to import functions and variables, how to use command line arguments, and how to prevent code from being executed when a file is imported.

---

## Learning Objectives

At the end of this project, you should be able to explain, without using Google:

### General
- Why Python programming is awesome  
- How to import functions from another file  
- How to use imported functions  
- How to create a module  
- How to use the built-in function `dir()`  
- How to prevent code in your script from being executed when imported  
- How to use command line arguments with your Python programs  

---

## Requirements

### General
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 22.04 LTS using `python3` (version 3.10.*)
- All files must end with a new line
- The first line of all files must be exactly: `#!/usr/bin/python3`
- A `README.md` file at the root of the project folder is mandatory
- Code must follow `pycodestyle` (version 2.7.*)
- All files must be executable
- File length will be tested using `wc`

---

## Tasks

### 0. Import a simple function from a simple file
**File:** `0-add.py`

Write a program that imports the function `add(a, b)` from `add_0.py` and prints the result of `1 + 2 = 3`.

Constraints:
- Use `print` with string format to display integers
- Assign `a = 1` and `b = 2` on two different lines
- Use `a` and `b` as arguments when calling `add`
- Output format: `<a> + <b> = <add(a, b)>`
- Use the word `add_0` only once
- Do not use `*` for importing or `__import__`
- The code must not be executed when imported

---

### 1. My first toolbox!
**File:** `1-calculation.py`

Write a program that imports functions from `calculator_1.py`, performs basic math operations, and prints the results.

Constraints:
- Do not use `print` more than 4 times
- Define `a = 10` and `b = 5` on two different lines
- Use only `a` and `b` as arguments when calling functions (including `print`)
- Call each imported function (`add`, `sub`, `mul`, `div`)
- Use the word `calculator_1` only once
- Do not use `*` for importing or `__import__`
- The code must not be executed when imported

Expected output:

```
10 + 5 = 15
10 - 5 = 5
10 * 5 = 50
10 / 5 = 2
```

---

### 2. How to make a script dynamic!
**File:** `2-args.py`

Write a program that prints the number of arguments and the list of its arguments.

Rules:
- If no arguments: print `0 arguments.`
- If one argument: print `1 argument:`
- Otherwise: print `<number> arguments:`
- If there is at least one argument, print one line per argument:
  - `<position>: <argument>` (position starts at 1)
- Use `len(argv)` to get the number of arguments
- The code must not be executed when imported

---

### 3. Infinite addition
**File:** `3-infinite_add.py`

Write a program that prints the result of the addition of all arguments.

Rules:
- Print the sum followed by a new line
- Cast arguments to integers using `int()`
- Handle very large numbers correctly
- The code must not be executed when imported

---

### 4. Who are you?
**File:** `4-hidden_discovery.py` (must be located in `/tmp/`)

Write a program that prints all the names defined by the compiled module `hidden_4.pyc`.

Rules:
- This task must be done on the sandbox only
- Download `hidden_4.pyc` locally
- Print one name per line, in alphabetical order
- Print only names that do not start with `__`
- The code must not be executed when imported

---

### 5. Everything can be imported
**File:** `5-variable_load.py`

Write a program that imports the variable `a` from `variable_load_5.py` and prints its value.

Rules:
- Do not use `*` for importing or `__import__`
- The code must not be executed when imported

---

### 6. Build my own calculator!
**#advanced**  
**File:** `100-my_calculator.py`

- Imports all functions from `calculator_1.py`
- Handles basic operations between two integers
- Usage: `./100-my_calculator.py <a> <operator> <b>`
- If the number of arguments is not 3:
  - Prints `Usage: ./100-my_calculator.py <a> <operator> <b>`
  - Exits with status `1`
- Supported operators:
  - `+` for addition
  - `-` for subtraction
  - `*` for multiplication
  - `/` for division
- If the operator is invalid:
  - Prints `Unknown operator. Available operators: +, -, * and /`
  - Exits with status `1`
- Casts arguments to integers using `int()`
- Prints the result as: `<a> <operator> <b> = <result>`
- Does not use `*` for importing or `__import__`
- Code must not execute when imported

---

### 7. Easy print
**#advanced**  
**File:** `101-easy_print.py`

- Prints `#pythoniscool` followed by a new line
- Program length: maximum **2 lines**
- Does **not** use:
  - `print`
  - `eval`
  - `open`
  - `import sys`

---

### 8. ByteCode → Python #3
**#advanced**  
**File:** `102-magic_calculation.py`

- Implements the function `magic_calculation(a, b)`
- The function must behave **exactly** like the provided Python bytecode
- Uses imported functions `add` and `sub` from `magic_calculation_102`
- Requires understanding of Python bytecode translation
- Tip provided: *Python bytecode*

---

### 9. Fast alphabet
**#advanced**  
**File:** `103-fast_alphabet.py`

- Prints the alphabet in **uppercase**, followed by a new line
- Program length: maximum **3 lines**
- Does **not** use:
  - Any loops
  - Any conditional statements
  - `str.join()`
  - Any string literal
  - Any system calls

---

## Author

**Gwenaelle PICHOT**  
Student at Holberton School  
Track: Higher Level Programming  
Project: Python - Import & modules





