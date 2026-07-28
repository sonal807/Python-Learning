# 📘 Chapter 06 - Conditional Statements

## 🎯 Objective

The objective of this chapter is to understand **Conditional Statements** in Python, which allow a program to make decisions based on different conditions.

In this chapter, I learned how to execute different blocks of code depending on whether a condition is **True** or **False**. I also learned how to use various conditional statements such as `if`, `if-else`, `if-elif-else`, and nested `if` statements to control the flow of a program.

By the end of this chapter, I understood how decision-making works in Python and how it is used to build interactive and intelligent programs.

---

# 📚 Topics Covered

- Conditional Statements
- Why Conditional Statements are Needed
- Flow of Execution
- if Statement
- if-else Statement
- if-elif-else Statement
- Nested if Statements
- Real-Life Applications

---

# 🤔 What are Conditional Statements?

A **Conditional Statement** is a programming construct that allows a program to make decisions based on a condition.

The program evaluates a condition. If the condition is **True**, one block of code is executed. If the condition is **False**, another block (if available) is executed.

Conditional statements make programs interactive and capable of responding differently to different situations.

---

# ❓ Why are Conditional Statements Needed?

Without conditional statements, a program would execute every statement in the same order every time.

Conditional statements allow programs to:

- Make decisions.
- Perform different actions based on user input.
- Validate data.
- Control the flow of execution.
- Build interactive applications.

---

# 🔄 Flow of Execution

When Python encounters a conditional statement:

1. The condition is evaluated.
2. If the condition is **True**, the corresponding block of code is executed.
3. If the condition is **False**, Python checks for another condition (`elif`) or executes the `else` block if available.
4. The program continues executing the remaining statements.

---

# 📝 Types of Conditional Statements

Python provides the following conditional statements:

- `if`
- `if-else`
- `if-elif-else`
- Nested `if`

Each statement is used depending on the complexity of the decision-making process.

---

# 1️⃣ if Statement

The `if` statement executes a block of code **only when the specified condition is True**.

If the condition is False, Python skips the block.

### Syntax

```python
if condition:
    # code
```

### Example

```python
age = 20

if age >= 18:
    print("You are eligible to vote.")
```

**Output**

```
You are eligible to vote.
```

---

# 2️⃣ if-else Statement

The `if-else` statement provides two possible execution paths.

If the condition is **True**, the `if` block is executed.

Otherwise, the `else` block is executed.

### Syntax

```python
if condition:
    # code
else:
    # code
```

### Example

```python
age = 16

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
```

**Output**

```
Not eligible to vote
```

---

# 3️⃣ if-elif-else Statement

The `if-elif-else` statement is used when multiple conditions need to be checked.

Python evaluates each condition one by one.

As soon as one condition becomes **True**, its corresponding block is executed, and the remaining conditions are skipped.

If none of the conditions are True, the `else` block is executed.

### Syntax

```python
if condition1:
    # code
elif condition2:
    # code
elif condition3:
    # code
else:
    # code
```

### Example

```python
marks = 82

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Grade D")
```

**Output**

```
Grade B
```

---

# 4️⃣ Nested if Statement

A **Nested if** means writing one `if` statement inside another `if` statement.

Nested conditions are useful when one condition depends on another.

### Syntax

```python
if condition1:
    if condition2:
        # code
```

### Example

```python
age = 22
has_license = True

if age >= 18:
    if has_license:
        print("You can drive.")
```

**Output**

```
You can drive.
```

---

# 🌍 Why Use Conditional Statements?

Conditional statements are useful when:

- Making decisions based on user input.
- Validating usernames and passwords.
- Checking eligibility.
- Performing calculations based on conditions.
- Controlling the program flow.
- Creating interactive applications.

---

# 📌 Real-Life Applications

Conditional statements are commonly used in:

- ATM Machines (PIN verification)
- Login Systems (Username and Password validation)
- Online Shopping (Discount calculation)
- Voting Eligibility Checker
- Student Result Management System
- Traffic Signal Control
- Banking Applications
- Online Examination Systems
- Movie Ticket Booking
- Weather-Based Applications

# 🔍 Comparison Operators

Comparison operators are used to compare two values. They always return a Boolean value (`True` or `False`).

| Operator | Description | Example |
|----------|-------------|---------|
| `==` | Equal to | `5 == 5` → `True` |
| `!=` | Not equal to | `5 != 3` → `True` |
| `>` | Greater than | `10 > 5` → `True` |
| `<` | Less than | `5 < 10` → `True` |
| `>=` | Greater than or equal to | `5 >= 5` → `True` |
| `<=` | Less than or equal to | `4 <= 5` → `True` |

