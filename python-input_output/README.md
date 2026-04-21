<p align="center">
  <img src="./assets/banner.jpeg" alt="holbertonschool-higher-level-programming Banner" width="600">
</p>

# Python - Input / Output

> Files, JSON, and Pascal's Triangle — because data that can't be saved is just a memory leak waiting to happen.

---

## 📝 Description

This project is my deep dive into file handling and data serialization in Python. I learn to read, write, and append to files safely using the `with` statement, convert Python objects to JSON and back, build a class-based serialization system for students, and tackle the classic Pascal's Triangle challenge. I also get comfortable with reading data from the command line and parsing log output — skills that turn out to be extremely useful in the real world.

---

## 🎯 Learning Objectives

By the end of this project, I am able to explain how to open, read, write, and append to files in Python, and how to move the file cursor. I know how to use the `with` statement to guarantee proper file closure. I understand what JSON is, what serialization and deserialization mean, and how to convert Python data structures to and from JSON strings. I also know how to access command-line parameters in a Python script using `sys.argv`.

---

## 🛠️ Technologies Used

This project is written in Python 3 (version 3.8.5), running on Ubuntu 20.04 LTS. It uses the built-in `json` and `sys` modules. All modules, classes, and functions include meaningful docstrings. Test cases use the `doctest` module. Code style is enforced with pycodestyle 2.7.*.

---

## ⚙️ Requirements

**Python Scripts**
- OS: Ubuntu 20.04 LTS
- Python version: `python3` (3.8.5)
- All files must end with a new line
- The first line of all files must be exactly: `#!/usr/bin/python3`
- A README.md file at the root of the project is mandatory
- Code must follow pycodestyle (version 2.7.*)
- All files must be executable

**Python Test Cases**
- All test files must be inside a `tests/` folder with `.txt` extension
- Tests are executed with: `python3 -m doctest ./tests/*`
- All modules, classes, and functions must have meaningful docstrings

---

## 🚀 Installation

```bash
git clone https://github.com/GwenP88/holbertonschool-higher_level_programming.git
cd holbertonschool-higher_level_programming/python-input_output
```

---

## ▶️ Usage / Execution

### Running scripts:
```bash
chmod +x filename.py
./filename.py
```

### Load/add/save script:
```bash
./7-add_item.py arg1 arg2 arg3
```

### Log parsing (advanced):
```bash
./101-generator.py | ./101-stats.py
```

---

## 📊 Project Progress

<p align="center">
<img src="assets/progress_barre_100.gif" alt="Mandatory tasks progress" width="80%">
</p>

<p align="center">
<sub>Mandatory tasks completion: 100% --- Advanced tasks completion: 0%</sub>
</p>

---

## ✨ Features

### Task 0 - Read file

- Mandatory
- Write a function `read_file(filename="")` that reads a UTF-8 text file and prints its content to stdout
- Must use `with` statement; no imports; no exception management required
- Prints the entire file content exactly as-is to stdout

**Files:** `0-read_file.py`

---

### Task 1 - Write to a file

- Mandatory
- Write a function `write_file(filename="", text="")` that writes a string to a UTF-8 file and returns the number of characters written; creates or overwrites the file
- Must use `with` statement; no imports
- Returns the integer count of characters written to the file

**Files:** `1-write_file.py`

---

### Task 2 - Append to a file

- Mandatory
- Write a function `append_write(filename="", text="")` that appends a string to a UTF-8 file and returns the number of characters added; creates the file if it doesn't exist
- Must use `with` statement; no imports
- Each call appends to the end of the file without overwriting existing content

**Files:** `2-append_write.py`

---

### Task 3 - To JSON string

- Mandatory
- Write a function `to_json_string(my_obj)` that returns the JSON string representation of an object
- No exception management required; uses the `json` module
- Returns a valid JSON string for serializable Python objects; raises `TypeError` for non-serializable types like sets

**Files:** `3-to_json_string.py`

---

### Task 4 - From JSON string to Object

- Mandatory
- Write a function `from_json_string(my_str)` that returns the Python object represented by a JSON string
- No exception management required; uses the `json` module
- Returns the deserialized Python data structure from the input JSON string

**Files:** `4-from_json_string.py`

---

### Task 5 - Save Object to a file

