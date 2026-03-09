![Python - Object-relational mapping Banner](assets/banner.png)

# Python - Object-relational mapping

## Description
This project introduces the connection between **Python** and **MySQL databases**.

It is divided into two main parts:

- using **MySQLdb** to connect Python scripts to a MySQL server and execute SQL queries,
- using **SQLAlchemy** to work with an **Object Relational Mapper (ORM)** and manipulate database data through Python objects instead of raw SQL queries.

The goal is to understand how to:
- connect a Python script to a MySQL database,
- retrieve and insert data with SQL,
- protect queries from SQL injection,
- map Python classes to database tables,
- query and update data through SQLAlchemy models.

This project is part of the **Higher Level Programming** track at **Holberton School**.

---

## Learning Objectives
At the end of this project, you should be able to explain:

- how to connect to a MySQL database from a Python script,
- how to `SELECT` rows in a MySQL table from Python,
- how to `INSERT` rows in a MySQL table from Python,
- what an **ORM** is,
- how to map a Python class to a MySQL table,
- the difference between raw SQL queries and ORM-based object manipulation,
- why parameterized queries are important to prevent **SQL injection**,
- how to use **SQLAlchemy** to create, query, update, and delete database objects.

---

## Requirements
- OS: Ubuntu 20.04 LTS
- Python version: `python3` (3.8.5)
- MySQL version: `8.0`
- MySQLdb version: `2.0.x`
- SQLAlchemy version: `1.4.x`
- Allowed editors: `vi`, `vim`, `emacs`
- All files must end with a new line
- The first line of all files must be exactly: `#!/usr/bin/python3`
- A `README.md` file at the root of the project is mandatory
- Code must follow `pycodestyle` (version `2.7.*`)
- All files must be executable
- File length will be checked using `wc`
- All modules must have proper documentation
- All classes must have proper documentation
- All functions must have proper documentation
- Documentation must be a real explanatory sentence
- You are **not allowed** to use `execute` with SQLAlchemy unless explicitly required
- No code should be executed when a file is imported

---

## Installation

### MySQL 8.0

```
sudo apt update
sudo apt install mysql-server
mysql --version
```

---

### MySQLdb

```
sudo apt-get install python3-dev
sudo apt-get install libmysqlclient-dev
sudo apt-get install zlib1g-dev
sudo pip3 install mysqlclient==2.0.3
```

---


### SQLAlchemy

```
sudo pip3 install SQLAlchemy==1.4.22
```

---

## Usage / Execution
All Python scripts can be executed in two ways:

### Direct execution
Make the file executable and run it directly:

```
chmod +x filename.py
./filename.py
```

---

### Using Python interpreter
Run the script with Python:

