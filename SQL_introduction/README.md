![SQL - Introduction Banner](assets/banner.jpg)

# SQL - Introduction

## Description
This project introduces the fundamentals of SQL and relational databases through a series of progressive tasks executed on a MySQL server.  
The objective is to manipulate databases directly from SQL scripts and understand how data is structured, stored, and queried in relational systems.

Throughout the project, we explore how to create and delete databases, define tables, insert and manipulate records, and retrieve data using different SQL queries. By the end of the project, the database is no longer a mysterious black box but a structured environment where data can be organized, analyzed, and controlled with precise commands.

In short: learning how to politely ask a database for information… and how to make sure it answers exactly what you expect.

---

## Learning Objectives
By completing this project, the goal is to gain a solid understanding of relational databases and SQL. You should be able to explain what a database is, why relational databases are widely used, and how SQL (Structured Query Language) is used to interact with them.

The project also introduces MySQL as a database management system and demonstrates how to create databases, define tables, and manipulate stored data. You will learn the difference between DDL (Data Definition Language) and DML (Data Manipulation Language), and how each is used to structure and modify data.

Finally, the exercises guide you through essential SQL operations such as selecting data, inserting new records, updating existing values, deleting entries, performing aggregations, grouping results, and using built-in SQL functions. By the end of the project, you should feel comfortable navigating and querying a relational database using SQL scripts.

---

## Requirements
- OS: Ubuntu 20.04 LTS / Ubuntu 22.04 LTS  
- MySQL version: 8.0  
- Allowed editors: `vi`, `vim`, `emacs`
- All files must end with a new line
- All SQL keywords must be written in **uppercase**
- Each SQL file must start with a comment describing the task
- Each query must include a comment explaining what it does
- The project must contain a `README.md` file at the root of the directory

---

## Usage / Execution
All SQL scripts can be executed using the MySQL command line interface.

Example execution:

```
cat script.sql | mysql -hlocalhost -uroot -p database_name
```

Or by connecting to MySQL and running the script manually:

```
mysql -uroot -p 
source script.sql;
```

Before running the scripts, ensure the MySQL service is started:

```
service mysql start
```

---

## Project Progress
<p align="center">
<img src="assets/progress_barre_100.gif" alt="Mandatory tasks progress" width="80%">
</p>

<p align="center">
<sub>Mandatory tasks completion: 100% ---  Advanced tasks completion: 25%</sub>
</p>

---

## Tasks

### 0 - List databases
- **Task status:** Mandatory  
- Lists all databases available on the MySQL server.  
- Introduces basic database inspection commands.  
- **Expected behavior:** display all existing databases.

**Files**
- `0-list_databases.sql`

---

### 1 - Create a database
- **Task status:** Mandatory  
- Creates the database `hbtn_0c_0` if it does not already exist.  
- Ensures the script does not fail when the database already exists.

**Files**
- `1-create_database_if_missing.sql`

---

### 2 - Delete a database
- **Task status:** Mandatory  
- Deletes the database `hbtn_0c_0` if it exists.  
- The script must not fail if the database does not exist.

**Files**
- `2-remove_database.sql`

---

### 3 - List tables
- **Task status:** Mandatory  
- Lists all tables of a specified database.

**Files**
- `3-list_tables.sql`

---

### 4 - First table
- **Task status:** Mandatory  
- Creates a table called `first_table` with two fields: `id` and `name`.

**Files**
- `4-first_table.sql`

---

### 5 - Full description
- **Task status:** Mandatory  
- Displays the full structure used to create the table `first_table`.

**Files**
- `5-full_table.sql`

---

### 6 - List all in table
- **Task status:** Mandatory  
- Displays all rows stored in the table `first_table`.

**Files**
- `6-list_values.sql`

---

### 7 - First add
- **Task status:** Mandatory  
- Inserts a new record into `first_table`.

**Files**
- `7-insert_value.sql`

---

### 8 - Count 89
- **Task status:** Mandatory  
- Counts how many records have the value `id = 89`.

**Files**
- `8-count_89.sql`

---

### 9 - Full creation
- **Task status:** Mandatory  
- Creates the table `second_table` and inserts several records.

**Files**
- `9-full_creation.sql`

---

### 10 - List by best
- **Task status:** Mandatory  
- Lists all records ordered by score in descending order.

**Files**
- `10-top_score.sql`

---

### 11 - Select the best
- **Task status:** Mandatory  
- Displays records where the score is greater than or equal to 10.

**Files**
- `11-best_score.sql`

---

### 12 - Cheating is bad
- **Task status:** Mandatory  
- Updates Bob's score to 10 without using his ID.

**Files**
- `12-no_cheating.sql`

---

### 13 - Score too low
- **Task status:** Mandatory  
- Removes records where the score is lower than or equal to 5.

**Files**
- `13-change_class.sql`

---

### 14 - Average
- **Task status:** Mandatory  
- Computes the average score of all records in `second_table`.

**Files**
- `14-average.sql`

---

### 15 - Number by score
- **Task status:** Mandatory  
- Groups records by score and counts how many share the same score.

**Files**
- `15-groups.sql`

---

### 16 - Say my name
- **Task status:** Mandatory  
- Lists records where the `name` column contains a value.

**Files**
- `16-no_link.sql`

---

### 17 - Go to UTF8
- **Task status:** Advanced  
- Converts the database and table encoding to `utf8mb4`.

**Files**
- `100-move_to_utf8.sql`

---

### 18 - Temperatures #0
- **Task status:** Advanced  
- Displays the average temperature by city ordered by temperature.

**Files**
- `101-avg_temperatures.sql`

---

### 19 - Temperatures #1
- **Task status:** Advanced  
- Displays the top 3 cities with the highest average temperatures during July and August.

**Files**
- `102-top_city.sql`

---

### 20 - Temperatures #2
- **Task status:** Advanced  
- Displays the maximum temperature recorded for each state.

**Files**
- `103-max_state.sql`

---

## Authors
**Gwenaelle PICHOT**
- Student at Holberton School
- Track: Higher Level Programming
- Project: SQL - Introduction