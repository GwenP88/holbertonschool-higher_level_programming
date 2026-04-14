# RESTful API

> Building, consuming, securing, and documenting APIs — because data doesn't move itself.

---

## 📝 Description

This project is a deep dive into the world of RESTful APIs — the backbone of modern web communication. I explore the full lifecycle of an API: from understanding the HTTP/HTTPS protocol at a conceptual level, to consuming public APIs from the command line, to building my own APIs from scratch using both Python's built-in `http.server` module and the Flask framework. I also tackle the critical topics of API security through authentication mechanisms and learn how to document APIs properly. By the end, I have a complete picture of how data flows between clients and servers in the real world.

---

## 🎯 Learning Objectives

By the end of this project, I am able to explain the foundational differences between HTTP and HTTPS and understand how request/response cycles work, including the structure of HTTP methods and status codes. I know how to consume APIs directly from the command line using `curl`, including setting headers, making POST requests, and interpreting responses. I am able to write Python scripts that fetch data from external APIs using the `requests` library, parse JSON responses, and export structured data to CSV. I can build a basic HTTP server from scratch using Python's `http.server` module and serve different endpoints with JSON responses. I know how to develop a more robust REST API using Flask, including defining routes, handling dynamic parameters, parsing POST request bodies, and returning appropriate HTTP status codes. I understand the importance of API security and am able to implement both Basic HTTP Authentication and JWT token-based authentication with role-based access control using Flask extensions. Finally, I understand the value of API documentation standards like OpenAPI.

---

## 🛠️ Technologies Used

This project uses Python 3 (version 3.9), along with the following libraries and frameworks: `requests` for API consumption, Flask for API development, Flask-HTTPAuth for basic authentication, Flask-JWT-Extended for JWT token-based security, and `werkzeug.security` for password hashing. The built-in Python modules `http.server`, `json`, and `csv` are also used. All testing is done with `curl` or Python scripts.

---

## ⚙️ Requirements

- OS: Ubuntu (scripts tested with Python 3.9)
- Python version: `python3` (3.9)
- Install dependencies:
  ```bash
  pip install requests Flask Flask-HTTPAuth Flask-JWT-Extended
  ```
- All files must end with a new line
- A README.md file at the root of the project is mandatory
- No testing data should be committed (e.g., `users` dictionary must be empty on push)

---

## 🚀 Installation

```bash
git clone https://github.com/GwenP88/holbertonschool-higher_level_programming.git
cd holbertonschool-higher_level_programming/restful-api
pip install requests Flask Flask-HTTPAuth Flask-JWT-Extended
```

---

## ▶️ Usage / Execution

### Running the http.server API (Task 3)
```bash
python3 task_03_http_server.py
```

### Running the Flask API (Tasks 4 & 5)
```bash
flask --app task_04_flask.py run
flask --app task_05_basic_security.py run
```

### Testing with curl
```bash
curl http://localhost:5000/
curl http://localhost:5000/data
curl http://localhost:5000/status
curl http://localhost:5000/users/jane
curl -X POST -H "Content-Type: application/json" \
  -d '{"username": "alice", "name": "Alice", "age": 25, "city": "Paris"}' \
  http://localhost:5000/add_user
```

### Running Python scripts
```bash
python3 main_02_requests.py
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

### Task 0 - Basics of HTTP/HTTPS

- **Status:** Mandatory
- **Objective:** Understand and explain the differences between HTTP and HTTPS, the structure of HTTP requests and responses, and the most common HTTP methods and status codes.
- **Constraint:** Conceptual/research task. Use browser DevTools, MDN documentation, and optional tools like Wireshark.
- **Expected behavior:** Produce a clear summary of HTTP vs HTTPS (encryption), an outline of request/response structure, and annotated lists of at least 4 HTTP methods (GET, POST, PUT, DELETE) and 5 status codes (200, 201, 301, 404, 500).

**Files:** *(conceptual task — no file submission)*

---

### Task 1 - Consume data from an API using command line tools (curl)

- **Status:** Mandatory
- **Objective:** Install and use `curl` to interact with the JSONPlaceholder public API from the command line.
- **Constraint:** Use `curl` flags including `-I` for headers only and `-X POST` with `-d` for POST requests.
- **Expected behavior:** `curl https://jsonplaceholder.typicode.com/posts` returns a JSON array of posts. `curl -I` returns only headers. A POST request simulates creating a new post and returns a response with `id: 101`.