### Example

```python
a = 10
b = 20

print(a == b)
print(a != b)
print(a < b)
print(a >= b)
```

**Output**

```
False
True
True
False
```

---

# 🔗 Logical Operators

Logical operators are used to combine multiple conditions.

Python provides three logical operators:

- `and`
- `or`
- `not`

---

## 1. and Operator

Returns `True` only if **both conditions are True**.

### Example

```python
age = 20
citizen = True

if age >= 18 and citizen:
    print("Eligible to vote")
```

**Output**

```
Eligible to vote
```

---

## 2. or Operator

Returns `True` if **at least one condition is True**.

### Example

```python
day = "Sunday"

if day == "Saturday" or day == "Sunday":
    print("Weekend")
```

**Output**

```
Weekend
```

---

## 3. not Operator

The `not` operator reverses the Boolean value.

### Example

```python
logged_in = False

if not logged_in:
    print("Please login first")
```

**Output**

```
Please login first
```

---

# 📦 Membership Operators

Membership operators check whether a value exists inside a sequence such as a string, list, tuple, or set.

Python provides:

- `in`
- `not in`

---

## in Operator

Returns `True` if the value exists.

### Example

```python
fruits = ["Apple", "Banana", "Mango"]

print("Apple" in fruits)
```

**Output**

```
True
```

---

## not in Operator

Returns `True` if the value does not exist.

### Example

```python
fruits = ["Apple", "Banana", "Mango"]

print("Orange" not in fruits)
```

**Output**

```
True
```

---

# 🆔 Identity Operators

Identity operators compare whether two variables refer to the **same object in memory**.

Python provides:

- `is`
- `is not`

---

## is Operator

Returns `True` if both variables refer to the same object.

### Example

```python
a = [1,2,3]
b = a

print(a is b)
```

**Output**

```
True
```

---

## is not Operator

Returns `True` if two variables refer to different objects.

### Example

```python
a = [1,2,3]
b = [1,2,3]

print(a is not b)
```

**Output**

```
True
```

> **Note:** Use `==` to compare values and `is` to compare object identity.

---

# ✅ Boolean Values

Python has two Boolean values:

- `True`
- `False`

Boolean values are commonly used in conditional statements.

### Example

```python
is_student = True

if is_student:
    print("Student Discount Applied")
```

**Output**

```
Student Discount Applied
```

---

# ⚡ Truthy and Falsy Values

In Python, every value is considered either **Truthy** or **Falsy**.

### Falsy Values

The following values are treated as `False`:

```python
False
None
0
0.0
''
[]
()
{}
set()
```

### Truthy Values

Everything else is considered `True`.

Example

```python
if "Python":
    print("Truthy")
```

**Output**

```
Truthy
```

---

# 📏 Indentation in Python

Python uses **indentation** (spaces or tabs) to define blocks of code.

Unlike many programming languages, Python does **not** use curly braces `{}`.

### Correct Example

```python
age = 20

if age >= 18:
    print("Eligible")
```

### Incorrect Example

```python
age = 20

if age >= 18:
print("Eligible")
```

This produces an **IndentationError**.

> **Best Practice:** Use **4 spaces** for each indentation level, following the PEP 8 style guide.

---

# ⚡ Short-Circuit Evaluation

Python stops evaluating logical expressions as soon as the final result is known.

### Example using `and`

```python
x = 5

if x > 10 and x / 0 > 1:
    print("Hello")
```

The second condition is **never evaluated** because `x > 10` is already `False`.

---

### Example using `or`

```python
x = 20

if x > 10 or x / 0 > 1:
    print("Valid")
```

Since the first condition is `True`, Python skips the second condition.

---

# ⚠️ Common Mistakes

### ❌ Using `=` instead of `==`

Incorrect

```python
if age = 18:
```

Correct

```python
if age == 18:
```

---

### ❌ Forgetting indentation

```python
if age >= 18:
print("Eligible")
```

This results in an **IndentationError**.

---

### ❌ Writing multiple `if` statements instead of `elif`

Incorrect

```python
if marks >= 90:
    print("A")

if marks >= 80:
    print("B")
```

Better

```python
if marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
```

---

# 💡 Best Practices