```
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

## Tasks

### 0 - Get all states
- **Status:** Mandatory
- **Objective:** List all states from the database `hbtn_0e_0_usa`
- **Constraints:** Use `MySQLdb`, connect to localhost on port `3306`, sort results by `states.id`
- **Expected behavior:** Display all rows from the `states` table exactly as stored

**Files:**
- `0-select_states.py`

---

### 1 - Filter states
- **Status:** Mandatory
- **Objective:** List all states starting with the letter `N`
- **Constraints:** Use `MySQLdb`, sort by `states.id`
- **Expected behavior:** Display only states whose names begin with uppercase `N`

**Files:**
- `1-filter_states.py`

---

### 2 - Filter states by user input
- **Status:** Mandatory
- **Objective:** Display states matching the user-provided name
- **Constraints:** Use `MySQLdb` and build the query with `format`
- **Expected behavior:** Return matching rows, but this version is vulnerable to SQL injection

**Files:**
- `2-my_filter_states.py`

---

### 3 - SQL Injection safe filter
- **Status:** Mandatory
- **Objective:** Securely display states matching user input
- **Constraints:** Must be safe from MySQL injection
- **Expected behavior:** Return exact matching states without allowing injected SQL commands

**Files:**
- `3-my_safe_filter_states.py`

---

### 4 - Cities by states
- **Status:** Mandatory
- **Objective:** List all cities with their corresponding state name
- **Constraints:** Use `MySQLdb`, only one `execute()`, sort by `cities.id`
- **Expected behavior:** Display each city with its city id and associated state

**Files:**
- `4-cities_by_state.py`

---

### 5 - All cities by state
- **Status:** Mandatory
- **Objective:** List all cities belonging to a given state
- **Constraints:** SQL injection free, only one `execute()`
- **Expected behavior:** Print city names separated by commas in ascending order by `cities.id`

**Files:**
- `5-filter_cities.py`

---

### 6 - First state model
- **Status:** Mandatory
- **Objective:** Create the `State` class mapped to the `states` table
- **Constraints:** Use `SQLAlchemy` and `declarative_base()`
- **Expected behavior:** Define a model with `id` and `name` columns and create the table through metadata

**Files:**
- `model_state.py`

---

### 7 - All states via SQLAlchemy
- **Status:** Mandatory
- **Objective:** List all `State` objects from the database
- **Constraints:** Import `Base` and `State` from `model_state`
- **Expected behavior:** Display all states ordered by id in the format `<id>: <name>`

**Files:**
- `7-model_state_fetch_all.py`

---

### 8 - First state
- **Status:** Mandatory
- **Objective:** Print the first `State` object from the database
- **Constraints:** Do not fetch all states before displaying the first one
- **Expected behavior:** Print the first state by id, or `Nothing` if the table is empty

**Files:**
- `8-model_state_fetch_first.py`

---

### 9 - Contains a
- **Status:** Mandatory
- **Objective:** List all states containing the letter `a`
- **Constraints:** Use SQLAlchemy query filtering
- **Expected behavior:** Print all matching states ordered by id

**Files:**
- `9-model_state_filter_a.py`

---

### 10 - Get a state
- **Status:** Mandatory
- **Objective:** Print the id of the state matching the provided name
- **Constraints:** SQL injection free
- **Expected behavior:** Display the state id if found, otherwise print `Not found`

**Files:**
- `10-model_state_my_get.py`

---

### 11 - Add a new state
- **Status:** Mandatory
- **Objective:** Insert a new `State` object named `Louisiana`
- **Constraints:** Use SQLAlchemy session
- **Expected behavior:** Add the record and print the newly created state's id

**Files:**
- `11-model_state_insert.py`

---

### 12 - Update a state
- **Status:** Mandatory
- **Objective:** Update the name of the state with `id = 2`
- **Constraints:** Change its name to `New Mexico`
- **Expected behavior:** Persist the modification in the database

**Files:**
- `12-model_state_update_id_2.py`

---

### 13 - Delete states
- **Status:** Mandatory
- **Objective:** Delete all states containing the letter `a`
- **Constraints:** Use SQLAlchemy
- **Expected behavior:** Remove all matching rows from the database

**Files:**
- `13-model_state_delete_a.py`

---

### 14 - Cities in state
- **Status:** Mandatory
- **Objective:** Create the `City` model and print all cities grouped by state
- **Constraints:** `City` must inherit from `Base`, include `state_id` as a foreign key to `states.id`
- **Expected behavior:** Display results in the format `<state name>: (<city id>) <city name>`

**Files:**
- `model_city.py`
- `14-model_city_fetch_by_state.py`

---

## Key Concepts Covered

- Python and MySQL connection with MySQLdb
- SQL queries from Python
- Secure parameter handling
- SQL injection prevention
- Database relationships
- ORM fundamentals
- SQLAlchemy model
- Session management
- Querying, inserting, updating, and deleting records with SQLAlchemy

---

## Example Databases Used

This project relies on several practice databases:

- hbtn_0e_0_usa
- hbtn_0e_4_usa
- hbtn_0e_6_usa
- hbtn_0e_14_usa

These databases include tables such as:

- states
- cities

---

## Notes

- Make sure your MySQL server is running before executing the scripts.
- Some scripts expect pre-existing databases and tables populated with test data.
- SQLAlchemy warnings related to deprecated MySQL session variables can be ignored for this project.
- All scripts are designed to respect Holberton project constraints.

---

## Authors
**Gwenaelle PICHOT**
- Student at Holberton School
- Track: Higher Level Programming
- Project: Python - Object-relational mapping