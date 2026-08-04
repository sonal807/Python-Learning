# 📘 Chapter 08 - Functions & Recursion

## 🎯 Objective

This chapter introduces one of the most important concepts in Python—**Functions**. Functions help organize code into reusable blocks, making programs shorter, more readable, and easier to maintain. This chapter also introduces the basics of **Recursion**, where a function calls itself to solve a problem.

---

# 📌 Topics Covered

- Introduction to Functions
- Why Functions are Needed
- Advantages of Functions
- Types of Functions
- Function Syntax
- Function Definition
- Function Call
- Parameters
- Arguments
- Types of Arguments
- Default Arguments
- Return Statement
- `print()` vs `return()`
- Introduction to Recursion

---

# 🧩 What is a Function?

A **function** is a reusable block of code that performs a specific task. Instead of writing the same code multiple times, we can write it once inside a function and call it whenever required.

Functions improve code readability, reduce repetition, and make programs easier to manage.

---

# ❓ Why Do We Need Functions?

Without functions, the same code may need to be written repeatedly, making programs lengthy and difficult to maintain.

Functions help by:

- Reusing code
- Reducing repetition
- Improving readability
- Making debugging easier
- Organizing programs into smaller modules

---

# ⭐ Advantages of Functions

- Code Reusability
- Better Code Organization
- Easy Debugging
- Easy Maintenance
- Improved Readability
- Reduces Code Duplication
- Makes Large Programs Easier to Manage

---

# 📚 Types of Functions

Python mainly provides two types of functions.

## 1. Built-in Functions

These are predefined functions provided by Python.

Examples:

- `print()`
- `input()`
- `len()`
- `type()`
- `range()`
- `sum()`
- `max()`
- `min()`
- `sorted()`

Example:

```python
numbers = [10, 20, 30]

print(len(numbers))
print(max(numbers))
```

Output

```
3
30
```

---

## 2. User-defined Functions

These are functions created by the programmer according to the program's requirements.

Example

```python
def greet():
    print("Welcome to Python")

greet()
```

Output

```
Welcome to Python
```

---

# 🔹 Functions Based on Parameters and Return Values

Functions can also be classified based on whether they accept parameters and whether they return a value.

### 1. Function without Parameters and without Return Value

```python
def hello():
    print("Hello World")

hello()
```

---

### 2. Function with Parameters and without Return Value

```python
def greet(name):
    print("Hello", name)

greet("Sonal")
```

---

### 3. Function without Parameters but with Return Value

```python
def number():
    return 100

print(number())
```

---

### 4. Function with Parameters and Return Value

```python
def add(a, b):
    return a + b

print(add(10, 20))
```

---

# 📝 Function Syntax

```python
def function_name(parameters):
    # Function Body
    return value
```

### Syntax Breakdown

- `def` → Keyword used to define a function.
- `function_name` → Name of the function.
- `parameters` → Values accepted by the function (optional).
- Function Body → Statements executed when the function is called.
- `return` → Sends a value back to the caller (optional).

---

# 🛠 Defining a Function

A function is created using the `def` keyword.

Example

```python
def welcome():
    print("Welcome to Python Programming")
```

The function is now defined but will not execute until it is called.

---

# ▶ Calling a Function

A function is executed by writing its name followed by parentheses.

Example

```python
def welcome():
    print("Welcome!")

welcome()
```

Output

```
Welcome!
```

A function can be called multiple times.

```python
welcome()
welcome()
welcome()
```

Output

```
Welcome!
Welcome!
Welcome!
```

# 📥 Function Parameters and Arguments

Functions often need some input to perform a task. This input is passed using **parameters** and **arguments**.

Although these terms are often used interchangeably, they have different meanings.

---

## Parameters

Parameters are the variables listed inside the parentheses while defining a function.

Example

```python
def greet(name):
    print("Hello", name)
```

Here, `name` is a **parameter**.

---

## Arguments

Arguments are the actual values passed to the function when it is called.

Example

```python
def greet(name):
    print("Hello", name)

greet("Sonal")
```

Here, `"Sonal"` is the **argument**.

---

# 📚 Types of Arguments

Python supports different ways of passing arguments to functions.

## 1. Positional Arguments

Arguments are assigned to parameters based on their position.

Example

```python
def student(name, age):
    print(name)
    print(age)

student("Sonal", 20)
```

Output

```
Sonal
20
```

