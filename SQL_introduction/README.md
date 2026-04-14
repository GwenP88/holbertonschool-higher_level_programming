# SQL - Introduction

> Teaching a database to remember things, so I don't have to.

---

## 📝 Description

This project is my introduction to the world of relational databases and SQL (Structured Query Language). I learn how to interact with a MySQL server to create and manage databases, define and modify table structures, and manipulate data using the core SQL operations. From listing databases to writing complex queries with functions and subqueries, this project builds a solid foundation for working with data in a structured and reliable way.

---

## 🎯 Learning Objectives

By the end of this project, I am able to explain what a database is and what makes a relational database different from other storage systems. I know what SQL stands for and understand the role MySQL plays as a database management system. I can create databases and tables in MySQL and understand the distinction between DDL (Data Definition Language) operations like `CREATE` and `ALTER`, and DML (Data Manipulation Language) operations like `INSERT`, `UPDATE`, and `DELETE`. I am able to query data from tables using `SELECT` with filtering, ordering, and grouping, and I understand how to use MySQL built-in functions such as `COUNT`, `AVG`, and `MAX`. I also understand what subqueries are and how to use them to write more expressive SQL statements.

---

## 🛠️ Technologies Used

This project uses MySQL 8.0 on Ubuntu 22.04 LTS. All scripts are plain SQL files executed via the MySQL command-line client. No external tools or libraries are required beyond a running MySQL server instance.

---

## ⚙️ Requirements

- OS: Ubuntu 22.04 LTS
- MySQL version: 8.0 (version 8.0.25+)
- All files must end with a new line
- All SQL queries must have a comment just before them explaining what they do
- All files must start with a comment describing the task
- All SQL keywords must be in uppercase (`SELECT`, `WHERE`, `CREATE`, etc.)
- A README.md file at the root of the project folder is mandatory
- File length is tested using `wc`

---

## 🚀 Installation

```bash
git clone https://github.com/GwenP88/holbertonschool-higher_level_programming.git
cd holbertonschool-higher_level_programming/SQL_introduction
```

To install MySQL 8.0 on Ubuntu:
```bash
sudo apt update
sudo apt install mysql-server
mysql --version
```

To start the MySQL service and connect:
```bash
service mysql start
mysql -uroot
```

---

## ▶️ Usage / Execution

All SQL scripts are executed by piping them into the MySQL client:

```bash
cat script_name.sql | mysql -hlocalhost -uroot -p
```

