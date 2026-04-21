<p align="center">
  <img src="./assets/banner.jpeg" alt="holbertonschool-higher-level-programming Banner" width="400">
</p>

# Python - Everything is Object

> Before you touch the interpreter, read, think, and reason — then verify.

---

## 📝 Description

This project is a deep philosophical and technical dive into how Python treats objects in memory. The twist: I'm not allowed to just run the code and copy the output. I have to think first — understand why Python behaves the way it does with identities, references, aliases, mutability, and function argument passing. The questions look simple; the reasoning behind them is what matters. By the end, I can explain Python's object model without a single Google search.

---

## 🎯 Learning Objectives

By the end of this project, I am able to explain what an object is, the difference between a class and an instance, and the distinction between mutable and immutable objects. I understand what references, assignments, and aliases are, how to check whether two variables point to the same object (using `is`) or are just equal in value (using `==`), and how to retrieve a variable's memory address with `id()`. I know which built-in types are mutable (lists, dicts, sets) and which are immutable (integers, strings, tuples), and I understand exactly how Python passes arguments to functions and what that means for mutable vs immutable objects.

---

## 🛠️ Technologies Used

This project is written in Python 3 (version 3.8.5), running on Ubuntu 20.04 LTS, using the CPython implementation with default configuration. Answer files are plain `.txt` files containing a single line. Code files follow pycodestyle 2.7.*. No external modules are used.

---

## ⚙️ Requirements

**Python Scripts**
- OS: Ubuntu 20.04 LTS
- Python version: `python3` (3.8.5)
- All files must end with a new line
- The first line of all `.py` files must be exactly: `#!/usr/bin/python3`
- A README.md file at the root of the project is mandatory
- Code must follow pycodestyle (version 2.7.*)
- All files must be executable

**Answer `.txt` Files**
- Only one line per file
- No shebang on the first line
- All files must end with a new line

---

## 🚀 Installation

```bash
git clone https://github.com/GwenP88/holbertonschool-higher_level_programming.git
cd holbertonschool-higher_level_programming/python-everything_is_object
```

---

## ▶️ Usage / Execution

```bash
# For Python scripts:
chmod +x filename.py
./filename.py

# Answer files are plain text and can be read with:
cat N-answer.txt
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

### Tasks 0–1 - Type and identity functions

- Mandatory
- Identify the Python built-in functions used to get the type and memory address of an object
- Answer: function names only, without parentheses

**Files:** `0-answer.txt`, `1-answer.txt`

---

### Tasks 2–5 - Do variables point to the same object?

- Mandatory
- Reason through whether pairs of variables reference the same object in memory using CPython's integer caching rules
- `Yes` or `No` answers based on understanding of object identity vs value equality

**Files:** `2-answer.txt` through `5-answer.txt`

---

### Tasks 6–13 - Equality vs identity for strings and lists

- Mandatory
- Predict what `==` and `is` print for strings and lists under various assignment scenarios, including direct assignment, aliasing, and separate instantiation
- Understand string interning, list mutability, and how CPython handles object identity

**Files:** `6-answer.txt` through `13-answer.txt`

---

### Tasks 14–18 - Mutation, reassignment, and function scope

- Mandatory
- Predict what scripts print when lists are mutated with `append`, reassigned with `+`, passed to functions, or reassigned inside functions
- Understand the difference between in-place mutation (affects the alias) and reassignment (creates a new binding)

**Files:** `14-answer.txt` through `18-answer.txt`

---

### Task 19 - Copy a list object

- Mandatory
- Write a function `copy_list(a_list)` that returns a shallow copy of the list; max 3 lines; no imports
- The copy must be a new object (`is` returns `False`) with the same values (`==` returns `True`)

**Files:** `19-copy_list.py`

---

### Tasks 20–26 - Tuple identity questions

- Mandatory
- Determine whether various expressions create tuples, and predict whether empty/singleton/identical tuples share the same identity in CPython
- Understand that `(1)` is an integer, `(1,)` is a tuple, and CPython caches the empty tuple singleton

**Files:** `20-answer.txt` through `26-answer.txt`

---

### Tasks 27–28 - List identity after `+` vs `+=`

- Mandatory
- Predict whether `a = a + [5]` and `a += [4]` preserve the same object identity for a list
- `a = a + [5]` creates a new list object; `a += [4]` uses `__iadd__` and modifies in place

**Files:** `27-answer.txt`, `28-answer.txt`

---

### Task 29 - Blog post

- Mandatory
- Write a comprehensive blog post covering: introduction, `id` and `type`, mutable objects, immutable objects, why mutability matters, and how Python passes arguments to functions
- Published on Medium or LinkedIn with code examples and at least one image

**Files:** *(blog post link — see repository)*

---

### Task 30 - #pythonic

- Advanced - **This task is still in progress — my future self is on it.**
- Write a function `magic_string()` that returns `"BestSchool"` repeated `n` times (where `n` is the call count), comma-separated; max 4 lines; no imports
- Uses a mutable default argument or closure to track call count across invocations

**Files:** `100-magic_string.py`

---

### Task 31 - Low memory cost

- Advanced - **This task is still in progress — my future self is on it.**
- Write a class `LockedClass` that prevents the creation of new instance attributes except for `first_name`, using `__slots__`
- No imports; any attempt to set an undefined attribute raises `AttributeError`

**Files:** `101-locked_class.py`

---

### Tasks 32–35 - CPython internals: int and string object creation

- Advanced - **This task is still in progress — my future self is on it.**
- Answer questions about how many int or string objects are created and deleted during specific script executions, based on CPython's small integer cache (`NSMALLPOSINTS`) and string interning behavior
- Requires understanding of CPython's memory optimization strategies under the hood

**Files:** `103-line1.txt`, `103-line2.txt`, `104-line1.txt` through `104-line5.txt`, `105-line1.txt`, `106-line1.txt` through `106-line5.txt`

---

## 🔮 What’s Next

I plan to continue working on this project by completing the advanced tasks that are not done yet. This will allow me to deepen my understanding, improve my skills, and push a bit further beyond the basics (because stopping halfway is not really my style).

---

## 🤝 Contributions & Acknowledgements

Thanks to Holberton School for a project that genuinely rewired how I think about variables in Python. The moment I truly understood that assignment is not copying — it's binding — was a good moment. The `+=` vs `+` list identity question was the cherry on top.

---

## 👤 Author

**Gwenaelle PICHOT**
- Student at Holberton School
- Track: holbertonschool-higher_level_programming
- Project: python-everything_is_object