- Mandatory
- Write a function `save_to_json_file(my_obj, filename)` that writes a Python object to a file using JSON representation
- Must use `with` statement; no exception management for non-serializable objects or file permissions
- Saves a valid JSON file containing the object's serialized representation

**Files:** `5-save_to_json_file.py`

---

### Task 6 - Create object from a JSON file

- Mandatory
- Write a function `load_from_json_file(filename)` that creates a Python object from a JSON file
- Must use `with` statement; no exception management required
- Returns the deserialized Python data structure from the contents of the JSON file

**Files:** `6-load_from_json_file.py`

---

### Task 7 - Load, add, save

- Mandatory
- Write a script that loads a list from `add_item.json` (creating it if absent), appends all command-line arguments to the list, and saves it back
- Uses `save_to_json_file` and `load_from_json_file` from previous tasks; no exception management for file permissions
- Persistent list that grows with each script execution and command-line arguments provided

**Files:** `7-add_item.py`

---

### Task 8 - Class to JSON

- Mandatory
- Write a function `class_to_json(obj)` that returns a dictionary of an object's attributes suitable for JSON serialization
- No imports; works with any class whose attributes are lists, dicts, strings, integers, or booleans
- Returns `obj.__dict__` filtered to serializable types

**Files:** `8-class_to_json.py`

---

### Task 9 - Student to JSON

- Mandatory
- Write a `Student` class with public attributes `first_name`, `last_name`, and `age`; add a `to_json()` method that returns the instance's dictionary representation
- No imports; equivalent to calling `class_to_json` on the student instance
- Returns a clean dictionary of all student attributes

**Files:** `9-student.py`

---

### Task 10 - Student to JSON with filter

- Mandatory
- Extend `Student.to_json(self, attrs=None)` to accept an optional list of attribute names; only those attributes are included if provided
- No imports; non-existent attribute names in the filter list are silently ignored
- Returns a filtered or full dictionary depending on whether `attrs` is provided

**Files:** `10-student.py`

---

### Task 11 - Student to disk and reload

- Mandatory
- Add `reload_from_json(self, json)` to `Student` that updates all instance attributes from a dictionary; enables full serialization and deserialization of student objects
- No imports; a dictionary key maps directly to a public attribute name
- A student can be saved to disk as JSON and fully reconstructed from it with no data loss

**Files:** `11-student.py`

---

### Task 12 - Pascal's Triangle

- Mandatory
- Write a function `pascal_triangle(n)` that returns a list of lists representing Pascal's triangle up to row `n`; returns an empty list if `n <= 0`
- No imports; whiteboard first — no googling
- Returns the correct triangular structure where each value is the sum of the two values above it

**Files:** `12-pascal_triangle.py`

---

### Task 13 - Search and update

- Advanced - **This task is still in progress — my future self is on it.**
- Write a function `append_after(filename="", search_string="", new_string="")` that inserts `new_string` after every line containing `search_string` in a file
- Must use `with` statement; no imports; no exception management
- Each matching line is immediately followed by the new string in the updated file

**Files:** `100-append_after.py`

---

### Task 14 - Log parsing

- Advanced - **This task is still in progress — my future self is on it.**
- Write a script `101-stats.py` that reads log lines from stdin and computes metrics every 10 lines and on keyboard interruption: total file size and count per status code
- Uses `sys` for stdin; only tracks valid status codes (200, 301, 400, 401, 403, 404, 405, 500); prints stats in ascending code order
- Produces running statistics from a continuous stream of HTTP log data, flushing output gracefully on `CTRL+C`

**Files:** `101-stats.py`

---

## 🔮 What’s Next

I plan to continue working on this project by completing the advanced tasks that are not done yet. This will allow me to deepen my understanding, improve my skills, and push a bit further beyond the basics (because stopping halfway is not really my style).

---

## 🤝 Contributions & Acknowledgements

Thanks to everyone at Holberton School who helped me understand that "saving data" is actually a deeply philosophical act. Also, Pascal's Triangle on a whiteboard without Google is surprisingly manageable — and surprisingly satisfying.

---

## 👤 Author

**Gwenaelle PICHOT**
- Student at Holberton School
- Track: holbertonschool-higher_level_programming
- Project: python-input_output