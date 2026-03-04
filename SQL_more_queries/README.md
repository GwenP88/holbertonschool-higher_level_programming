![SQL - More Queries Banner](assets/banner.jpg)

# SQL - More Queries

## Description
This project continues the exploration of SQL and relational databases by introducing more advanced database concepts and queries using MySQL.

While the previous project focused on basic database manipulation, this one goes deeper into how databases are structured and how relationships between tables are handled. The goal is to understand how to manage users and permissions, enforce data integrity with constraints, and retrieve complex data from multiple related tables.

Throughout the project, we learn how to create MySQL users, manage privileges, define constraints such as `PRIMARY KEY`, `FOREIGN KEY`, `NOT NULL`, and `UNIQUE`, and write more advanced queries using subqueries, joins, and aggregations.

By the end of this project, you should understand how relational databases enforce structure and how SQL can be used to combine and analyze data from multiple tables efficiently.

---

## Learning Objectives
By completing this project, you should be able to explain the following concepts without external help:

- How to create and manage MySQL users
- How to grant and manage privileges on databases and tables
- What a `PRIMARY KEY` is and why it is important
- What a `FOREIGN KEY` is and how it enforces relationships between tables
- How to enforce constraints such as `NOT NULL` and `UNIQUE`
- How to retrieve data from multiple tables in a single query
- What subqueries are and when to use them
- How `JOIN` operations work and how they link related tables
- What `UNION` is and how it combines result sets

The project also strengthens the understanding of relational database design and SQL query optimization through practical exercises.

---

## Requirements
- OS: Ubuntu 20.04 LTS
- MySQL version: 8.0 (8.0.25)
- Allowed editors: `vi`, `vim`, `emacs`
- All files must end with a new line
- All SQL keywords must be written in **uppercase**
- Each SQL file must start with a comment describing the task
- Each SQL query must include a comment explaining what it does
- The project must contain a `README.md` file at the root of the directory
- File lengths will be tested using `wc`

Example of required SQL comment format:

```
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
```

### Usage / Execution
Start the MySQL service before running scripts:

```
service mysql start
```

Execute SQL scripts using:

```
cat script.sql | mysql -hlocalhost -uroot -p database_name
```

Or from inside the MySQL shell:

```
mysql -uroot -p
source script.sql;
```

Default credentials in the Holberton sandbox:

```
user: root
password: root
```

### Importing SQL Dumps
Some tasks require importing prepared databases.

Example:

```
echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
```

Then import the dump:

```
curl "https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
```

---

## Project Progress
<p align="center">
<img src="assets/progress_barre_100.gif" alt="Mandatory tasks progress" width="80%">
</p>

<p align="center">
<sub>Mandatory tasks completion: 100% ---  Advanced tasks completion: 0%</sub>
</p>

---

## Tasks

### 0 - My privileges!
Lists all privileges of the MySQL users `user_0d_1` and `user_0d_2`.

**File**
- `0-privileges.sql`

---

### 1 - Root user
Creates the MySQL user `user_0d_1`.

The user:
- must have **all privileges**
- password must be `user_0d_1_pwd`
- the script must not fail if the user already exists

**File**
- `1-create_user.sql`

---

### 2 - Read user
Creates:
- database `hbtn_0d_2`
- user `user_0d_2`

The user must have **SELECT privilege only** on the database.

**File**
- `2-create_read_user.sql`

---

### 3 - Always a name
Creates the table `force_name`.

**Structure**
- `id INT`
- `name VARCHAR(256) NOT NULL`

**File**
- `3-force_name.sql`

---

### 4 - ID can't be null
Creates the table `id_not_null`.

**Structure**
- `id INT DEFAULT 1`
- `name VARCHAR(256)`

**File**
- `4-never_empty.sql`

---

### 5 - Unique ID
Creates the table `unique_id`.

**Structure**
- `id INT DEFAULT 1 UNIQUE`
- `name VARCHAR(256)`

**File**
- `5-unique_id.sql`

---

### 6 - States table
Creates the database `hbtn_0d_usa` and the table `states`.

**Structure**
- `id INT AUTO_INCREMENT PRIMARY KEY`
- `name VARCHAR(256) NOT NULL`

**File**
- `6-states.sql`

---

### 7 - Cities table
Creates the table `cities`.

**Structure**
- `id INT AUTO_INCREMENT PRIMARY KEY`
- `state_id INT NOT NULL`
- `name VARCHAR(256) NOT NULL`

`state_id` is a **FOREIGN KEY** referencing `states.id`.

**File**
- `7-cities.sql`

---

### 8 - Cities of California
Lists all cities belonging to the state **California**.

**Constraints**
- results must be sorted by `cities.id`
- the `JOIN` keyword is **not allowed**

**File**
- `8-cities_of_california_subquery.sql`

---

### 9 - Cities by States
Lists all cities with their associated state.

**Output format**

cities.id - cities.name - states.name

**File**
- `9-cities_by_state_join.sql`

---

### 10 - Genre ID by show
Lists all TV shows that have at least one genre.

**Output**

tv_shows.title - tv_show_genres.genre_id

**File**
- `10-genre_id_by_show.sql`

---

### 11 - Genre ID for all shows
Lists all shows and their genre IDs.

Shows without genre must display `NULL`.

**File**
- `11-genre_id_all_shows.sql`

---

### 12 - No genre
Lists all shows without any genre linked.

**File**
- `12-no_genre.sql`

---

### 13 - Number of shows by genre
Displays each genre and the number of shows linked to it.

**Columns**

genre  
number_of_shows

**File**
- `13-count_shows_by_genre.sql`

---

### 14 - My genres
Lists all genres linked to the show **Dexter**.

**File**
- `14-my_genres.sql`

---

### 15 - Only Comedy
Lists all shows classified in the **Comedy** genre.

**File**
- `15-comedy_only.sql`

---

### 16 - List shows and genres
Lists all shows with all their genres.

Shows without genre must display `NULL`.

**File**
- `16-shows_by_genre.sql`

---

## Advanced Tasks

### 17 - Not my genre
Lists genres **not linked to the show Dexter**.

**File**
- `100-not_my_genres.sql`

---

### 18 - No Comedy tonight!
Lists all shows that are **not Comedy**.

**File**
- `101-not_a_comedy.sql`

---

### 19 - Rotten tomatoes
Lists shows ordered by their **total rating**.

**Output**

tv_shows.title - rating sum

**File**
- `102-rating_shows.sql`

---

### 20 - Best genre
Lists genres ordered by their **total rating**.

**File**
- `103-rating_genres.sql`

---

### 21 - How Do SQL Database Engines Work?
Write a blog post explaining **how SQL database engines work**.

The post must include:
- introduction
- detailed explanation
- diagrams
- examples
- conclusion

The article must be published on **Medium or LinkedIn**.

---

## Authors
**Gwenaelle PICHOT**
- Student at Holberton School
- Track: Higher Level Programming
- Project: SQL - Introduction