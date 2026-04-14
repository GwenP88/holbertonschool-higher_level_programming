# SQL - More Queries

> More tables, more joins, more power. SQL is not just a query language — it's an art form.

---

## 📝 Description

This project goes beyond the basics of SQL and dives into the more advanced features of MySQL: user management, table constraints, relational design with primary and foreign keys, and multi-table queries using `JOIN`, subqueries, and `UNION`. I also work with a real TV shows database, which makes the exercises surprisingly enjoyable — turns out writing SQL queries about Breaking Bad and Game of Thrones is much more motivating than generic placeholder data.

---

## 🎯 Learning Objectives

By the end of this project, I am able to create new MySQL users and manage their privileges at the database and table level. I understand what primary keys and foreign keys are, and how they enforce referential integrity between related tables. I know how to use `NOT NULL` and `UNIQUE` constraints when defining table schemas. I am able to retrieve data from multiple tables in a single query using `JOIN` (inner, left, right) and `UNION`, and I understand when to use each. I am comfortable writing subqueries to filter or aggregate data based on the results of nested `SELECT` statements. I can also work with grouped data using `GROUP BY`, `HAVING`, and aggregate functions like `COUNT`, `SUM`, and `MAX`.

---

## 🛠️ Technologies Used

This project uses MySQL 8.0 on Ubuntu 20.04 LTS. All scripts are plain SQL files executed via the MySQL command-line client. Some tasks require importing external SQL dumps, fetched using `curl`. No external libraries are required.

---

## ⚙️ Requirements

- OS: Ubuntu 20.04 LTS
- MySQL version: 8.0 (version 8.0.25)
- All files must end with a new line
- All SQL queries must have a comment just before them explaining what they do
- All files must start with a comment describing the task
- All SQL keywords must be in uppercase (`SELECT`, `WHERE`, `JOIN`, etc.)
- A README.md file at the root of the project folder is mandatory
- File length is tested using `wc`

---

## 🚀 Installation

```bash
git clone https://github.com/GwenP88/holbertonschool-higher_level_programming.git
cd holbertonschool-higher_level_programming/SQL_more_queries
```

To start MySQL and connect:
```bash
service mysql start
mysql -uroot -p
```

To import an external SQL dump:
```bash
echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
curl "https://s3.eu-west-3.amazonaws.com/.../hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
```

---

## ▶️ Usage / Execution

All SQL scripts are executed by piping them into the MySQL client:

```bash
cat script_name.sql | mysql -hlocalhost -uroot -p
```

For scripts requiring a specific database:
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

### Task 0 - My privileges!

- **Status:** Mandatory
- **Objective:** Write a script that lists all privileges of MySQL users `user_0d_1` and `user_0d_2` on localhost.
- **Constraint:** Standard `SHOW GRANTS` syntax.
- **Expected behavior:** Displays all grants for both users, or returns an error if a user does not exist.

**Files:** `0-privileges.sql`

---

### Task 1 - Root user

- **Status:** Mandatory
- **Objective:** Write a script that creates the MySQL user `user_0d_1` with all privileges and password `user_0d_1_pwd`.
- **Constraint:** Must not fail if the user already exists.
- **Expected behavior:** The user is created (or silently skipped) and has full privileges on the MySQL server.

**Files:** `1-create_user.sql`

---

### Task 2 - Read user

- **Status:** Mandatory
- **Objective:** Write a script that creates the database `hbtn_0d_2` and the user `user_0d_2` with SELECT-only privileges on that database.
- **Constraint:** Must not fail if the database or user already exists. Password: `user_0d_2_pwd`.
- **Expected behavior:** `user_0d_2` can read but not write to `hbtn_0d_2`.

**Files:** `2-create_read_user.sql`

---

### Task 3 - Always a name

- **Status:** Mandatory
- **Objective:** Write a script that creates the table `force_name` with `id INT` and `name VARCHAR(256) NOT NULL`.
- **Constraint:** Must not fail if the table already exists. Database name is passed as an argument.
- **Expected behavior:** Inserting a row without a `name` value raises an error. Inserting with a name succeeds.

**Files:** `3-force_name.sql`

---

### Task 4 - ID can't be null