The order of arguments must match the order of parameters.

---

## 2. Keyword Arguments

Arguments are passed using parameter names.

Example

```python
def student(name, age):
    print(name)
    print(age)

student(age=20, name="Sonal")
```

Output

```
Sonal
20
```

Since parameter names are used, the order does not matter.

---

## 3. Default Arguments

A parameter can have a default value. If no value is passed, the default value is used.

Example

```python
def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Sonal")
```

Output

```
Hello Guest
Hello Sonal
```

---

## 4. Variable-Length Arguments (`*args`)

Sometimes we do not know how many arguments will be passed. In such cases, we use `*args`.

Example

```python
def add(*numbers):
    print(sum(numbers))

add(10, 20)
add(10, 20, 30, 40)
```

Output

```
30
100
```

`*args` stores all positional arguments as a tuple.

---

## 5. Keyword Variable-Length Arguments (`**kwargs`)

`**kwargs` accepts multiple keyword arguments and stores them as a dictionary.

Example

```python
def details(**student):
    print(student)

details(name="Sonal", age=20, city="Lucknow")
```

Output

```
{'name': 'Sonal', 'age': 20, 'city': 'Lucknow'}
```

---

# 🔙 Return Statement

The `return` statement sends a value back to the function caller.

Once `return` is executed, the function immediately stops executing.

Syntax

```python
return value
```

Example

```python
def square(num):
    return num * num

result = square(5)

print(result)
```

Output

```
25
```

A function can also return multiple values.

Example

```python
def calculation(a, b):
    return a + b, a - b

add, subtract = calculation(10, 5)

print(add)
print(subtract)
```

Output

```
15
5
```

---

# 🖨️ `print()` vs `return`

Many beginners confuse these two.

## `print()`

- Displays output on the screen.
- Does not send any value back.
- Mainly used for debugging and displaying information.

Example

```python
def add(a, b):
    print(a + b)

result = add(10, 20)

print(result)
```

Output

```
30
None
```

---

## `return`

- Sends a value back to the caller.
- Returned value can be stored in a variable.
- Makes functions reusable.

Example

```python
def add(a, b):
    return a + b

result = add(10, 20)

print(result)
```

Output

```
30
```

---

# 🌍 Variable Scope

The scope of a variable determines where it can be accessed.

Python mainly has two types of variables.

## 1. Local Variable

A local variable is created inside a function and can only be accessed within that function.

Example

```python
def show():
    message = "Hello"

    print(message)

show()
```

---

## 2. Global Variable

A global variable is declared outside a function and can be accessed from anywhere in the program.

Example

```python
message = "Python"

def show():
    print(message)

show()

print(message)
```

Output

```
Python
Python
```

---

# 🌐 The `global` Keyword

Normally, a global variable cannot be modified inside a function.

To modify it, we use the `global` keyword.

Example

```python
count = 10

def increase():
    global count
    count += 1

increase()

print(count)
```

Output

```
11
```

The `global` keyword tells Python to use the global variable instead of creating a new local variable.

---

# ⭐ Key Points

- Parameters receive values inside a function definition.
- Arguments are the actual values passed during a function call.
- Python supports positional, keyword, default, variable-length (`*args`), and keyword variable-length (`**kwargs`) arguments.
- `return` sends values back to the caller.
- `print()` only displays output.
- Local variables exist only inside a function.
- Global variables can be accessed throughout the program.
- The `global` keyword allows modification of global variables inside a function.

# 🛠 Built-in Functions

Python provides many predefined functions known as **built-in functions**. These functions are readily available and do not need to be defined by the programmer.

Some commonly used built-in functions are:

| Function | Description |
|----------|-------------|
| `print()` | Displays output on the screen |
| `input()` | Takes input from the user |
| `len()` | Returns the length of an object |
| `type()` | Returns the data type of an object |
| `range()` | Generates a sequence of numbers |
| `sum()` | Returns the sum of elements |
| `max()` | Returns the largest element |
| `min()` | Returns the smallest element |
| `abs()` | Returns the absolute value |
| `round()` | Rounds a number |
| `sorted()` | Returns a sorted list |
| `enumerate()` | Returns index-value pairs |
| `zip()` | Combines multiple iterables |

### Example

```python
numbers = [10, 20, 30, 40]

print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))
```

Output

```
4
40
10
100
```

---

# 👨‍💻 User-defined Functions

