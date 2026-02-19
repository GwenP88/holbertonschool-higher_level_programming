![RESTful API Banner](assets/banner.png)

# RESTful API

## Description
In a world where applications talk to each other more than humans do, RESTful APIs are the translators, diplomats, and sometimes the bouncers of the digital ecosystem.

In this project, we explore how systems communicate over HTTP and HTTPS using REST principles. From understanding how a simple request travels across the web to building and securing our own API, this journey covers the essential foundations of modern backend development.

We begin with the basics of HTTP structure, then move on to consuming public APIs from the command line and Python. Next, we build our own APIs using both Python’s built-in `http.server` module and the Flask framework. Finally, we secure our endpoints with authentication mechanisms, including Basic Authentication and JWT with role-based access control.

By the end of this project, we don’t just “use” APIs — we understand how they think.

---

## Learning Objectives
With this project, I learned how HTTP and HTTPS work, including how requests and responses are structured, how methods function, and how status codes reflect what happens on the server side. I practiced interacting with APIs directly from the command line using tools like `curl`, which helped me better understand what really happens behind a simple web request.

I learned how to fetch, parse, and manipulate JSON data using Python, and how to transform structured API data into other formats such as CSV files. I built a basic API using Python’s built-in `http.server` module, which allowed me to understand the mechanics of handling requests and sending responses without relying on external frameworks.

I then developed a more structured REST API using Flask, where I implemented multiple routes, handled dynamic endpoints, and processed POST requests. I implemented authentication mechanisms, including Basic Authentication and JWT (JSON Web Token), to secure access to protected routes. I also protected endpoints using decorators and implemented role-based access control to differentiate between regular users and administrators.

Finally, I learned how to handle authentication errors consistently and correctly, ensuring proper HTTP status codes are returned. Through this project, I gained a deeper appreciation for clean API design, structured logic, and clear documentation.

From request to response, from an open endpoint to a secured system, I built and understood the full flow of a RESTful API.

---

## Requirements
- OS: Ubuntu 20.04 LTS
- Python version: `python3` (3.8.5)
- All files must end with a new line
- The first line of all files must be exactly: `#!/usr/bin/python3`
- A README.md file at the root of the project is mandatory
- Code must follow pycodestyle (version 2.7.*)
- All files must be executable
- No module imports allowed unless explicitly stated

---

## Usage / Execution
All Python scripts can be executed in two ways:

### 1. Direct execution
Make the file executable and run it directly:
```bash
chmod +x filename.py
./filename.py
```

### 2. Using Python interpreter
Run the script with Python:
```bash
python3 filename.py
```

---

## Project Progress
<p align="center">
<img src="assets/progress_barre_100.gif" alt="Mandatory tasks progress" width="80%">
</p>

<p align="center">
<sub>Mandatory tasks completion: 100%%</sub>
</p>

---

## Tasks

### 2 - Consuming and Processing Data from an API using Python

**Task status:** Mandatory  
**Task objectives:**  
Use the `requests` library to fetch API data, parse JSON responses, display selected information, and export structured data into a CSV file.
**Task constraints:**  
Must use the `requests` library and Python’s built-in `csv` module.
**Expected behavior:**  
Display the HTTP response status code.  
Print all post titles retrieved from the API.  
Create a CSV file named `posts.csv` containing the fields `id`, `title`, and `body`.  
Properly handle successful responses before processing data.
**Files:**  
`task_02_requests.py`

---

### 3 - Develop a Simple API using Python with the `http.server` Module

**Task status:** Mandatory  
**Task objectives:**  
Build a minimal API using only Python’s standard library.
**Task constraints:**  
No external frameworks allowed.
**Expected behavior:**  
The root endpoint (`/`) returns a simple text message.  
The `/data` endpoint returns JSON data.  
The `/status` endpoint returns `OK`.  
Undefined routes return a `404 Not Found` response.  
Proper HTTP headers are set for JSON responses.
**Files:**  
`task_03_http_server.py`

---

### 4 - Develop a Simple API using Python with Flask

**Task status:** Mandatory  
**Task objectives:**  
Build a structured RESTful API using Flask, including dynamic routes and POST request handling.
**Task constraints:**  
Data must be stored in memory using a dictionary. No database allowed.
**Expected behavior:**  
The root route returns a welcome message.  
The `/data` route returns a list of usernames.  
The `/users/<username>` route returns the full user object or a `404` error if the user does not exist.  
The `/add_user` route accepts a POST request with JSON data and:  
Adds the user if the data is valid.  
Returns `400` for invalid JSON.  
Returns `400` if the username is missing.  
Returns `409` if the username already exists.  
Proper HTTP status codes are used for every response.
**Files:**  
`task_04_flask.py`

---

### 5 - Implement Basic and JWT Authentication with Role-Based Access

**Task status:** Mandatory  
**Task objectives:**  
Secure the Flask API using Basic Authentication and JWT, including role-based access control.
**Task constraints:**  
Passwords must be securely hashed.  
JWT must use a secret key for token generation and validation.  
All authentication errors must return HTTP `401 Unauthorized`.
**Expected behavior:**  
The `/basic-protected` route requires valid basic authentication credentials.  
The `/login` route returns a JWT token when valid credentials are provided.  
The `/jwt-protected` route requires a valid JWT token.  
The `/admin-only` route requires an admin role.  
Invalid or missing tokens return `401 Unauthorized`.  
Non-admin access to the admin route returns `403 Forbidden`.
**Files:**  
`task_05_basic_security.py`

---

## Authors
**Gwenaelle PICHOT**
- Student at Holberton School
- Track: Higher Level Programming
- Project: RESTful API