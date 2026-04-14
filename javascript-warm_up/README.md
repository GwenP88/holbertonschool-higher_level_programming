# JavaScript - Warm Up

> First contact with JavaScript — variables, loops, functions, and the realization that `var` is best left in the past.

---

## 📝 Description

This project is my introduction to JavaScript programming. I explore the fundamentals of the language: how to declare variables and constants, work with data types, control program flow with conditionals and loops, and write reusable functions. I also get my first taste of JavaScript's module system and object manipulation. It's a hands-on warm-up that sets the foundation for everything that comes next in JavaScript development.

---

## 🎯 Learning Objectives

By the end of this project, I am able to explain why JavaScript is an amazing and versatile programming language that runs everywhere from browsers to servers. I know how to run a JavaScript script using Node.js and understand the differences between `var`, `const`, and `let` — and why `var` is generally avoided in modern JavaScript. I can work with all JavaScript data types, use `if`/`else` statements and comments, assign values to variables, and write `while` and `for` loops with `break` and `continue`. I know how to define and call functions, understand what a function without a `return` statement returns (`undefined`), and grasp the concept of variable scope. I am comfortable using arithmetic operators and manipulating objects (dictionaries), and I understand how to export and import functionality across files using Node.js modules.

---

## 🛠️ Technologies Used

This project uses Node.js (version 14.x) to run JavaScript scripts from the command line. Code style is enforced with semistandard (version 16.x.x), which combines the Standard style guide with mandatory semicolons, following AirBnB conventions.

---

## ⚙️ Requirements

- OS: Ubuntu 20.04 LTS
- Runtime: Node.js (version 14.x)
- All files must end with a new line
- The first line of all files must be exactly: `#!/usr/bin/node`
- A README.md file at the root of the project folder is mandatory
- Code must be semistandard compliant (version 16.x.x)
- All files must be executable
- File length is tested using `wc`
- `var` is not allowed

To install Node 14:
```bash
curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
sudo apt-get install -y nodejs
```

To install semistandard:
```bash
sudo npm install semistandard --global
```

---

## 🚀 Installation

```bash
git clone https://github.com/GwenP88/holbertonschool-higher_level_programming.git
cd holbertonschool-higher_level_programming/javascript-warm_up
```

---

## ▶️ Usage / Execution

All JavaScript scripts can be executed in two ways:

### 1. Direct execution
Make the file executable and run it directly:
```bash
chmod +x filename.js
./filename.js
```

### 2. Using Node.js interpreter
```bash
node filename.js
```

Some scripts accept command-line arguments:
```bash
./2-arguments.js Hello World
./7-multi_c.js 5
./9-add.js 13 89
```

---

## 📊 Project Progress

<p align="center">
<img src="assets/progress_barre_100.gif" alt="Mandatory tasks progress" width="80%">
</p>

<p align="center">
<sub>Mandatory tasks completion: 100% --- Advanced tasks completion: 100%</sub>
</p>

---

## ✨ Features

### Task 0 - First constant, first print

- **Status:** Mandatory
- **Objective:** Write a script that prints "JavaScript is amazing" using a `const` variable.
- **Constraint:** Must use `const` for `myVar`. Must use `console.log()`. `var` is not allowed.
- **Expected behavior:** Running `./0-javascript_is_amazing.js` prints `JavaScript is amazing`.

**Files:** `0-javascript_is_amazing.js`

---

### Task 1 - 3 languages

- **Status:** Mandatory
- **Objective:** Write a script that prints three lines, one for each of C, Python, and JavaScript.
- **Constraint:** Must use `console.log()`. `var` is not allowed.
- **Expected behavior:** Prints `C is fun`, `Python is cool`, and `JavaScript is amazing` on separate lines.

**Files:** `1-multi_languages.js`

---

### Task 2 - Arguments

- **Status:** Mandatory
- **Objective:** Write a script that prints a message depending on the number of arguments passed.
- **Constraint:** Must use `console.log()` and `process.argv`. `var` is not allowed.
- **Expected behavior:** No arguments → `No argument`. One argument → `Argument found`. More → `Arguments found`.

**Files:** `2-arguments.js`

---

### Task 3 - Value of my argument

- **Status:** Mandatory
- **Objective:** Write a script that prints the first argument passed to it, or `"No argument"` if none is provided.
- **Constraint:** `var` and `length` are not allowed.
- **Expected behavior:** `./3-value_argument.js School` prints `School`. No arguments prints `No argument`.

**Files:** `3-value_argument.js`

---

### Task 4 - Create a sentence

- **Status:** Mandatory
- **Objective:** Write a script that prints two arguments in the format `<arg1> is <arg2>`.
- **Constraint:** Must use `console.log()`. `var` is not allowed. Missing arguments display as `undefined`.
- **Expected behavior:** `./4-concat.js c cool` prints `c is cool`. Missing args print `undefined is undefined`.

**Files:** `4-concat.js`

---

### Task 5 - An Integer

- **Status:** Mandatory
- **Objective:** Write a script that prints `My number: <integer>` if the first argument can be cast to an integer, or `"Not a number"` otherwise.
- **Constraint:** `var` and `try/catch` are not allowed.
- **Expected behavior:** `./5-to_integer.js 89.89` prints `My number: 89`. `./5-to_integer.js School` prints `Not a number`.