User-defined functions are functions created by the programmer according to the requirements of the program.

### Example

```python
def area(length, width):
    return length * width

print(area(10, 5))
```

Output

```
50
```

---

# ⚡ Lambda Functions

A **Lambda Function** is a small anonymous function written in a single line.

Instead of using the `def` keyword, lambda functions are created using the `lambda` keyword.

### Syntax

```python
lambda arguments : expression
```

### Example

```python
square = lambda x: x * x

print(square(5))
```

Output

```
25
```

### Example

```python
add = lambda a, b: a + b

print(add(10, 20))
```

Output

```
30
```

Lambda functions are commonly used for short operations and with functions like `map()`, `filter()`, and `sorted()`.

---

# 📝 Docstrings

A **Docstring** is a string written inside a function to describe what the function does.

It is enclosed within triple quotes (`""" """`).

Docstrings help other programmers understand the purpose of the function.

### Example

```python
def add(a, b):
    """
    Returns the sum of two numbers.
    """
    return a + b

print(add.__doc__)
```

Output

```
Returns the sum of two numbers.
```

---

# 🏷 Type Hints

Type hints allow programmers to specify the expected data types of function parameters and return values.

They improve code readability and make development easier.

### Example

```python
def add(a: int, b: int) -> int:
    return a + b

print(add(10, 20))
```

Output

```
30
```

Type hints are optional in Python and are mainly used for better code documentation.

---

# 🔁 Introduction to Recursion

**Recursion** is a programming technique in which a function calls itself to solve a problem.

Instead of using loops, some problems can be solved more naturally using recursion.

Every recursive function must have:

- A **Base Case**
- A **Recursive Case**

Without a base case, recursion will continue forever and eventually cause an error.

---

# 🔹 Base Case

The **Base Case** is the condition that stops the recursive function.

It prevents infinite recursion.

### Example

```python
def countdown(n):

    if n == 0:
        return

    print(n)
    countdown(n - 1)

countdown(5)
```

Output

```
5
4
3
2
1
```

When `n` becomes `0`, the function stops calling itself.

---

# 🔹 Recursive Case

The recursive case is where the function calls itself with a smaller or modified problem.

### Example

```python
def show(n):

    if n == 0:
        return

    print(n)

    show(n - 1)

show(3)
```

Output

```
3
2
1
```

The function keeps calling itself until the base case is reached.

---

# 📚 Call Stack

Whenever a function is called, Python stores it in a memory area called the **Call Stack**.

Each recursive call creates a new stack frame.

As soon as the base case is reached, the stack starts removing function calls one by one.

### Example

```python
def fun(n):

    if n == 0:
        return

    print(n)

    fun(n - 1)

fun(3)
```

Execution Order

```
fun(3)
 ↓
fun(2)
 ↓
fun(1)
 ↓
fun(0)
```

Returning Back

```
fun(0)
 ↑
fun(1)
 ↑
fun(2)
 ↑
fun(3)
```

This process is known as **Stack Unwinding**.

---

# 💡 Key Points

- Python provides many built-in functions.
- Programmers can create their own user-defined functions.
- Lambda functions are useful for short, one-line operations.
- Docstrings improve code documentation.
- Type hints improve readability and maintainability.
- Recursion is a technique where a function calls itself.
- Every recursive function must have a base case.
- The call stack keeps track of recursive function calls.
- Once the base case is reached, the recursive calls return one by one.

# 💻 Common Recursive Programs

Recursion is widely used to solve problems that can be broken down into smaller, similar sub-problems. Below are some common recursive programs.

---

# 1️⃣ Factorial of a Number

The factorial of a number is the product of all positive integers less than or equal to that number.

### Formula

```
5! = 5 × 4 × 3 × 2 × 1 = 120
```

### Program

```python
def factorial(n):

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)

print(factorial(5))
```

**Output**

```
120
```

---

# 2️⃣ Fibonacci Series

In the Fibonacci sequence, each number is the sum of the previous two numbers.

```
0 1 1 2 3 5 8 13 ...
```

### Program

```python
def fibonacci(n):

    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))
```

**Output**

```
8
```

---

# 3️⃣ Sum of First N Natural Numbers

### Program

```python
def sum_n(n):

    if n == 1:
        return 1

    return n + sum_n(n - 1)

print(sum_n(5))
```

**Output**

```
15
```

---

# 4️⃣ Reverse a String

### Program

