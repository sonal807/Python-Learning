# 📘 Chapter 03 - Strings

## 🎯 Objective

This chapter introduces **Strings** in Python. A string is one of the most commonly used data types in programming. In this chapter, I learned how to create strings, access characters using indexing, extract parts of strings using slicing, use various built-in string functions, and work with escape sequence characters.

---

# 📚 Topics Covered

- What is a String?
- Characteristics of Strings
- String Indexing
- String Slicing
- Negative Indexing
- Slicing with Skip Value
- String Functions
- Escape Sequence Characters

---

# 📝 What is a String?

A **String** is a sequence of characters enclosed within single quotes (`' '`), double quotes (`" "`), or triple quotes (`''' '''` or `""" """`).

Strings are used to store textual data such as names, messages, and sentences.

### Examples

```python
name = "Sonal"
city = 'Lucknow'
message = """Welcome to Python"""
```

---

# ✨ Characteristics of Strings

- Strings are enclosed in quotes.
- Strings are immutable (cannot be changed after creation).
- Strings are ordered collections of characters.
- Every character has an index.

---

# 🔢 String Indexing

Each character in a string has an index.

Example:

```python
name = "Python"
```

| Character | P | y | t | h | o | n |
|-----------|---|---|---|---|---|---|
| Index | 0 | 1 | 2 | 3 | 4 | 5 |
| Negative Index | -6 | -5 | -4 | -3 | -2 | -1 |

Example

```python
name = "Python"

print(name[0])
print(name[3])
print(name[-1])
```

Output

```
P
h
n
```

---

# ✂️ String Slicing

String slicing is used to extract a portion of a string.

### Syntax

```python
string[start:end]
```

Example

```python
name = "Python"

print(name[0:3])
print(name[2:6])
```

Output

```
Pyt
thon
```

---

# ⏩ String Slicing with Skip Value

Syntax

```python
string[start:end:step]
```

Example

```python
word = "Programming"

print(word[0:11:2])
```

Output

```
Pormig
```

---

# ◀️ Negative Slicing

Negative indexing starts from the end of the string.

Example

```python
name = "Python"

print(name[-4:-1])
```

Output

```
tho
```

---

# 🛠️ Common String Functions

## len()

Returns the length of the string.

```python
len("Python")
```

---

## count()

Counts the occurrence of a character or substring.

```python
text.count("a")
```

---

## find()

Returns the index of the first occurrence.

```python
text.find("Python")
```

Returns **-1** if not found.

---

## replace()

Replaces one string with another.

```python
text.replace("Java", "Python")
```

---

## upper()

Converts all characters to uppercase.

```python
text.upper()
```

---

## lower()

Converts all characters to lowercase.

```python
text.lower()
```

---

## capitalize()

Capitalizes the first character.

```python
text.capitalize()
```

---

## title()

Capitalizes the first letter of every word.

```python
text.title()
```

---

## startswith()

Checks whether a string starts with a specified value.

```python
text.startswith("Python")
```

---

## endswith()

Checks whether a string ends with a specified value.

```python
text.endswith(".")
```

---

## strip()

Removes extra spaces from both ends.

```python
text.strip()
```

---

# 🔤 Escape Sequence Characters

Escape sequences are special characters used inside strings.

| Escape Sequence | Meaning |
|----------------|---------|
| `\n` | New Line |
| `\t` | Tab Space |
| `\\` | Backslash |
| `\'` | Single Quote |
| `\"` | Double Quote |

Example

```python
print("Hello\nWorld")
print("Python\tProgramming")
```

Output

```
Hello
World
Python    Programming
```

---

# ⭐ Key Takeaways

- Strings store textual data.
- Strings are immutable.
- Every character has an index.
- Slicing extracts a portion of a string.
- Negative indexing accesses characters from the end.
- Python provides many useful built-in string methods.
- Escape sequence characters help format output.

---

# 📖 Important String Functions

```python
len()
count()
find()
replace()
upper()
lower()
capitalize()
title()
startswith()
endswith()
strip()
```

---

# 🚀 Summary

In this chapter, I learned:

- ✅ What is a String
- ✅ Characteristics of Strings
- ✅ String Indexing
- ✅ String Slicing
- ✅ Negative Indexing
- ✅ Slicing with Skip Value
- ✅ Common String Functions
- ✅ Escape Sequence Characters
- ✅ Solved Practice Questions

This chapter helped me understand how to create, access, manipulate, and format strings in Python. These concepts are fundamental and are used frequently in Python programming.

---

**Course:** CodeWithHarry Python Course

**Chapter:** 03 - Strings