For scripts that require a database argument:
```bash
cat script_name.sql | mysql -hlocalhost -uroot -p database_name
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

### Task 0 - List databases

- **Status:** Mandatory
- **Objective:** Write a script that lists all databases on the MySQL server.
- **Constraint:** Standard SQL only.
- **Expected behavior:** Outputs all existing databases, including `information_schema`, `mysql`, `performance_schema`, and `sys`.

**Files:** `0-list_databases.sql`

---

### Task 1 - Create a database

- **Status:** Mandatory
- **Objective:** Write a script that creates the database `hbtn_0c_0` if it does not already exist.
- **Constraint:** Must not fail if the database already exists. `SELECT` and `SHOW` statements are not allowed.
- **Expected behavior:** The database is created silently, with no error if it already exists.

**Files:** `1-create_database_if_missing.sql`

---

### Task 2 - Delete a database

- **Status:** Mandatory
- **Objective:** Write a script that deletes the database `hbtn_0c_0` if it exists.
- **Constraint:** Must not fail if the database does not exist. `SELECT` and `SHOW` statements are not allowed.
- **Expected behavior:** The database is dropped silently, with no error if it does not exist.

**Files:** `2-remove_database.sql`

---

### Task 3 - List tables

- **Status:** Mandatory
- **Objective:** Write a script that lists all tables in a given database.
- **Constraint:** The database name is passed as an argument to the `mysql` command.
- **Expected behavior:** All table names in the specified database are listed.

**Files:** `3-list_tables.sql`

---

### Task 4 - First table

- **Status:** Mandatory
- **Objective:** Write a script that creates a table called `first_table` with columns `id INT` and `name VARCHAR(256)`.
- **Constraint:** Must not fail if the table already exists. `SELECT` and `SHOW` statements are not allowed. Database name is passed as an argument.
- **Expected behavior:** The table is created in the current database without error.

**Files:** `4-first_table.sql`

---

### Task 5 - Full description

- **Status:** Mandatory
- **Objective:** Write a script that prints the full creation statement for `first_table`.
- **Constraint:** `DESCRIBE` and `EXPLAIN` statements are not allowed. Database name is passed as an argument.
- **Expected behavior:** Displays the `CREATE TABLE` statement for `first_table`, including column definitions, engine, and charset.

**Files:** `5-full_table.sql`

---

### Task 6 - List all in table

- **Status:** Mandatory
- **Objective:** Write a script that lists all rows and all fields from `first_table`.
- **Constraint:** Database name is passed as an argument.
- **Expected behavior:** All rows in `first_table` are displayed. If the table is empty, nothing is returned.

**Files:** `6-list_values.sql`

---

### Task 7 - First add

- **Status:** Mandatory
- **Objective:** Write a script that inserts a new row into `first_table` with `id = 89` and `name = 'Best School'`.
- **Constraint:** Database name is passed as an argument.
- **Expected behavior:** The row is inserted. Running the script multiple times inserts multiple identical rows.

**Files:** `7-insert_value.sql`

---

### Task 8 - Count 89

- **Status:** Mandatory
- **Objective:** Write a script that displays the number of records with `id = 89` in `first_table`.
- **Constraint:** Database name is passed as an argument.
- **Expected behavior:** Returns the count of matching rows as a single number.

**Files:** `8-count_89.sql`

---

### Task 9 - Full creation

- **Status:** Mandatory
- **Objective:** Write a script that creates `second_table` with columns `id INT`, `name VARCHAR(256)`, and `score INT`, and inserts four specific records.
- **Constraint:** Must not fail if the table already exists. `SELECT` and `SHOW` are not allowed. Database name is passed as an argument.
- **Expected behavior:** The table is created and populated with John (10), Alex (3), Bob (14), and George (8).

**Files:** `9-full_creation.sql`

---

### Task 10 - List by best

- **Status:** Mandatory
- **Objective:** Write a script that lists all records from `second_table`, ordered by score descending, displaying score and name.
- **Constraint:** Database name is passed as an argument.
- **Expected behavior:** Output shows records from highest to lowest score: Bob (14), John (10), George (8), Alex (3).

**Files:** `10-top_score.sql`

---

### Task 11 - Select the best

- **Status:** Mandatory
- **Objective:** Write a script that lists all records with `score >= 10` from `second_table`, ordered by score descending.
- **Constraint:** Database name is passed as an argument.
- **Expected behavior:** Only Bob (14) and John (10) are displayed.

**Files:** `11-best_score.sql`

---

### Task 12 - Cheating is bad

- **Status:** Mandatory
- **Objective:** Write a script that updates Bob's score to `10` using only the `name` field (not the `id`).
- **Constraint:** Cannot use Bob's `id` value. Database name is passed as an argument.
- **Expected behavior:** Bob's score changes from 14 to 10. John and Bob are now tied at 10.

**Files:** `12-no_cheating.sql`

---

### Task 13 - Score too low

- **Status:** Mandatory
- **Objective:** Write a script that removes all records with `score <= 5` from `second_table`.
- **Constraint:** Database name is passed as an argument.
- **Expected behavior:** Alex (score 3) is removed. John, Bob, and George remain.

**Files:** `13-change_class.sql`

---

### Task 14 - Average

- **Status:** Mandatory
- **Objective:** Write a script that computes the average score of all records in `second_table`, with the result column labeled `average`.
- **Constraint:** Database name is passed as an argument.
- **Expected behavior:** Returns the average score as a decimal value (e.g., `9.3333`).

**Files:** `14-average.sql`

---

### Task 15 - Number by score

- **Status:** Mandatory
- **Objective:** Write a script that lists each distinct score and the number of records with that score from `second_table`, sorted by count descending.
- **Constraint:** Result columns must be named `score` and `number`. Database name is passed as an argument.
- **Expected behavior:** Displays each score alongside how many records share it, most frequent first.

**Files:** `15-groups.sql`

---

### Task 16 - Say my name

- **Status:** Mandatory
- **Objective:** Write a script that lists all records from `second_table` where the `name` column is not empty, displaying score and name ordered by score descending.
- **Constraint:** Rows with no name value must be excluded. Database name is passed as an argument.
- **Expected behavior:** Only records with a non-empty `name` are listed, sorted by descending score.

**Files:** `16-no_link.sql`

---

### Task 17 - Go to UTF8

- **Status:** Advanced - **This task is still in progress — my future self is on it.**
- **Objective:** Write a script that converts the `hbtn_0c_0` database, `first_table` table, and its `name` field to `utf8mb4` with `utf8mb4_unicode_ci` collation.
- **Constraint:** Must convert the database, the table, and the specific field.
- **Expected behavior:** The `SHOW CREATE TABLE first_table` output reflects the `utf8mb4_unicode_ci` charset and collation.

**Files:** `100-move_to_utf8.sql`

---

### Task 18 - Temperatures #0

- **Status:** Advanced - **This task is still in progress — my future self is on it.**
- **Objective:** Write a script that displays the average temperature (Fahrenheit) per city from an imported temperature dump, ordered by temperature descending.
- **Constraint:** Requires importing the provided SQL dump. Database name is passed as an argument.
- **Expected behavior:** Lists all cities with their average temperature, from hottest to coolest.

**Files:** `101-avg_temperatures.sql`

---

### Task 19 - Temperatures #1

- **Status:** Advanced - **This task is still in progress — my future self is on it.**
- **Objective:** Write a script that displays the top 3 cities by average temperature during July and August, ordered descending.
- **Constraint:** Filter by month (July = 7, August = 8). Database name is passed as an argument.
- **Expected behavior:** Returns Naperville, San Diego, and Sunnyvale as the top 3 summer cities.

**Files:** `102-top_city.sql`

---

### Task 20 - Temperatures #2

- **Status:** Advanced - **This task is still in progress — my future self is on it.**
- **Objective:** Write a script that displays the maximum temperature per state, ordered by state name.
- **Constraint:** Database name is passed as an argument.
- **Expected behavior:** Each state is listed once with its maximum recorded temperature. AZ, CA, and IL all top at 110°F.

**Files:** `103-max_state.sql`

---

## 🔮 What’s Next

I plan to continue working on this project by completing the advanced tasks that are not done yet. This will allow me to deepen my understanding, improve my skills, and push a bit further beyond the basics (because stopping halfway is not really my style).

---

## 🤝 Contributions & Acknowledgements

Thanks to the Holberton School team for a project that makes SQL feel less like a foreign language and more like a superpower. Special acknowledgement to MySQL for being simultaneously frustrating and deeply satisfying — there is real joy in watching a clean `SELECT` return exactly what you asked for.

---

## 👤 Author

**Gwenaelle PICHOT**
- Student at Holberton School
- Track: holbertonschool-higher_level_programming
- Project: SQL_introduction