**Files:** *(command-line task — no file submission)*

---

### Task 2 - Consuming and processing data from an API using Python

- **Status:** Mandatory
- **Objective:** Write two Python functions that fetch posts from JSONPlaceholder, print titles, and export data to a CSV file.
- **Constraint:** Use the `requests` library. The `fetch_and_print_posts()` function prints the status code and all post titles. The `fetch_and_save_posts()` function writes `id`, `title`, and `body` columns to `posts.csv` using `csv.DictWriter`.
- **Expected behavior:** Running the script prints `Status Code: 200` followed by all post titles, and generates a `posts.csv` file with 100 rows.

**Files:** `task_02_requests.py`

---

### Task 3 - Develop a simple API using Python with the http.server module

- **Status:** Mandatory
- **Objective:** Build a basic HTTP server from scratch using Python's `http.server` module with multiple endpoints.
- **Constraint:** No third-party libraries. Use `BaseHTTPRequestHandler`. Serve correct `Content-Type` headers. Return 404 for undefined routes.
- **Expected behavior:** `GET /` returns `"Hello, this is a simple API!"`. `GET /data` returns `{"name": "John", "age": 30, "city": "New York"}` as JSON. `GET /status` returns `"OK"`. Any other path returns a 404 with an appropriate message.

**Files:** `task_03_http_server.py`

---

### Task 4 - Develop a Simple API using Python with Flask

- **Status:** Mandatory
- **Objective:** Build a REST API using Flask with in-memory user storage, JSON responses, dynamic routes, and POST request handling with full validation.
- **Constraint:** Users are stored in a dictionary (empty on push). No external database. Validate JSON, check for missing `username`, and handle duplicate entries with appropriate HTTP status codes (400, 404, 409).
- **Expected behavior:** `GET /` returns a welcome message. `GET /data` returns a list of all usernames. `GET /status` returns `"OK"`. `GET /users/<username>` returns the full user object or a 404 error. `POST /add_user` adds a user and returns 201 with confirmation, or the appropriate error code.

**Files:** `task_04_flask.py`

---

### Task 5 - API Security and Authentication Techniques

- **Status:** Mandatory
- **Objective:** Secure Flask API routes using both Basic HTTP Authentication and JWT token-based authentication, with role-based access control for admin-only routes.
- **Constraint:** Use Flask-HTTPAuth for basic auth with hashed passwords via `werkzeug.security`. Use Flask-JWT-Extended for JWT. All authentication errors must consistently return 401. Admin-only access returns 403 for non-admin users. Custom JWT error handlers must be implemented.
- **Expected behavior:** `GET /basic-protected` requires valid Basic Auth credentials and returns `"Basic Auth: Access Granted"`. `POST /login` returns a JWT token for valid credentials. `GET /jwt-protected` requires a valid JWT and returns `"JWT Auth: Access Granted"`. `GET /admin-only` returns `"Admin Access: Granted"` for admin users or `{"error": "Admin access required"}` with 403 for regular users.

**Files:** `task_05_basic_security.py`

---

## 🤝 Contributions & Acknowledgements

Thanks to the Holberton School team for a project that connects all the dots — from raw HTTP to secured, documented APIs. Special appreciation to the creators of Flask for making web development approachable without making it feel like you're assembling IKEA furniture blindfolded. Also, `curl` — the unsung hero of every developer's terminal.

---

## 👤 Author

**Gwenaelle PICHOT**
- Student at Holberton School
- Track: holbertonschool-higher_level_programming
- Project: restful-api