**Files:** `5-to_integer.js`

---

### Task 6 - Loop to languages

- **Status:** Mandatory
- **Objective:** Print the same three lines as Task 1, but using an array and a loop with only one `console.log`.
- **Constraint:** No `var`, no `if/else`, only one `console.log`, must use a loop.
- **Expected behavior:** Same output as Task 1, achieved with a loop over a string array.

**Files:** `6-multi_languages_loop.js`

---

### Task 7 - I love C

- **Status:** Mandatory
- **Objective:** Write a script that prints `"C is fun"` exactly `x` times, where `x` is the first argument.
- **Constraint:** No `var`. Maximum 2 `console.log` calls. Must use a loop. Invalid input prints `"Missing number of occurrences"`.
- **Expected behavior:** `./7-multi_c.js 3` prints `C is fun` three times. Negative input prints nothing.

**Files:** `7-multi_c.js`

---

### Task 8 - Square

- **Status:** Mandatory
- **Objective:** Write a script that prints a square of `X` characters with the given size.
- **Constraint:** No `var`. Must use a loop. Invalid input prints `"Missing size"`. Negative input prints nothing.
- **Expected behavior:** `./8-square.js 3` prints a 3×3 square of `X` characters.

**Files:** `8-square.js`

---

### Task 9 - Add

- **Status:** Mandatory
- **Objective:** Write a script that prints the sum of two integer arguments using a defined `add(a, b)` function.
- **Constraint:** No `var`. Function prototype must be `function add(a, b)`.
- **Expected behavior:** `./9-add.js 1 7` prints `8`. Missing arguments print `NaN`.

**Files:** `9-add.js`

---

### Task 10 - Factorial

- **Status:** Mandatory
- **Objective:** Write a script that recursively computes and prints the factorial of the first argument.
- **Constraint:** No `var`. Must use a recursive function. Factorial of `NaN` is `1`.
- **Expected behavior:** `./10-factorial.js 3` prints `6`. `./10-factorial.js 333` prints `Infinity`.

**Files:** `10-factorial.js`

---

### Task 11 - Second biggest!

- **Status:** Mandatory
- **Objective:** Write a script that finds and prints the second biggest integer among all arguments passed.
- **Constraint:** No `var`. Fewer than 2 arguments prints `0`.
- **Expected behavior:** `./11-second_biggest.js 4 2 5 3 0 -3` prints `4` (the second largest after 5).

**Files:** `11-second_biggest.js`

---

### Task 12 - Object

- **Status:** Mandatory
- **Objective:** Update a script to replace the value `12` with `89` in an existing object.
- **Constraint:** No `var`. Must modify the object in place between the two `console.log` calls.
- **Expected behavior:** First log shows `{ type: 'object', value: 12 }`, second shows `{ type: 'object', value: 89 }`.

**Files:** `12-object.js`

---

### Task 13 - Add file

- **Status:** Mandatory
- **Objective:** Write a module that exports an `add` function so it can be used by other scripts via `require`.
- **Constraint:** No `var`. The function must be named `add` and must be exported.
- **Expected behavior:** `require('./13-add').add(3, 5)` returns `8`.

**Files:** `13-add.js`

---

### Task 14 - Const or not const

- **Status:** Advanced
- **Objective:** Write a file that modifies the global variable `myVar` to `333` when required.
- **Constraint:** No `var`. This exercise deliberately explores scope and does not need to pass semistandard.
- **Expected behavior:** After requiring `./100-let_me_const`, `console.log(myVar)` prints `333`.

**Files:** `100-let_me_const.js`

---

### Task 15 - Call me Moby

- **Status:** Advanced
- **Objective:** Write a module that exports a function which executes another function `x` times.
- **Constraint:** No `var`. Prototype: `function (x, theFunction)`. Must be exported.
- **Expected behavior:** `callMeMoby(3, fn)` calls `fn` three times.

**Files:** `101-call_me_moby.js`

---

### Task 16 - Add me maybe

- **Status:** Advanced
- **Objective:** Write a module that exports a function that increments a number and passes the result to a callback.
- **Constraint:** No `var`. Prototype: `function (number, theFunction)`. Must be exported.
- **Expected behavior:** `addMeMaybe(4, fn)` calls `fn(5)`, i.e., `fn` receives `number + 1`.

**Files:** `102-add_me_maybe.js`

---

### Task 17 - Increment object

- **Status:** Advanced
- **Objective:** Update a script to add an `incr` method to an existing object that increments its `value` property.
- **Constraint:** No `var`. The method must be added to the object in place.
- **Expected behavior:** Each call to `myObject.incr()` increments `myObject.value` by 1 and the updated object is logged.

**Files:** `103-object_fct.js`

---

## 🤝 Contributions & Acknowledgements

Thanks to the Holberton School team for a JavaScript warm-up that covers everything you need to know before diving into the deep end. And to semistandard, for making sure I always remember my semicolons — even when I really don't want to.

---

## 👤 Author

**Gwenaelle PICHOT**
- Student at Holberton School
- Track: holbertonschool-higher_level_programming
- Project: javascript-warm_up