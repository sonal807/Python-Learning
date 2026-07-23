# 📘 Chapter 01 - Modules, Comments & pip

## 🎯 Objective
This chapter introduces the basics of Python programming, how to use modules, install external packages using `pip`, and write comments for better code readability.

---

# 📌 Topics Covered

- What is Programming?
- Python REPL (Interactive Mode)
- Python as a calculator
- What are Modules?
- Types of Modules
- Built-in Modules
- External Modules
- User-defined Modules
- What is pip?
- Installing Python Packages
- Comments in Python
- Practice Programs

---

# 🖥️ Python REPL (Read-Eval-Print Loop)

Python provides an interactive environment called the **Python REPL**, where you can write and execute Python code line by line.

REPL stands for:

- **R** → Read
- **E** → Evaluate
- **P** → Print
- **L** → Loop

It is useful for:
- Testing small pieces of code
- Performing quick calculations
- Learning Python interactively
- Debugging simple programs

### Example

```python
>>> print("Hello World")
Hello World

>>> 10 + 20
30
```

---

# 🧮 Python as a Calculator

Python can perform mathematical calculations just like a calculator.

### Basic Arithmetic Operators

| Operator | Meaning | Example |
|----------|---------|---------|
| `+` | Addition | `10 + 5` |
| `-` | Subtraction | `10 - 5` |
| `*` | Multiplication | `10 * 5` |
| `/` | Division | `10 / 5` |
| `//` | Floor Division | `10 // 3` |
| `%` | Modulus (Remainder) | `10 % 3` |
| `**` | Exponent (Power) | `2 ** 5` |

### Example

```python
print(15 + 5)
print(20 - 8)
print(6 * 4)
print(20 / 5)
print(20 // 3)
print(20 % 3)
print(2 ** 5)
```

Output

```
20
12
24
4.0
6
2
32
```

---

# 🧩 What is a Module?

A **module** is a Python file (`.py`) that contains reusable code such as functions, classes, and variables.

Instead of writing the same code again and again, we can simply import a module.

### Syntax

```python
import module_name
```

Example:

```python
import math
print(math.sqrt(25))
```

Output:

```
5.0
```

---

# 📚 Types of Modules

## 1. Built-in Modules

These modules come pre-installed with Python.

Examples:

- os
- math
- random
- datetime
- statistics

Example:

```python
import os

print(os.getcwd())
```

This prints the current working directory.

---

## 2. External Modules

These modules are created by other developers and must be installed using **pip**.

Examples:

- pyjokes
- pyttsx3
- numpy
- pandas
- requests

Example:

```python
import pyjokes

print(pyjokes.get_joke())
```

Example:

```python
import pyttsx3

engine = pyttsx3.init()
engine.say("Hello World")
engine.runAndWait()
```

---

## 3. User-defined Modules

A module created by the programmer.

Example

Create a file named

```
greet.py
```

```python
def hello():
    print("Hello Everyone!")
```

Now use it in another file.

```python
import greet

greet.hello()
```

Output

```
Hello Everyone!
```

---

# 📦 What is pip?

**pip** stands for

> **Pip Installs Packages**

It is Python's package manager.

It allows us to install, update and remove external Python libraries.

---

# ⚙️ Common pip Commands

## Install a package

```bash
pip install package_name
```

Example

```bash
pip install pyjokes
```

---

## Install another package

```bash
pip install pyttsx3
```

---

## Upgrade a package

```bash
pip install --upgrade package_name
```

Example

```bash
pip install --upgrade pyjokes
```

---

## Uninstall a package

```bash
pip uninstall package_name
```

Example

```bash
pip uninstall pyjokes
```

---

## Check installed packages

```bash
pip list
```

---

## Show information about a package

```bash
pip show package_name
```

Example

```bash
pip show pyjokes
```

---

# 💬 Comments in Python

Comments are ignored by the Python interpreter.

They make the code easier to understand.

---

## Single-line Comment

```python
# This is a comment
print("Hello")
```

---

## Multi-line Comment

Python does not have a dedicated multi-line comment syntax.

Triple quotes are commonly used for documentation.

```python
"""
This is
a multi-line
comment/documentation string.
"""
```

---

# 📝 Practice Programs

### Using pyjokes

```python
import pyjokes

print(pyjokes.get_joke())
```

---

### Using pyttsx3

```python
import pyttsx3

engine = pyttsx3.init()
engine.say("Welcome to Python.")
engine.runAndWait()
```

---

### Using os Module

```python
import os

print(os.listdir())
```

---

# ⭐ Key Takeaways

- A module is a reusable Python file.
- Python provides Built-in, External and User-defined modules.
- `pip` is Python's package manager.
- External packages are installed using pip.
- Comments improve code readability.
- Built-in modules do not require installation.
- External modules must be installed before use.
- REPL (Read Evaluate Print Loop)

---

# 📖 Important Commands

```bash
pip install package_name
pip uninstall package_name
pip install --upgrade package_name
pip list
pip show package_name
```

---

# 🚀 Summary

In this chapter, I learned:

- ✅ What programming is
- ✅ About REPL
- ✅ What modules are
- ✅ Types of modules
- ✅ Built-in modules
- ✅ External modules
- ✅ User-defined modules
- ✅ How to install packages using pip
- ✅ Basic pip commands
- ✅ How to write comments
- ✅ How to use `pyjokes`, `pyttsx3`, and `os`

---

**Course:** CodeWithHarry Python Course  
**Chapter:** 01 - Modules, Comments & pip