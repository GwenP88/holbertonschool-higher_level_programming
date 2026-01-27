![Python Exceptions Banner](assets/banner.png)

# Python - Classes and Objects

## Description
This project introduces Object-Oriented Programming (OOP) in Python through the progressive construction of classes and objects.  
By implementing different versions of a `Square` class and additional data structures, this project focuses on understanding how classes work internally, how attributes and methods are defined and controlled, and how Python handles encapsulation, abstraction, and information hiding.  
The goal is to experiment with OOP concepts by writing, testing, and improving code step by step, while following Python best practices and strict coding standards.

---

## Learning Objectives
With this project, I learned that Object-Oriented Programming is not magic, even if it sometimes looks like it at first.  
I now understand what OOP is, how a class differs from an object or an instance, and why mixing them up is a beginner’s classic mistake.  
I learned how to build classes properly, use attributes and methods, and why `self` is everywhere (and why forgetting it breaks everything).  
I can explain how the `__init__` method works, how objects are initialized, and why validation logic should not be scattered everywhere.  
This project also taught me how to protect my data from myself using public, protected, and private attributes, and how to use properties, getters, and setters the Pythonic way.  
Finally, I learned how Python actually finds attributes behind the scenes, what `__dict__` really contains, and how to dynamically add attributes without summoning chaos.

---

## Requirements
- OS: Ubuntu 20.04 LTS
- Python version: `python3` (3.8.5)
- All files must end with a new line
- The first line of all files must be exactly: `#!/usr/bin/python3`
- A README.md file at the root of the project is mandatory
- Code must follow pycodestyle (version 2.7.*)
- All files must be executable
- No module imports allowed unless explicitly stated

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
<sub>Mandatory tasks completion: 100% ---  Advanced tasks completion: %</sub>
</p>

---

## Tasks
### 0. My first square
- **Status:** Mandatory
- **Objective:** Create an empty class that defines a square
- **Constraints:** No module imports allowed
- **Expected behavior:** The class can be instantiated and has no attributes

**Files**
- `0-square.py`

---

### 1. Square with size
- **Status:** Mandatory
- **Objective:** Define a square with a private size attribute
- **Constraints:** No type or value validation, no module imports
- **Expected behavior:** Size is stored as a private attribute and cannot be accessed directly

**Files**
- `1-square.py`

---

### 2. Size validation
- **Status:** Mandatory
- **Objective:** Add validation rules for the square size
- **Constraints:** Size must be an integer and greater or equal to 0
- **Expected behavior:** Raises appropriate exceptions when size is invalid

**Files**
- `2-square.py`

---

### 3. Area of a square
- **Status:** Mandatory
- **Objective:** Compute and return the area of the square
- **Constraints:** No module imports
- **Expected behavior:** The `area()` method returns the correct square area

**Files**
- `3-square.py`

---

### 4. Access and update private attribute
- **Status:** Mandatory
- **Objective:** Control access to the private size attribute using getter and setter
- **Constraints:** Centralized validation logic in the setter
- **Expected behavior:** Size can be read and updated safely with validation

**Files**
- `4-square.py`

---

### 5. Printing a square
- **Status:** Mandatory
- **Objective:** Display the square using the `#` character
- **Constraints:** Print an empty line if size equals 0
- **Expected behavior:** The square is printed correctly to stdout

**Files**
- `5-square.py`

---

### 6. Coordinates of a square
- **Status:** Mandatory
- **Objective:** Add position handling to control square printing offset
- **Constraints:** Position must be a tuple of two positive integers
- **Expected behavior:** Square is printed with correct horizontal and vertical offsets

**Files**
- `6-square.py`

---

### 7. Singly linked list
- **Status:** Advanced
- **Objective:** Implement a sorted singly linked list
- **Constraints:** Nodes must store integers only, no module imports
- **Expected behavior:** Values are inserted in sorted order and printable

**Files**
- `100-singly_linked_list.py`

---

### 8. Print Square instance
- **Status:** Advanced
- **Objective:** Make the Square instance printable
- **Constraints:** Printing behavior must match `my_print()`
- **Expected behavior:** Printing a Square displays it correctly using `print()`

**Files**
- `101-square.py`

---

### 9. Compare 2 squares
- **Status:** Advanced
- **Objective:** Enable comparison between Square instances
- **Constraints:** Comparison based on square area
- **Expected behavior:** Supports all comparison operators (`==`, `!=`, `<`, `<=`, `>`, `>=`)

**Files**
- `102-square.py`

---

## Authors
**Gwenaelle PICHOT**
- Student at Holberton School
- Track: Higher Level Programming
- Project: Python - Classes and Objects
