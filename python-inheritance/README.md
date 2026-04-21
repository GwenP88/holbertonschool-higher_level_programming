<p align="center">
  <img src="./assets/banner.jpeg" alt="holbertonschool-higher-level-programming Banner" width="800">
</p>

# Python - Inheritance

> Standing on the shoulders of classes — because rewriting everything from scratch is so last year.

---

## 📝 Description

This project dives into one of the core pillars of Object-Oriented Programming: inheritance. I learn how to build class hierarchies, reuse and override behavior, and use Python's built-in tools to inspect and validate objects. Starting from simple lookup functions, I progressively build a geometry hierarchy — `BaseGeometry`, `Rectangle`, and `Square` — and explore advanced concepts like inverting comparison operators and dynamically adding attributes to objects.

---

## 🎯 Learning Objectives

By the end of this project, I am able to explain what superclasses, base classes, and subclasses are, and how to create them in Python. I know how to list all attributes and methods of a class or instance, when an instance can have new attributes, and how to define a class with multiple base classes. I understand what the default base class is (everything inherits from `object`), how to override inherited methods and attributes, and which attributes are available through heritage. I can confidently use `isinstance`, `issubclass`, `type`, and `super` in real code.

---

## 🛠️ Technologies Used

This project is written entirely in Python 3 (version 3.8.5), running on Ubuntu 20.04 LTS. All modules, classes, and functions include mandatory docstrings. Doctest files are stored in a `tests/` folder and run with the `doctest` module. Code style is enforced with pycodestyle 2.7.*. No external modules are used.

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
- Do not use the words `import` or `from` inside comments

---

## 🚀 Installation

```bash
git clone https://github.com/GwenP88/holbertonschool-higher_level_programming.git
cd holbertonschool-higher_level_programming/python-inheritance
```

---

## ▶️ Usage / Execution

### Running scripts:
```bash
chmod +x filename.py
./filename.py
```

### Running doctests:
```bash
python3 -m doctest ./tests/filename.txt
python3 -m doctest -v ./tests/filename.txt
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

### Task 0 - Lookup

- Mandatory
- Write a function `lookup(obj)` that returns the list of available attributes and methods of an object
- No imports; uses Python's built-in introspection
- Returns a list of strings representing all accessible names on the object

**Files:** `0-lookup.py`

---

### Task 1 - My list

- Mandatory
- Write a class `MyList` that inherits from `list` and adds a `print_sorted()` method that prints the list in ascending order
- No imports; the original list is not modified by the sort
- `print_sorted()` outputs the sorted version without altering the original instance

**Files:** `1-my_list.py`, `tests/1-my_list.txt`

---

### Task 2 - Exact same object

- Mandatory
- Write a function `is_same_class(obj, a_class)` that returns `True` only if the object is exactly an instance of the specified class
- No imports; uses `type()` comparison — not `isinstance`
- Returns `False` even for subclasses of the specified class

**Files:** `2-is_same_class.py`

---

### Task 3 - Same class or inherit from

- Mandatory
- Write a function `is_kind_of_class(obj, a_class)` that returns `True` if the object is an instance of, or inherits from, the specified class
- No imports; uses `isinstance()`
- Returns `True` for the class itself and any of its subclasses

**Files:** `3-is_kind_of_class.py`

---

### Task 4 - Only sub class of

- Mandatory
- Write a function `inherits_from(obj, a_class)` that returns `True` only if the object's class is a subclass (direct or indirect) of the specified class — not the class itself
- No imports
- Returns `False` if the object is an exact instance of `a_class`

**Files:** `4-inherits_from.py`

---

### Task 5 - Geometry module

- Mandatory
- Write an empty class `BaseGeometry`
- No imports
- A valid, instantiable empty class ready to be extended

**Files:** `5-base_geometry.py`

---

### Task 6 - Improve Geometry

- Mandatory
- Add a public `area()` method to `BaseGeometry` that raises `Exception` with the message `area() is not implemented`
- No imports; forces subclasses to implement `area()`
- Calling `area()` on a `BaseGeometry` instance raises an exception with a clear message

**Files:** `6-base_geometry.py`

---

### Task 7 - Integer validator

- Mandatory
- Add `integer_validator(self, name, value)` to `BaseGeometry`; raises `TypeError` if value is not an integer, `ValueError` if value is ≤ 0
- No imports; `name` is always a string; `bool` is not considered a valid integer
- Provides reusable validation for all geometry subclasses

**Files:** `7-base_geometry.py`, `tests/7-base_geometry.txt`

---

### Task 8 - Rectangle

- Mandatory
- Write a `Rectangle` class inheriting from `BaseGeometry`; accepts `width` and `height`, both validated as positive integers
- No imports; no getters or setters — dimensions are private and validated at init time
- Instantiation with invalid values raises the appropriate exception from `integer_validator`

**Files:** `8-rectangle.py`

---

### Task 9 - Full rectangle

- Mandatory
- Extend `Rectangle` with an `area()` implementation and a `__str__` that returns `[Rectangle] <width>/<height>`
- No imports; builds on `8-rectangle.py`
- `print(rectangle)` outputs a formatted description; `area()` returns the correct value

**Files:** `9-rectangle.py`

---

### Task 10 - Square #1

- Mandatory
- Write a `Square` class inheriting from `Rectangle`; accepts `size`, validated as a positive integer; implements `area()`
- No imports; `size` is private with no getter or setter
- `print(square)` outputs `[Rectangle] size/size`; `area()` returns `size²`

**Files:** `10-square.py`

---

### Task 11 - Square #2

- Mandatory
- Override `__str__` in `Square` to return `[Square] <size>/<size>` instead of `[Rectangle] ...`
- No imports; builds on `10-square.py`
- `print(square)` now correctly identifies the shape as a square

**Files:** `11-square.py`

---

### Task 12 - My integer

- Advanced
- Write a `MyInt` class inheriting from `int` with inverted `==` and `!=` operators
- No imports; `__eq__` returns what `__ne__` normally would, and vice versa
- A rebellious integer where `MyInt(3) == 3` is `False` and `MyInt(3) != 3` is `True`

**Files:** `100-my_int.py`

---

### Task 13 - Can I?

- Advanced
- Write a function `add_attribute(obj, name, value)` that adds a new attribute to an object if possible; raises `TypeError` with `can't add new attribute` if not
- No imports; no `try/except` allowed; checks for `__dict__` on the object
- Works for custom class instances; raises `TypeError` for built-in types like strings

**Files:** `101-add_attribute.py`

---

## 🤝 Contributions & Acknowledgements

Thanks to Holberton School and fellow students for the collaborative doctest sessions. Writing tests together means fewer edge cases slip through — and more laughs when they do.

---

## 👤 Author

**Gwenaelle PICHOT**
- Student at Holberton School
- Track: holbertonschool-higher_level_programming
- Project: python-inheritance