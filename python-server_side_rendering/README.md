# Python - Server-Side Rendering

> Flask + Jinja: generating HTML on the server so browsers don't have to suffer.

---

## 📝 Description

This project introduces me to Server-Side Rendering (SSR) using Python, Flask, and the Jinja2 templating engine. Instead of sending raw data to the browser and letting JavaScript figure it out, I generate fully-formed HTML pages on the server and deliver them ready to display. I start with simple string templating, build a multi-page Flask app with reusable headers and footers, integrate dynamic data from JSON, CSV, and SQLite, and finish with a complete data-driven product catalog — all rendered server-side.

---

## 🎯 Learning Objectives

By the end of this project, I am able to explain the difference between server-side and client-side rendering and articulate the benefits of SSR for SEO, performance, and maintainability. I can implement SSR in Python using Flask and the Jinja2 templating engine, dynamically render HTML pages using loops and conditionals, read and display data from JSON files, CSV files, and SQLite databases, and handle dynamic content and user inputs through URL query parameters.

---

## 🛠️ Technologies Used

This project is written in Python 3, running on Ubuntu 20.04 LTS. It uses the Flask web framework and the Jinja2 templating engine (included with Flask). Standard library modules `json`, `csv`, and `sqlite3` are used for data reading. HTML templates are organized in a `templates/` folder. Flask runs on port 5000 in debug mode.

---

## ⚙️ Requirements

- OS: Ubuntu 20.04 LTS
- Python version: `python3`
- Flask: install with `pip install Flask`
- All files must end with a new line
- A README.md file at the root of the project is mandatory
- Templates must be stored in a `templates/` folder
- Flask app must run on port 5000

---

## 🚀 Installation

```bash
git clone https://github.com/GwenP88/holbertonschool-higher_level_programming.git
cd holbertonschool-higher_level_programming/python-server_side_rendering
pip install Flask
```

---

## ▶️ Usage / Execution

Run any Flask application with:

```bash
python3 task_XX_name.py
```

Then open your browser at `http://localhost:5000`.

For query parameter routes:
```
http://localhost:5000/products?source=json
http://localhost:5000/products?source=csv
http://localhost:5000/products?source=sql
http://localhost:5000/products?source=json&id=1
```

For the templating script (Task 0):
```bash
python3 main_00_intro.py
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

### Task 0 - Creating a Simple Templating Program

- Mandatory
- Write a `generate_invitations(template, attendees)` function that fills a text template with attendee data and writes one output file per attendee, named `output_1.txt`, `output_2.txt`, etc.
- Validates input types (template must be a string, attendees a list of dicts); logs errors for empty template or empty list; missing values are replaced with `"N/A"`
- Generates personalized invitation files from a shared template with full error handling for all edge cases

**Files:** `task_00_intro.py`

---

### Task 1 - Creating a Basic HTML Template in Flask

- Mandatory
- Build a basic Flask app with three routes (`/`, `/about`, `/contact`) each rendering an HTML template; create reusable `header.html` and `footer.html` components included across all pages using Jinja's `{% include %}`
- Flask runs on port 5000; templates live in a `templates/` folder; navigation links are in the header
- A multi-page Flask app with consistent layout and zero HTML duplication across pages

**Files:** `task_01_jinja.py`

---

### Task 2 - Creating a Dynamic Template with Loops and Conditions in Flask

- Mandatory
- Add a `/items` route that reads a list from `items.json` and renders it dynamically using a Jinja `{% for %}` loop; displays `"No items found"` if the list is empty via a `{% if %}` conditional
- Uses Python's `json` module to read data; passes the list to the `items.html` template via `render_template`
- Dynamically renders an unordered list from JSON data, with graceful handling of empty input

**Files:** `task_02_logic.py`

---

### Task 3 - Displaying Data from JSON or CSV Files in Flask

- Mandatory
- Add a `/products` route that accepts `source` (`json` or `csv`) and optional `id` query parameters; reads product data from the appropriate file and renders it in a table; handles invalid source and missing ID gracefully
- Uses `request.args` to read query parameters; `json` and `csv` modules for data parsing; Jinja template displays errors conditionally
- Supports filtering by ID, displays all products when no ID is given, and shows appropriate error messages for invalid inputs

**Files:** `task_03_files.py`

---

### Task 4 - Extending Dynamic Data Display to Include SQLite

- Mandatory
- Extend the `/products` route to also support `source=sql`, fetching product data from a `products.db` SQLite database; uses the same `product_display.html` template as Task 3
- Uses Python's `sqlite3` module; a `create_database()` helper populates the database; handles DB errors gracefully alongside existing JSON/CSV logic
- A single Flask route serves data from three different sources (JSON, CSV, SQLite) with unified rendering and error handling

**Files:** `task_04_db.py`

---

## 🤝 Contributions & Acknowledgements

Thanks to the Holberton School team for this project. Server-side rendering finally made me appreciate why "the server does the work so the browser doesn't have to" is not just a slogan — it's a design philosophy. Also, Jinja2 templates are genuinely delightful.

---

## 👤 Author

**Gwenaelle PICHOT**
- Student at Holberton School
- Track: holbertonschool-higher_level_programming
- Project: python-server_side_rendering