- **Status:** Mandatory
- **Objective:** Write a script that creates the table `id_not_null` with `id INT DEFAULT 1` and `name VARCHAR(256)`.
- **Constraint:** Must not fail if the table already exists. Database name is passed as an argument.
- **Expected behavior:** Inserting without an `id` value uses the default of `1` automatically.

**Files:** `4-never_empty.sql`

---

### Task 5 - Unique ID

- **Status:** Mandatory
- **Objective:** Write a script that creates the table `unique_id` with `id INT DEFAULT 1 UNIQUE` and `name VARCHAR(256)`.
- **Constraint:** Must not fail if the table already exists. Database name is passed as an argument.
- **Expected behavior:** Inserting a duplicate `id` raises a duplicate key error and the row is rejected.

**Files:** `5-unique_id.sql`

---

### Task 6 - States table

- **Status:** Mandatory
- **Objective:** Write a script that creates the database `hbtn_0d_usa` and the `states` table with `id INT AUTO_INCREMENT PRIMARY KEY NOT NULL` and `name VARCHAR(256) NOT NULL`.
- **Constraint:** Must not fail if the database or table already exists.
- **Expected behavior:** States can be inserted with auto-incremented IDs.

**Files:** `6-states.sql`

---

### Task 7 - Cities table

- **Status:** Mandatory
- **Objective:** Write a script that creates the `cities` table with a foreign key `state_id` referencing `states.id`.
- **Constraint:** Must not fail if the database or table already exists. `state_id` must be `NOT NULL` and a valid `FOREIGN KEY`.
- **Expected behavior:** Inserting a city with a non-existent `state_id` raises a foreign key constraint error.

**Files:** `7-cities.sql`

---

### Task 8 - Cities of California

- **Status:** Mandatory
- **Objective:** Write a script that lists all cities belonging to California, using a subquery to find California's `id`.
- **Constraint:** `JOIN` keyword is not allowed. Only one `SELECT` is implied. Results sorted by `cities.id` ascending.
- **Expected behavior:** Returns only cities whose `state_id` matches California's `id`.

**Files:** `8-cities_of_california_subquery.sql`

---

### Task 9 - Cities by States

- **Status:** Mandatory
- **Objective:** Write a script that lists all cities alongside their state name using a `JOIN`.
- **Constraint:** Only one `SELECT` statement. Database name is passed as an argument. Results sorted by `cities.id` ascending.
- **Expected behavior:** Each row displays city `id`, city `name`, and the corresponding state `name`.

**Files:** `9-cities_by_state_join.sql`

---

### Task 10 - Genre ID by show

- **Status:** Mandatory
- **Objective:** Write a script that lists all TV shows that have at least one genre linked, with their `genre_id`.
- **Constraint:** Only one `SELECT`. Results sorted by `tv_shows.title` and `tv_show_genres.genre_id` ascending. Requires importing `hbtn_0d_tvshows` dump.
- **Expected behavior:** Shows without genres are excluded. Each genre link appears as a separate row.

**Files:** `10-genre_id_by_show.sql`

---

### Task 11 - Genre ID for all shows

- **Status:** Mandatory
- **Objective:** Write a script that lists all TV shows with their genre IDs, displaying `NULL` for shows without a genre.
- **Constraint:** Only one `SELECT`. Left join required. Results sorted by title and genre ID.
- **Expected behavior:** Shows like "Better Call Saul" and "Homeland" appear with `NULL` in the genre column.

**Files:** `11-genre_id_all_shows.sql`

---

### Task 12 - No genre

- **Status:** Mandatory
- **Objective:** Write a script that lists all TV shows that have no genre linked.
- **Constraint:** Only one `SELECT`. Filter for `NULL` genre IDs. Results sorted by title.
- **Expected behavior:** Only "Better Call Saul" and "Homeland" are returned, both with `NULL` genre IDs.

**Files:** `12-no_genre.sql`

---

### Task 13 - Number of shows by genre

- **Status:** Mandatory
- **Objective:** Write a script that lists all genres and the number of shows linked to each, sorted by count descending.
- **Constraint:** Only one `SELECT`. Columns named `genre` and `number_of_shows`. Genres with no shows are excluded.
- **Expected behavior:** Drama tops the list with 5 shows; Comedy follows with 4.

**Files:** `13-count_shows_by_genre.sql`

---

### Task 14 - My genres

