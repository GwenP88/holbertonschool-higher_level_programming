# Python - Hello, World

> My first steps into Python — printing things, slicing strings, and discovering that there are ten ways to do everything.

---

## 📝 Description

This project is my introduction to Python programming. I explore the very foundations of the language: how to print text and variables, how strings work, and how to manipulate them using indexing and slicing. It is a gentle but thorough entry point into a language that rewards curiosity — and punishes inconsistent indentation. As Guillaume wisely said: enjoy it!

---

## 🎯 Learning Objectives

By the end of this project, I am able to use the Python interpreter to run scripts and understand how it executes code. I know how to print text and variables using the `print` function, including the use of f-strings for clean and readable output. I understand what strings are and how to work with them, including how indexing and slicing allow me to extract specific characters or substrings with precision. I am also familiar with the official Python coding style guide (pycodestyle) and how to check my code against it to ensure clean, readable, and standards-compliant scripts.

---

## 🛠️ Technologies Used

This project uses Python 3 (version 3.8.*), interpreted on Ubuntu 20.04 LTS. Style compliance is enforced with pycodestyle (version 2.7.*). No external libraries are required — just Python and its built-in capabilities.

---

## ⚙️ Requirements

- OS: Ubuntu 20.04 LTS
- Python version: `python3` (3.8.*)
- All files must end with a new line
- The first line of all files must be exactly: `#!/usr/bin/python3`
- A README.md file at the root of the repo and at the root of this project folder is mandatory
- Code must follow pycodestyle (version 2.7.*)
- All files must be executable
- File length is tested using `wc`

---

## 🚀 Installation

```bash
git clone https://github.com/GwenP88/holbertonschool-higher_level_programming.git
cd holbertonschool-higher_level_programming/python-hello_world
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

### Task 0 - Hello, print

- **Status:** Mandatory
- **Objective:** Write a Python script that prints an exact string using the `print` function.
- **Constraint:** Must use the `print` function. Output must match exactly, including quotation marks.
- **Expected behavior:** Running `./2-print.py` prints `"Programming is like building a multilingual puzzle` followed by a new line.

**Files:** `2-print.py`

---

### Task 1 - Print integer

- **Status:** Mandatory
- **Objective:** Print an integer stored in a variable followed by a string, using f-strings.
- **Constraint:** Cannot cast the variable to a string. Code must be exactly 3 lines long. Must use f-strings.
- **Expected behavior:** Running `./3-print_number.py` prints `98 Battery street`.

**Files:** `3-print_number.py`

---

### Task 2 - Print float

- **Status:** Mandatory
- **Objective:** Print a float stored in a variable with a precision of 2 decimal digits using f-strings.
- **Constraint:** Cannot cast the variable to a string. Must use f-strings.
- **Expected behavior:** Running `./4-print_float.py` prints `Float: 3.14`.

**Files:** `4-print_float.py`

---

### Task 3 - Print string

- **Status:** Mandatory
- **Objective:** Print a string 3 times, then print its first 9 characters, using slicing.
- **Constraint:** No loops or conditional statements allowed. Program must be maximum 5 lines long.
- **Expected behavior:** Running `./5-print_string.py` prints `Holberton SchoolHolberton SchoolHolberton School` then `Holberton`.

**Files:** `5-print_string.py`

---

### Task 4 - Play with strings

- **Status:** Mandatory
- **Objective:** Use two existing string variables to print `Welcome to Holberton School!`.
- **Constraint:** No loops or conditionals. Must use variables `str1` and `str2`. Program must be exactly 5 lines long.
- **Expected behavior:** Running `./6-concat.py` prints `Welcome to Holberton School!`.

**Files:** `6-concat.py`

---

### Task 5 - Copy - Cut - Paste

- **Status:** Mandatory
- **Objective:** Use string slicing to extract the first 3 letters, last 2 letters, and middle part of a word.
- **Constraint:** No loops or conditionals. Program must be exactly 8 lines long.
- **Expected behavior:** Running `./7-edges.py` prints `First 3 letters: Hol`, `Last 2 letters: on`, `Middle word: olberto`.

**Files:** `7-edges.py`

---

### Task 6 - Create a new sentence

- **Status:** Mandatory
- **Objective:** Use slicing on existing variables to print `object-oriented programming with Python`.
- **Constraint:** No loops, no new variables, no string literals. Program must be exactly 5 lines long.
- **Expected behavior:** Running `./8-concat_edges.py` prints `object-oriented programming with Python`.

**Files:** `8-concat_edges.py`

---

### Task 7 - Easter Egg

- **Status:** Mandatory
- **Objective:** Write a script that prints "The Zen of Python" by Tim Peters.
- **Constraint:** Script must be maximum 98 characters long (checked with `wc -m`).
- **Expected behavior:** Running `./9-easter_egg.py` prints the full Zen of Python text.

**Files:** `9-easter_egg.py`

---

## 🤝 Contributions & Acknowledgements

Thanks to Guillaume and the Holberton School team for the warm welcome into the Python world — and for reminding me that there are ten ways to do the same thing, and I just have to find the one that passes the checker. Special mention to Tim Peters for the Zen, which I now know by heart (almost).

---

## 👤 Author

**Gwenaelle PICHOT**
- Student at Holberton School
- Track: holbertonschool-higher_level_programming
- Project: python-hello_world