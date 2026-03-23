![JavaScript DOM Manipulation Banner](assets/banner.png)

# JavaScript DOM Manipulation

## Description
This project focuses on manipulating the DOM (Document Object Model) using JavaScript.  
It covers selecting HTML elements, modifying content and styles, handling events, and making network requests using Fetch API.

The goal is to understand how JavaScript interacts dynamically with web pages without reloading them.

---

## Learning Objectives
At the end of this project, you should be able to:

- Select HTML elements using JavaScript
- Understand the differences between ID, class, and tag selectors
- Modify HTML element styles dynamically
- Update HTML content
- Manipulate the DOM structure
- Handle user events (click, input, etc.)
- Make HTTP requests using:
  - XMLHttpRequest
  - Fetch API
- Work with asynchronous JavaScript (Promises basics)

---

## Requirements
- Allowed editors: All
- All files interpreted on Chrome (version 57.0 or later)
- All files must end with a new line
- A README.md file at the root of the project is mandatory
- Code must be semistandard compliant
- Use of `let` and `const` only (no `var`)
- No page reload allowed (all updates must be done via DOM manipulation)

---

## Usage / Execution
All JavaScript scripts are executed in the browser.

### 1. Open HTML file
Simply open the provided HTML file in your browser:
```
xdg-open file.html
```

### 2. UUsing Live Server (recommended)
Run a local server (VS Code Live Server for example) for better behavior with Fetch requests.

---

## Project Progress
<p align="center">
<img src="assets/progress_barre_100.gif" alt="Mandatory tasks progress" width="80%">
</p>

<p align="center">
<sub>Mandatory tasks completion: 100% ---  Advanced tasks completion: 100%</sub>
</p>

---

## Tasks

### 0 - Color Me
- Status: Mandatory
- Update header text color to red
- Use `document.querySelector`
- Modify CSS style via JavaScript

**Files**
- 0-script.js

---

### 1 - Click and turn red
- Status: Mandatory
- Change header color on click
- Use event listener on element with id `red_header`

**Files**
- 1-script.js

---

### 2 - Add `.red` class
- Status: Mandatory
- Add CSS class to header on click
- Use `classList`

**Files**
- 2-script.js

---

### 3 - Toggle classes
- Status: Mandatory
- Switch between `red` and `green`
- Ensure only one class is present

**Files**
- 3-script.js

---

### 4 - List of elements
- Status: Mandatory
- Add `<li>` element dynamically
- Append element to list `.my_list`

**Files**
- 4-script.js

---

### 5 - Change the text
- Status: Mandatory
- Update header text content
- Triggered by click event

**Files**
- 5-script.js

---

### 6 - Star Wars character
- Status: Mandatory
- Fetch character data from API
- Display name in DOM
- Use Fetch API

**Files**
- 6-script.js

---

### 7 - Star Wars movies
- Status: Mandatory
- Fetch movies list from API
- Display titles in `<ul>`

**Files**
- 7-script.js

---

### 8 - Say Hello!
- Status: Mandatory
- Fetch translation from API
- Display result in DOM
- Script works in `<head>`

**Files**
- 8-script.js

---

### 9 - List, add, remove
- Status: Advanced
- Add, remove and clear list items
- Handle multiple user actions
- Works from `<head>`

**Files**
- 100-script.js

---

### 10 - Say hello to everybody!
- Status: Advanced
- Fetch translation based on selected language
- Trigger request on button click
- Update DOM dynamically

---

## Authors
**Gwenaelle PICHOT**
- Student at Holberton School
- Track: Higher Level Programming
- Project: JavaScript DOM Manipulation