```python
def reverse(text):

    if len(text) == 1:
        return text

    return reverse(text[1:]) + text[0]

print(reverse("Python"))
```

**Output**

```
nohtyP
```

---

# 5️⃣ Countdown Program

### Program

```python
def countdown(n):

    if n == 0:
        return

    print(n)

    countdown(n - 1)

countdown(5)
```

**Output**

```
5
4
3
2
1
```

---

# ⚖️ Advantages of Recursion

Recursion offers several benefits when solving certain types of problems.

- Makes code shorter and cleaner.
- Easy to solve problems that can be divided into smaller sub-problems.
- Useful for tree and graph traversal.
- Simplifies mathematical and recursive algorithms.
- Reduces the need for complex loops in some cases.
- Improves code readability for recursive problems.

---

# ⚠️ Disadvantages of Recursion

Although recursion is powerful, it also has some drawbacks.

- Uses more memory because of the call stack.
- Can be slower than iterative solutions.
- May cause **Stack Overflow Error** if the recursion depth becomes too large.
- Debugging recursive functions can be difficult for beginners.

---

# 🔄 Recursion vs Iteration

| Feature | Recursion | Iteration |
|---------|-----------|-----------|
| Uses | Function Calls | Loops |
| Memory Usage | Higher | Lower |
| Speed | Usually Slower | Usually Faster |
| Code Length | Shorter | Sometimes Longer |
| Readability | Better for recursive problems | Better for simple repetition |
| Risk | Stack Overflow | No Stack Overflow |

---

# 🌍 Real-Life Applications of Functions

Functions are one of the most important building blocks in programming.

They are used in:

- Banking Systems
- ATM Machines
- Calculator Applications
- Login Systems
- Student Management Systems
- E-commerce Websites
- Data Analysis
- Machine Learning Projects
- Web Development
- Desktop Applications
- Mobile Applications

---

# 🌍 Real-Life Applications of Recursion

Recursion is commonly used in:

- Tree Traversal
- File and Folder Navigation
- Binary Search Trees
- Depth First Search (DFS)
- Divide and Conquer Algorithms
- Backtracking Problems
- Dynamic Programming
- Artificial Intelligence
- Maze Solving
- Parsing Expressions

---

# 💡 Best Practices

- Write small and focused functions.
- Give meaningful names to functions.
- Keep one function responsible for one task.
- Avoid unnecessary global variables.
- Always include a base case in recursive functions.
- Use recursion only when it makes the solution simpler.
- Prefer iteration for very large repetitive tasks.
- Write proper docstrings for important functions.
- Return values instead of printing whenever possible.

---

# ⚠️ Common Beginner Mistakes

### ❌ Forgetting the Base Case

```python
def show(n):
    return show(n - 1)
```

This results in infinite recursion and eventually raises a **RecursionError**.

---

### ❌ Using `print()` Instead of `return`

Incorrect

```python
def square(n):
    print(n * n)
```

Correct

```python
def square(n):
    return n * n
```

---

### ❌ Writing Large Functions

Avoid writing functions that perform multiple unrelated tasks.

Instead, divide the program into smaller reusable functions.

---

### ❌ Modifying Global Variables Unnecessarily

Use local variables whenever possible to keep functions independent and reusable.

---

# ⭐ Key Points

- Functions make programs modular and reusable.
- Parameters receive data, while arguments provide data.
- The `return` statement sends values back to the caller.
- Built-in functions are provided by Python.
- User-defined functions are created by programmers.
- Lambda functions are useful for simple one-line operations.
- Every recursive function must have a base case.
- The call stack manages recursive function calls.
- Recursion is powerful but should be used carefully.

# ⚡ Quick Revision Tables

## 📖 Types of Functions

| Type | Description |
|------|-------------|
| Built-in Functions | Functions already provided by Python |
| User-defined Functions | Functions created by the programmer |

---

## 📖 Functions Based on Parameters and Return Values

| Function Type | Parameters | Return Value |
|--------------|------------|--------------|
| Without Parameters & Without Return | ❌ | ❌ |
| With Parameters & Without Return | ✅ | ❌ |
| Without Parameters & With Return | ❌ | ✅ |
| With Parameters & With Return | ✅ | ✅ |

---

## 📖 Types of Arguments