- **Status:** Mandatory
- **Objective:** Write a script that lists all genres of the show "Dexter" using a subquery.
- **Constraint:** Only one `SELECT`. Results sorted alphabetically by genre name.
- **Expected behavior:** Returns Crime, Drama, Mystery, Suspense, and Thriller — Dexter's full portfolio of genre tags.

**Files:** `14-my_genres.sql`

---

### Task 15 - Only Comedy

- **Status:** Mandatory
- **Objective:** Write a script that lists all Comedy shows from `hbtn_0d_tvshows`.
- **Constraint:** Only one `SELECT`. Results sorted by show title.
- **Expected behavior:** Returns New Girl, Silicon Valley, The Big Bang Theory, and The Last Man on Earth.

**Files:** `15-comedy_only.sql`

---

### Task 16 - List shows and genres

- **Status:** Mandatory
- **Objective:** Write a script that lists all shows alongside all their linked genres, with `NULL` for shows without a genre.
- **Constraint:** Only one `SELECT`. Results sorted by show title and genre name.
- **Expected behavior:** Each show-genre combination appears as a separate row. Shows without genres display `NULL`.

**Files:** `16-shows_by_genre.sql`

---

### Task 17 - Not my genre

- **Status:** Advanced - **This task is still in progress — my future self is on it.**
- **Objective:** Write a script that lists all genres NOT linked to the show "Dexter".
- **Constraint:** Maximum two `SELECT` statements. Results sorted alphabetically.
- **Expected behavior:** Returns Adventure, Comedy, and Fantasy — the genres Dexter has not been tagged with.

**Files:** `100-not_my_genres.sql`

---

### Task 18 - No Comedy tonight!

- **Status:** Advanced - **This task is still in progress — my future self is on it.**
- **Objective:** Write a script that lists all shows that do NOT have the Comedy genre.
- **Constraint:** Maximum two `SELECT` statements. Results sorted by show title.
- **Expected behavior:** Returns Better Call Saul, Breaking Bad, Dexter, Game of Thrones, Homeland, and House.

**Files:** `101-not_a_comedy.sql`

---

### Task 19 - Rotten tomatoes

- **Status:** Advanced - **This task is still in progress — my future self is on it.**
- **Objective:** Write a script that lists all shows from `hbtn_0d_tvshows_rate` by their total rating, sorted descending.
- **Constraint:** Only one `SELECT`. Requires importing the `hbtn_0d_tvshows_rate` dump.
- **Expected behavior:** Better Call Saul tops the list with 163 rating points. The Big Bang Theory and New Girl both score 0.

**Files:** `102-rating_shows.sql`

---

### Task 20 - Best genre

- **Status:** Advanced - **This task is still in progress — my future self is on it.**
- **Objective:** Write a script that lists all genres by their total rating sum, sorted descending.
- **Constraint:** Only one `SELECT`. Requires the `hbtn_0d_tvshows_rate` dump.
- **Expected behavior:** Drama leads with 150, followed by Comedy at 92. Thriller closes the list at 40.

**Files:** `103-rating_genres.sql`

---

### Task 21 - How Do SQL Database Engines Work?

- **Status:** Advanced - **This task is still in progress — my future self is on it.**
- **Objective:** Write a blog post explaining how SQL database engines work, in plain language with diagrams, code examples, and a conclusion.
- **Constraint:** Must be published on Medium or LinkedIn and shared publicly. Written in English.
- **Expected behavior:** A complete blog post with introduction, detailed explanation, original examples, at least one diagram, and a summary conclusion.

**Files:** *(blog post — external link)*

---

## 🔮 What’s Next

I plan to continue working on this project by completing the advanced tasks that are not done yet. This will allow me to deepen my understanding, improve my skills, and push a bit further beyond the basics (because stopping halfway is not really my style).

---

## 🤝 Contributions & Acknowledgements

Thanks to the Holberton School team for a SQL project that actually tells a story — TV shows, ratings, and genres make for far more engaging queries than abstract placeholder data. Also, sincere gratitude to `JOIN` for making multi-table queries feel powerful once you finally understand which way the relationship goes.

---

## 👤 Author

**Gwenaelle PICHOT**
- Student at Holberton School
- Track: holbertonschool-higher_level_programming
- Project: SQL_more_queries