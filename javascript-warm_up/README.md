# JavaScript - Warm up

## Description

This project is an introduction to JavaScript programming using Node.js.
It focuses on scripting concepts and fundamental language features such as variables, loops, functions, and objects.

The goal is to build a solid foundation before moving to more advanced topics like web front-end development and dynamic applications.

---

## Learning Objectives

At the end of this project, you should be able to explain:

- Why JavaScript programming is amazing
- How to run a JavaScript script using Node.js
- How to create variables and constants (`const`, `let`)
- The differences between `var`, `let`, and `const`
- All available data types in JavaScript
- How to use conditionals (`if`, `if...else`)
- How to write comments
- How to assign values to variables
- How to use loops (`while`, `for`)
- How to use `break` and `continue`
- What a function is and how to use it
- What a function returns without a return statement
- Scope of variables
- Arithmetic operators
- How to manipulate objects and arrays
- How to import a file (`require`)

---

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- OS: Ubuntu 20.04 LTS
- Node version: `14.x`
- All files must end with a new line
- The first line of all files must be exactly: `#!/usr/bin/node`
- A `README.md` file at the root is mandatory
- Code must be **semistandard compliant** (version 16.x.x)
- All files must be executable
- File length will be tested using `wc`

---

## Project Progress
<p align="center">
<img src="assets/progress_barre_100.gif" alt="Mandatory tasks progress" width="80%">
</p>

<p align="center">
<sub>Mandatory tasks completion: 100% ---  Advanced tasks completion: 100%</sub>
</p>

---

## Setup

### Install Node.js

```bash
curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
sudo apt-get install -y nodejs
```

### Install semistandard

```bash
sudo npm install semistandard --global
```

---

## Usage

### Direct execution

```bash
chmod +x filename.js
./filename.js
```

### Using Node.js

```bash
node filename.js
```

---

## Tasks

### Mandatory

| # | Description | File |
|---|---|---|
| 0 | Create a constant `myVar` with value `"JavaScript is amazing"` and print it | `0-javascript_is_amazing.js` |
| 1 | Print 3 predefined strings | `1-multi_languages.js` |
| 2 | Print message depending on number of arguments | `2-arguments.js` |
| 3 | Print the first argument | `3-value_argument.js` |
| 4 | Print two arguments in a formatted sentence | `4-concat.js` |
| 5 | Convert argument to integer and print result | `5-to_integer.js` |
| 6 | Print strings using array + loop | `6-multi_languages_loop.js` |
| 7 | Print "C is fun" x times | `7-multi_c.js` |
| 8 | Print a square using `X` | `8-square.js` |
| 9 | Create function `add(a, b)` | `9-add.js` |
| 10 | Compute factorial recursively | `10-factorial.js` |
| 11 | Find the second largest number | `11-second_biggest.js` |
| 12 | Modify an object value | `12-object.js` |
| 13 | Export function `add` | `13-add.js` |

### Advanced

| # | Description | File |
|---|---|---|
| 14 | Modify a global variable using scope | `100-let_me_const.js` |
| 15 | Execute a function x times | `101-call_me_moby.js` |
| 16 | Increment value and call function | `102-add_me_maybe.js` |
| 17 | Add method `incr` to an object | `103-object_fct.js` |

---

## Authors
**Gwenaelle PICHOT**
- Student at Holberton School
- Track: Higher Level Programming 
- Project: JavaScript - Warm up