| Argument Type | Description |
|--------------|-------------|
| Positional Arguments | Passed according to position |
| Keyword Arguments | Passed using parameter names |
| Default Arguments | Uses a default value if no argument is provided |
| Variable-Length Arguments (`*args`) | Accepts multiple positional arguments |
| Keyword Variable-Length Arguments (`**kwargs`) | Accepts multiple keyword arguments |

---

## 📖 Variable Scope

| Variable | Scope |
|----------|-------|
| Local Variable | Accessible only inside the function |
| Global Variable | Accessible throughout the program |

---

## 📖 Recursion Terminology

| Term | Meaning |
|------|---------|
| Base Case | Stops the recursive function |
| Recursive Case | Function calls itself with a smaller problem |
| Call Stack | Stores active function calls |
| Stack Unwinding | Returning from recursive calls after reaching the base case |

---

# 📚 Important Built-in Functions

| Function | Purpose |
|----------|---------|
| `print()` | Displays output |
| `input()` | Takes input from the user |
| `len()` | Returns the length of an object |
| `type()` | Returns the data type |
| `range()` | Generates a sequence of numbers |
| `sum()` | Returns the sum of elements |
| `max()` | Returns the largest element |
| `min()` | Returns the smallest element |
| `abs()` | Returns the absolute value |
| `round()` | Rounds a number |
| `sorted()` | Returns a sorted list |
| `enumerate()` | Returns index-value pairs |
| `zip()` | Combines multiple iterables |

---

# ⭐ Key Takeaways

- Functions help organize code into reusable blocks.
- They improve readability, maintainability, and reduce code duplication.
- Python provides both built-in and user-defined functions.
- Parameters define the expected input, while arguments provide actual values.
- Python supports positional, keyword, default, `*args`, and `**kwargs` arguments.
- The `return` statement sends values back to the caller.
- `print()` displays output, whereas `return` provides reusable results.
- Local variables exist only within a function, while global variables can be accessed throughout the program.
- The `global` keyword allows modification of global variables inside a function.
- Lambda functions are useful for short, anonymous functions.
- Docstrings improve documentation and readability.
- Type hints make code easier to understand and maintain.
- Recursion is a technique where a function calls itself.
- Every recursive function must include a base case to prevent infinite recursion.
- The call stack keeps track of recursive function calls.
- Functions and recursion are fundamental concepts used in software development, data science, machine learning, web development, automation, and algorithm design.

---

# 🚀 Summary

In this chapter, I learned:

- ✅ Introduction to Functions
- ✅ Why Functions are Needed
- ✅ Advantages of Functions
- ✅ Types of Functions
- ✅ Function Syntax
- ✅ Function Definition
- ✅ Function Calling
- ✅ Parameters
- ✅ Arguments
- ✅ Positional Arguments
- ✅ Keyword Arguments
- ✅ Default Arguments
- ✅ Variable-Length Arguments (`*args`)
- ✅ Keyword Variable-Length Arguments (`**kwargs`)
- ✅ Return Statement
- ✅ Difference Between `print()` and `return()`
- ✅ Local Variables
- ✅ Global Variables
- ✅ `global` Keyword
- ✅ Built-in Functions
- ✅ User-defined Functions
- ✅ Lambda Functions
- ✅ Docstrings
- ✅ Type Hints
- ✅ Introduction to Recursion
- ✅ Base Case
- ✅ Recursive Case
- ✅ Call Stack
- ✅ Factorial Using Recursion
- ✅ Fibonacci Using Recursion
- ✅ Sum of Natural Numbers
- ✅ Reverse a String Using Recursion
- ✅ Countdown Using Recursion
- ✅ Advantages of Recursion
- ✅ Disadvantages of Recursion
- ✅ Recursion vs Iteration
- ✅ Real-Life Applications
- ✅ Best Practices
- ✅ Common Beginner Mistakes

This chapter introduced me to one of the most powerful concepts in Python—**Functions**. I learned how to divide large programs into smaller, reusable functions, making code more organized, readable, and maintainable. I also explored **Recursion**, understanding how a function can solve complex problems by calling itself until a base case is reached. These concepts are fundamental for writing efficient programs and form the foundation for advanced topics such as Object-Oriented Programming (OOP), Data Structures & Algorithms (DSA), Web Development, Data Science, Artificial Intelligence, and Machine Learning.

---

# 📚 Course Information

**Course:** CodeWithHarry Python Course

**Chapter:** 08 - Functions & Recursion

**Language:** Python

**Author:** Sonal Rai