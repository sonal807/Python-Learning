# 📘 Chapter 02 - Variables, Data Types & Operators

## 🎯 Objective

This chapter introduces the fundamental building blocks of Python programming, including variables, keywords, identifiers, data types, operators, user input, type checking, and type casting. These concepts form the foundation for writing Python programs.

---

# 📚 Topics Covered

- Variables
- Keywords
- Identifiers
- Data Types
- Rules for Defining Variables
- `type()` Function
- Operators
- Input Function
- Type Casting
- Practice Programs

---

# 📝 What is a Variable?

A **variable** is a named memory location used to store data. It allows us to save values that can be used and modified later in the program.

### Syntax

```python
variable_name = value
```

### Example

```python
name = "Harry"
age = 25
marks = 92.5

print(name)
print(age)
print(marks)
```

---

# 🔑 Keywords

Keywords are **reserved words** in Python that have predefined meanings. They cannot be used as variable names.

### Examples of Keywords

- False
- True
- None
- if
- else
- elif
- while
- for
- break
- continue
- return
- import
- class
- def
- try
- except
- pass
- with
- lambda

### Example

```python
if = 10
```

❌ This will produce an error because `if` is a keyword.

---

# 🏷️ Identifiers

Identifiers are the names given to variables, functions, classes, and other objects.

### Rules for Identifiers

- Can contain letters, digits and underscore (`_`)
- Cannot begin with a digit
- Cannot contain spaces
- Cannot use special symbols except `_`
- Cannot be a Python keyword
- Python identifiers are case-sensitive

### Valid Identifiers

```python
student
student_name
_marks
age2
```

### Invalid Identifiers

```python
2age
student-name
my age
class
```

---

# 📦 Data Types

A data type specifies the type of value stored in a variable.

## Common Data Types

| Data Type | Example |
|-----------|---------|
| int | 25 |
| float | 3.14 |
| str | "Python" |
| bool | True |
| complex | 2+3j |
| list | [1,2,3] |
| tuple | (1,2,3) |
| dict | {"name":"Harry"} |
| set | {1,2,3} |
| NoneType | None |

### Example

```python
a = 10
b = 3.14
c = "Python"
d = True

print(type(a))
print(type(b))
print(type(c))
print(type(d))
```

---

# 📋 Rules for Defining Variables

- Variable names should be meaningful.
- Use lowercase names where possible.
- Use underscore for multiple words.
- Avoid Python keywords.
- Variable names are case-sensitive.

Example

```python
student_name = "Rahul"
student_marks = 95
```

---

# 🔍 type() Function

The `type()` function returns the data type of a variable or value.

### Syntax

```python
type(object)
```

### Example

```python
a = 10
b = 3.14
c = "Hello"

print(type(a))
print(type(b))
print(type(c))
```

Output

```
<class 'int'>
<class 'float'>
<class 'str'>
```

---

# ➕ Operators

Operators perform operations on values and variables.

## 1. Arithmetic Operators

```python
+
-
*
/
/
//
%
**
```

Example

```python
a = 20
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
```

---

## 2. Assignment Operators

```python
=
+=
-=
*=
/=
%=
```

Example

```python
a = 10
a += 5

print(a)
```

---

## 3. Comparison Operators

```python
==
!=
>
<
>=
<=
```

Example

```python
print(10 > 5)
print(10 == 5)
```

---

## 4. Logical Operators

```python
and
or
not
```

Example

```python
a = True
b = False

print(a and b)
print(a or b)
print(not a)
```

---

# ⌨️ Input Function

The `input()` function is used to take input from the user.

### Syntax

```python
input("Message")
```

### Example

```python
name = input("Enter your name: ")

print("Welcome", name)
```

**Note:** The `input()` function always returns a **string**.

---

# 🔄 Type Casting

Type casting means converting one data type into another.

### Common Functions

```python
int()
float()
str()
bool()
```

### Example

```python
age = input("Enter Age: ")

age = int(age)

print(age + 5)
```

---

# 📝 Practice Programs

During this chapter, I solved practice questions related to:

- Variables
- Keywords
- Identifiers
- Data Types
- Operators
- Input Function
- Type Casting

These practice programs helped strengthen my understanding of Python fundamentals.

---

# ⭐ Key Takeaways

- Variables are used to store data.
- Keywords are reserved words in Python.
- Identifiers are names given to variables and functions.
- Python supports multiple data types.
- The `type()` function returns the type of an object.
- Operators perform different types of operations.
- `input()` is used to accept user input.
- User input is always received as a string.
- Type casting converts one data type into another.

---

# 📖 Important Functions

```python
type()
input()
int()
float()
str()
bool()
```

---

# 🚀 Summary

In this chapter, I learned:

- ✅ Variables
- ✅ Keywords
- ✅ Identifiers
- ✅ Data Types
- ✅ Rules for Defining Variables
- ✅ `type()` Function
- ✅ Arithmetic Operators
- ✅ Assignment Operators
- ✅ Comparison Operators
- ✅ Logical Operators
- ✅ User Input
- ✅ Type Casting
- ✅ Practice Programs

---

**Course:** CodeWithHarry Python Course

**Chapter:** 02 - Variables, Data Types & Operators