- Use meaningful variable names.
- Keep conditions simple and readable.
- Use `elif` instead of multiple `if` statements when checking related conditions.
- Avoid deeply nested `if` statements whenever possible.
- Use parentheses to improve readability in complex conditions.
- Follow proper indentation using **4 spaces**.
- Write conditions that are easy to understand and maintain.

# 📌 Real-Life Examples

Conditional statements are widely used in real-world applications to make decisions based on different situations.

### 1. ATM Machine

Check whether the entered PIN is correct before allowing access to the account.

```python
pin = 1234
entered_pin = 1234

if entered_pin == pin:
    print("Access Granted")
else:
    print("Invalid PIN")
```

---

### 2. Login System

Verify the username and password before logging in.

```python
username = "admin"
password = "python123"

if username == "admin" and password == "python123":
    print("Login Successful")
else:
    print("Invalid Credentials")
```

---

### 3. Voting Eligibility

Check whether a person is eligible to vote.

```python
age = 20

if age >= 18:
    print("Eligible to Vote")
else:
    print("Not Eligible")
```

---

### 4. Online Shopping Discount

Apply a discount based on the purchase amount.

```python
amount = 2500

if amount >= 2000:
    print("20% Discount Applied")
else:
    print("No Discount")
```

---

### 5. Traffic Signal System

Decide whether vehicles should stop or move.

```python
signal = "Red"

if signal == "Green":
    print("Go")
elif signal == "Yellow":
    print("Wait")
else:
    print("Stop")
```

---

### 6. Student Result

Display pass or fail based on marks.

```python
marks = 45

if marks >= 33:
    print("Pass")
else:
    print("Fail")
```

---

# ⚡ Quick Revision Table

| Statement | Purpose |
|-----------|---------|
| `if` | Executes code when a condition is True |
| `if-else` | Executes one block if True and another if False |
| `if-elif-else` | Checks multiple conditions one by one |
| Nested `if` | Places one `if` statement inside another |

---

## 📖 Comparison Operators

| Operator | Meaning |
|----------|---------|
| `==` | Equal to |
| `!=` | Not Equal to |
| `>` | Greater Than |
| `<` | Less Than |
| `>=` | Greater Than or Equal To |
| `<=` | Less Than or Equal To |

---

## 📖 Logical Operators

| Operator | Meaning |
|----------|---------|
| `and` | True if both conditions are True |
| `or` | True if at least one condition is True |
| `not` | Reverses the Boolean value |

---

## 📖 Membership Operators

| Operator | Meaning |
|----------|---------|
| `in` | Checks if a value exists |
| `not in` | Checks if a value does not exist |

---

## 📖 Identity Operators

| Operator | Meaning |
|----------|---------|
| `is` | Checks whether two variables refer to the same object |
| `is not` | Checks whether two variables refer to different objects |

---

# ⭐ Key Takeaways

- Conditional statements help programs make decisions.
- The `if` statement executes code only when the condition is `True`.
- The `if-else` statement provides two execution paths.
- The `if-elif-else` statement is useful for checking multiple conditions.
- Nested `if` statements are used for complex decision-making.
- Comparison operators always return a Boolean value.
- Logical operators combine multiple conditions.
- Membership operators check whether a value exists in a sequence.
- Identity operators compare object identity, not values.
- Python uses indentation to define code blocks.
- Every value in Python is either Truthy or Falsy.
- Short-circuit evaluation improves program efficiency by skipping unnecessary condition checks.

---

# 🚀 Summary

In this chapter, I learned:

- ✅ Conditional Statements
- ✅ Why Conditional Statements are Needed
- ✅ Flow of Execution
- ✅ `if` Statement
- ✅ `if-else` Statement
- ✅ `if-elif-else` Statement
- ✅ Nested `if` Statement
- ✅ Comparison Operators
- ✅ Logical Operators
- ✅ Membership Operators
- ✅ Identity Operators
- ✅ Boolean Values
- ✅ Truthy and Falsy Values
- ✅ Indentation in Python
- ✅ Short-Circuit Evaluation
- ✅ Real-Life Applications
- ✅ Best Practices
- ✅ Common Mistakes

This chapter introduced me to **decision-making in Python**. I learned how to control the flow of a program using conditional statements and different operators. These concepts are essential for building interactive applications, validating user input, implementing business logic, and solving real-world programming problems effectively.

---

## 📚 Course Information

**Course:** CodeWithHarry Python Course

**Chapter:** 06 - Conditional Statements

**Language:** Python

**Author:** Sonal Rai