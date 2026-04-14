# Python - Abstract Classes, Interfaces, and OOP Design Patterns

> Abstract, inherit, mix, override — the full OOP toolkit, no assembly required.

---

## 📝 Description

This project is a hands-on exploration of advanced Object-Oriented Programming concepts in Python: abstract classes, interfaces through duck typing, subclassing built-in types, method overriding, multiple inheritance, and mixins. I design class hierarchies that enforce contracts, extend Python's built-in data structures, and compose behaviors modularly using mixins. By the end, I think in terms of blueprints, protocols, and composition — not just flat scripts.

---

## 🎯 Learning Objectives

By the end of this project, I understand how to use abstract base classes (ABCs) to define mandatory interfaces for subclasses. I grasp the concept of duck typing and can write functions that operate on objects based on their behavior rather than their type. I know how to extend Python's built-in classes like `list` and `iter` to create customized data structures. I can apply method overriding to modify inherited behavior, use multiple inheritance to combine features from several parent classes, and leverage mixins to compose modular, reusable behavior across unrelated classes.

---

## 🛠️ Technologies Used

This project is written in Python 3 (version 3.8.5), running on Ubuntu 20.04 LTS. It uses Python's built-in `abc` module for abstract base classes, and the `math` module for geometric calculations. Code style is enforced with pycodestyle 2.7.*.

---

## ⚙️ Requirements

- OS: Ubuntu 20.04 LTS
- Python version: `python3` (3.8.5)
- All files must end with a new line
- The first line of all files must be exactly: `#!/usr/bin/env python3`
- A README.md file at the root of the project is mandatory
- Code must follow pycodestyle (version 2.7.*)
- All files must be executable
- Imports are allowed where explicitly required (e.g., `abc`, `math`)

---

## 🚀 Installation

```bash
git clone https://github.com/GwenP88/holbertonschool-higher_level_programming.git
cd holbertonschool-higher_level_programming/python-abc
```

---

## ▶️ Usage / Execution

All Python scripts can be executed in two ways:

### 1. Direct execution
```bash
chmod +x main_XX_taskname.py
./main_XX_taskname.py
```

### 2. Using Python interpreter
```bash
python3 main_XX_taskname.py
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

### Task 0 - Abstract Animal Class and its Subclasses

- Mandatory
- Create an abstract class `Animal` using the `ABC` module with an abstract method `sound`; implement `Dog` and `Cat` subclasses returning `"Bark"` and `"Meow"` respectively
- Attempting to instantiate `Animal` directly raises a `TypeError`
- Each concrete subclass implements `sound()` and can be instantiated independently

**Files:** `task_00_abc.py`

---

### Task 1 - Shapes, Interfaces, and Duck Typing

- Mandatory
- Create an abstract `Shape` class with abstract `area` and `perimeter` methods; implement `Circle` and `Rectangle` subclasses; write a `shape_info(shape)` function that uses duck typing to print area and perimeter
- No `isinstance` checks in `shape_info` — the function trusts the object's interface
- `shape_info` works with any object that implements `area()` and `perimeter()`, regardless of its class

**Files:** `task_01_duck_typing.py`

---

### Task 2 - Extending the Python List with Notifications

- Mandatory
- Create a `VerboseList` class that extends Python's built-in `list`; override `append`, `extend`, `remove`, and `pop` to print a notification message for each operation
- `super()` is used to preserve the original list behavior; notification messages are printed after additions and before removals
- Every list modification prints a descriptive message, making data flow transparent and auditable

**Files:** `task_02_verboselist.py`

---

### Task 3 - CountedIterator — Keeping Track of Iteration

- Mandatory
- Create a `CountedIterator` class that wraps a built-in iterator and counts how many items have been fetched via `__next__`; provides a `get_count()` method to retrieve the counter
- `StopIteration` is re-raised when the wrapped iterator is exhausted; the count only increments on successful fetches
- Iterating over a `CountedIterator` tracks exactly how many items have been consumed

**Files:** `task_03_countediterator.py`

---

### Task 4 - The Enigmatic FlyingFish — Exploring Multiple Inheritance

- Mandatory
- Create `Fish` and `Bird` base classes, each with `swim`/`fly` and `habitat` methods; create a `FlyingFish` class inheriting from both and overriding all three methods with unique messages
- Python's Method Resolution Order (MRO) determines which inherited method is called; `FlyingFish.mro()` reveals the resolution chain
- `FlyingFish` correctly overrides all parent methods and demonstrates how Python resolves multiple inheritance

**Files:** `task_04_flyingfish.py`

---

### Task 5 - The Mystical Dragon — Mastering Mixins

- Mandatory
- Create two focused mixin classes `SwimMixin` and `FlyMixin`, each providing one behavior; create a `Dragon` class inheriting from both and adding a `roar()` method
- Mixins are designed to be combined, not instantiated alone; `Dragon` composes both behaviors cleanly
- A `Dragon` instance can `swim()`, `fly()`, and `roar()` — behavior composed through mixins without deep inheritance chains

**Files:** `task_05_dragon.py`

---

## 🤝 Contributions & Acknowledgements

Thanks to the Holberton School team for designing exercises that actually make you think. The FlyingFish MRO diagram alone was worth the whole project. Also, dragons are a perfectly valid use case for mixins.

---

## 👤 Author

**Gwenaelle PICHOT**
- Student at Holberton School
- Track: holbertonschool-higher_level_programming
- Project: python-abc