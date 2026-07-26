# 📘 Chapter 04 - Lists & Tuples

## 🎯 Objective

The objective of this chapter is to understand Python's two most commonly used collection data types: **Lists** and **Tuples**. In this chapter, I learned how to create them, access their elements using indexing, extract data using slicing, modify lists, and use various built-in methods and operations efficiently.

By the end of this chapter, I understood when to use a **List** and when a **Tuple** is a better choice.

---

# 📚 Topics Covered

- Lists
- Creating Lists
- Characteristics of Lists
- List Indexing
- List Slicing
- Modifying Lists
- Nested Lists
- Tuples
- Creating Tuples
- Characteristics of Tuples
- Tuple Indexing
- Tuple Slicing
- Tuple Methods
- Tuple Operations
- Difference Between Lists & Tuples
- Similarities Between Lists & Tuples

---

# 📋 What is a List?

A **List** is one of Python's built-in data structures used to store multiple values in a single variable.

Unlike variables that store only one value, a list can store many values together.

Lists are enclosed within **square brackets `[ ]`** and elements are separated using commas.

### Syntax

```python
list_name = [item1, item2, item3]
```

### Example

```python
fruits = ["Apple", "Mango", "Banana"]

print(fruits)
```

**Output**

```
['Apple', 'Mango', 'Banana']
```

Lists can contain different data types in a single collection.

Example

```python
student = ["Sonal", 21, 75.5, True]

print(student)
```

---

# ✨ Characteristics of Lists

- Ordered collection
- Mutable (elements can be changed)
- Allows duplicate values
- Supports indexing
- Supports slicing
- Can store different data types
- Can contain another list (Nested List)
- Dynamic in size (elements can be added or removed)

---

# 🔢 List Indexing

Every element inside a list has its own position called an **index**.

Python indexing starts from **0**.

Example

```python
fruits = ["Apple", "Banana", "Orange", "Mango"]

print(fruits[0])
print(fruits[2])
```

**Output**

```
Apple
Orange
```

### Negative Indexing

Negative indexing starts from the last element.

```python
fruits = ["Apple", "Banana", "Orange", "Mango"]

print(fruits[-1])
print(fruits[-2])
```

**Output**

```
Mango
Orange
```

---

# ✂️ List Slicing

Slicing is used to access multiple elements from a list.

### Syntax

```python
list_name[start : end]
```

The starting index is included, while the ending index is excluded.

Example

```python
numbers = [10,20,30,40,50,60]

print(numbers[1:5])
```

**Output**

```
[20, 30, 40, 50]
```

---

## Slicing with Step Value

We can also skip elements while slicing.

### Syntax

```python
list_name[start:end:step]
```

Example

```python
numbers = [10,20,30,40,50,60,70]

print(numbers[0:7:2])
```

**Output**

```
[10, 30, 50, 70]
```

---

# 📝 Modifying Lists

Lists are **mutable**, meaning their values can be changed after creation.

Example

```python
friends = ["Apple", "Orange", "Banana"]

friends[1] = "Mango"

print(friends)
```

**Output**

```
['Apple', 'Mango', 'Banana']
```

You can also modify multiple values using slicing.

```python
numbers = [1,2,3,4,5]

numbers[1:3] = [20,30]

print(numbers)
```

**Output**

```
[1, 20, 30, 4, 5]
```

---

# 📂 Nested Lists

A list can contain another list inside it.

Example

```python
students = [
    ["Rahul", 20],
    ["Aman", 21],
    ["Sonal", 22]
]

print(students)
print(students[1])
print(students[1][0])
```

**Output**

```
[['Rahul', 20], ['Aman', 21], ['Sonal', 22]]
['Aman', 21]
Aman
```

Nested lists are useful for storing data in rows and columns, similar to a table.

---

# 💡 Why Use Lists?

Lists are useful when:

- Data changes frequently.
- You need to store multiple values.
- You need to add or remove items.
- You need sorting and searching operations.
- The number of elements is not fixed.

### Real-Life Examples

- Shopping cart
- Student records
- Employee database
- Playlist in a music app
- To-do list
- Online order history
- Chat messages

# 🛠️ List Methods

Python provides several built-in methods to perform different operations on lists. These methods make it easy to add, remove, search, sort, and manipulate data efficiently.

---

## 1. append()

The `append()` method adds a single element to the **end** of the list.

### Syntax

```python
list_name.append(element)
```

### Example

```python
fruits = ["Apple", "Mango"]

fruits.append("Banana")

print(fruits)
```

**Output**

```
['Apple', 'Mango', 'Banana']
```

---

## 2. extend()

The `extend()` method adds all elements from another iterable (such as a list, tuple, or set) to the end of the list.

### Syntax

```python
list_name.extend(iterable)
```

### Example

```python
fruits = ["Apple", "Mango"]

more_fruits = ["Banana", "Orange"]

fruits.extend(more_fruits)

print(fruits)
```

**Output**

```
['Apple', 'Mango', 'Banana', 'Orange']
```

---

## 3. insert()

The `insert()` method inserts an element at a specified position.

### Syntax

```python
list_name.insert(index, element)
```

### Example

```python
numbers = [10,20,40]

numbers.insert(2,30)

print(numbers)
```

**Output**

```
[10, 20, 30, 40]
```

---

## 4. remove()

The `remove()` method removes the **first occurrence** of the specified value.

### Syntax

```python
list_name.remove(value)
```

### Example

```python
fruits = ["Apple","Banana","Orange"]

fruits.remove("Banana")

print(fruits)
```

**Output**

```
['Apple', 'Orange']
```

> **Note:** If the value does not exist, Python raises a `ValueError`.

---

## 5. pop()

The `pop()` method removes and returns the element at the specified index.

If no index is provided, it removes the last element.

### Syntax

```python
list_name.pop(index)
```

### Example 1

```python
numbers = [10,20,30,40]

numbers.pop()

print(numbers)
```

**Output**

```
[10, 20, 30]
```

### Example 2

```python
numbers = [10,20,30,40]

numbers.pop(1)

print(numbers)
```

**Output**

```
[10, 30, 40]
```

---

## 6. clear()

The `clear()` method removes **all elements** from the list.

### Syntax

```python
list_name.clear()
```

### Example

```python
numbers = [10,20,30]

numbers.clear()

print(numbers)
```

**Output**

```
[]
```

---

## 7. sort()

The `sort()` method arranges elements in ascending order.

### Syntax

```python
list_name.sort()
```

### Example

```python
numbers = [50,10,40,20]

numbers.sort()

print(numbers)
```

**Output**

```
[10, 20, 40, 50]
```

### Descending Order

```python
numbers.sort(reverse=True)

print(numbers)
```

**Output**

```
[50, 40, 20, 10]
```

---

## 8. reverse()

The `reverse()` method reverses the order of the elements.

### Syntax

```python
list_name.reverse()
```

### Example

```python
numbers = [1,2,3,4]

numbers.reverse()

print(numbers)
```

**Output**

```
[4, 3, 2, 1]
```

> **Note:** `reverse()` only changes the order. It does **not** sort the list.

---

## 9. copy()

The `copy()` method creates a shallow copy of the list.

### Syntax

```python
new_list = list_name.copy()
```

### Example

```python
numbers = [10,20,30]

new_numbers = numbers.copy()

print(new_numbers)
```

**Output**

```
[10, 20, 30]
```

---

## 10. count()

The `count()` method returns how many times a particular element appears in the list.

### Syntax

```python
list_name.count(value)
```

### Example

```python
numbers = [1,2,2,3,2]

print(numbers.count(2))
```

**Output**

```
3
```

---

## 11. index()

The `index()` method returns the index of the first occurrence of an element.

### Syntax

```python
list_name.index(value)
```

### Example

```python
fruits = ["Apple","Banana","Orange"]

print(fruits.index("Banana"))
```

**Output**

```
1
```

> **Note:** If the element is not found, Python raises a `ValueError`.

---

# 📖 Summary of List Methods

| Method | Purpose |
|---------|---------|
| `append()` | Adds one element at the end |
| `extend()` | Adds multiple elements |
| `insert()` | Inserts an element at a specified position |
| `remove()` | Removes an element by value |
| `pop()` | Removes an element by index |
| `clear()` | Removes all elements |
| `sort()` | Sorts the list |
| `reverse()` | Reverses the list |
| `copy()` | Creates a copy of the list |
| `count()` | Counts occurrences of an element |
| `index()` | Returns the index of an element |

---

# ⚠️ Common Mistakes

❌ Confusing `remove()` and `pop()`

```python
numbers.remove(2)
```

Removes the **value** `2`.

```python
numbers.pop(2)
```

Removes the element at **index 2**.

---

❌ Thinking `reverse()` sorts the list.

```python
numbers = [5,1,4]

numbers.reverse()
```

Output

```
[4, 1, 5]
```

This is **not** sorted.

---

# 💡 Best Practices

- Use `append()` when adding a single item.
- Use `extend()` when adding multiple items.
- Use `sort()` only when all elements are of comparable data types.
- Use `copy()` if you want to preserve the original list.
- Avoid modifying a list while iterating over it unless necessary.


# 📦 What is a Tuple?

A **Tuple** is an ordered collection of elements, similar to a list, but it is **immutable**, meaning its elements cannot be modified after creation.

Tuples are enclosed within **parentheses `( )`** and elements are separated by commas.

### Syntax

```python
tuple_name = (item1, item2, item3)
```

### Example

```python
student = ("Sonal", 21, "CSE")

print(student)
```

**Output**

```
('Sonal', 21, 'CSE')
```

A tuple can store multiple data types.

```python
data = ("Python", 3.13, True, 100)

print(data)
```

---

# ✨ Characteristics of Tuples

- Ordered collection
- Immutable (cannot be modified)
- Allows duplicate values
- Supports indexing
- Supports slicing
- Can store different data types
- Faster than lists
- Uses less memory than lists

---

# 📝 Creating Tuples

## Multiple Element Tuple

```python
numbers = (10,20,30)
```

---

## Empty Tuple

```python
t = ()
```

---

## Single Element Tuple

```python
t = (5,)
```

> **Note:** A comma is mandatory for a single-element tuple. Without the comma, Python treats it as an integer.

Example

```python
t = (5)

print(type(t))
```

Output

```
<class 'int'>
```

Correct way

```python
t = (5,)

print(type(t))
```

Output

```
<class 'tuple'>
```

---

# 🔢 Tuple Indexing

Tuple indexing works exactly like list indexing.

Example

```python
colors = ("Red", "Green", "Blue", "Black")

print(colors[0])
print(colors[2])
```

**Output**

```
Red
Blue
```

### Negative Indexing

```python
print(colors[-1])
print(colors[-2])
```

**Output**

```
Black
Blue
```

---

# ✂️ Tuple Slicing

Tuple slicing is similar to list slicing.

### Syntax

```python
tuple_name[start:end]
```

Example

```python
numbers = (10,20,30,40,50)

print(numbers[1:4])
```

**Output**

```
(20, 30, 40)
```

---

## Slicing with Step

```python
numbers = (10,20,30,40,50,60)

print(numbers[0:6:2])
```

**Output**

```
(10, 30, 50)
```

---

# 🛠️ Tuple Methods

Unlike lists, tuples have only **two built-in methods**.

---

## 1. count()

Returns the number of occurrences of an element.

### Syntax

```python
tuple_name.count(value)
```

### Example

```python
numbers = (1,2,2,3,2)

print(numbers.count(2))
```

**Output**

```
3
```

---

## 2. index()

Returns the index of the first occurrence of an element.

### Syntax

```python
tuple_name.index(value)
```

### Example

```python
fruits = ("Apple","Banana","Orange")

print(fruits.index("Banana"))
```

**Output**

```
1
```

---

# 🔄 Tuple Operations

## Concatenation

Joins two tuples together.

```python
a = (1,2)

b = (3,4)

print(a + b)
```

**Output**

```
(1, 2, 3, 4)
```

---

## Repetition

Repeats the tuple.

```python
numbers = (1,2)

print(numbers * 3)
```

**Output**

```
(1, 2, 1, 2, 1, 2)
```

---

## Membership Operator

Checks whether an element exists.

```python
numbers = (10,20,30)

print(20 in numbers)
```

**Output**

```
True
```

---

# 📖 Built-in Functions with Tuples

## len()

Returns the number of elements.

```python
numbers = (10,20,30)

print(len(numbers))
```

Output

```
3
```

---

## min()

Returns the smallest value.

```python
numbers = (50,10,30)

print(min(numbers))
```

Output

```
10
```

---

## max()

Returns the largest value.

```python
numbers = (50,10,30)

print(max(numbers))
```

Output

```
50
```

---

## sum()

Returns the sum of numeric values.

```python
numbers = (10,20,30)

print(sum(numbers))
```

Output

```
60
```

---

## sorted()

Returns a sorted **list**.

```python
numbers = (50,10,30)

print(sorted(numbers))
```

Output

```
[10, 30, 50]
```

> **Note:** `sorted()` always returns a **list**, not a tuple.

---

## tuple()

Converts another iterable into a tuple.

```python
numbers = [10,20,30]

t = tuple(numbers)

print(t)
```

Output

```
(10, 20, 30)
```

---

# 🎁 Tuple Packing

Packing means storing multiple values into a tuple.

```python
student = "Sonal", 21, "CSE"

print(student)
```

Output

```
('Sonal', 21, 'CSE')
```

---

# 🎯 Tuple Unpacking

Unpacking means assigning tuple elements to separate variables.

```python
student = ("Sonal", 21, "CSE")

name, age, course = student

print(name)
print(age)
print(course)
```

Output

```
Sonal
21
CSE
```

---

# ⭐ Extended Unpacking

The `*` operator collects remaining values.

```python
numbers = (10,20,30,40,50)

a, b, *c = numbers

print(a)
print(b)
print(c)
```

Output

```
10
20
[30, 40, 50]
```

---

# 💡 Why Use Tuples?

Tuples are useful when:

- Data should never change.
- Better performance is required.
- Less memory usage is preferred.
- Storing fixed information.

### Real-Life Examples

- RGB color values
- GPS Coordinates
- Days of the week
- Months of the year
- Database records
- Student roll numbers
- Employee IDs

---

# ⚠️ Common Mistakes

❌ Trying to modify a tuple.

```python
numbers = (1,2,3)

numbers[0] = 10
```

This produces a **TypeError** because tuples are immutable.

---

❌ Forgetting the comma in a single-element tuple.

```python
t = (5)
```

This creates an integer, **not** a tuple.

Correct:

```python
t = (5,)
```

---

# 💡 Best Practices

- Use tuples for fixed data.
- Use lists when data changes frequently.
- Prefer tuples for constant values such as coordinates and records.
- Use unpacking to write cleaner and more readable code.

---

# 📊 Difference Between List & Tuple

| Feature | List | Tuple |
|---------|------|-------|
| Syntax | `[]` | `()` |
| Mutability | Mutable | Immutable |
| Modification | Allowed | Not Allowed |
| Methods | Many built-in methods | Only `count()` and `index()` |
| Performance | Slightly slower | Faster |
| Memory Usage | More | Less |
| Use Case | Frequently changing data | Fixed data |
| Hashable | No | Yes (if elements are immutable) |

---

# 🤝 Similarities Between List & Tuple

Although lists and tuples have some differences, they also share many similarities.

- Both are ordered collections.
- Both can store multiple values.
- Both allow duplicate elements.
- Both support indexing.
- Both support negative indexing.
- Both support slicing.
- Both can contain different data types.
- Both can be nested.
- Both can be iterated using loops.
- Both support membership operators (`in` and `not in`).

---

# 💡 When to Use What?

## ✅ Use a List When:

- Data changes frequently.
- You need to add or remove elements.
- You need sorting operations.
- The number of elements is dynamic.
- Building applications like shopping carts, playlists, and to-do lists.

### Example

```python
shopping_cart = ["Milk", "Bread"]

shopping_cart.append("Butter")
```

---

## ✅ Use a Tuple When:

- Data should remain constant.
- Better performance is required.
- Less memory consumption is preferred.
- Prevent accidental modification.
- Storing coordinates, IDs, or configuration values.

### Example

```python
location = (28.6139, 77.2090)
```

---

# 📌 Real-Life Applications

## Lists

Lists are commonly used in:

- Shopping Cart
- Student Record System
- Contact List
- Playlist
- Attendance Management
- To-do Applications
- Product Inventory
- Social Media Posts

---

## Tuples

Tuples are commonly used in:

- GPS Coordinates
- RGB Color Values
- Employee IDs
- Database Records
- Mathematical Coordinates
- Months of the Year
- Days of the Week
- Fixed Configuration Settings

---

# ⚠️ Common Mistakes

### ❌ Trying to modify a tuple

```python
t = (10,20,30)

t[0] = 100
```

This results in:

```
TypeError
```

---

### ❌ Forgetting comma in a single-element tuple

Incorrect

```python
t = (5)
```

Correct

```python
t = (5,)
```

---

### ❌ Confusing remove() and pop()

```python
numbers.remove(2)
```

Removes the **value** `2`.

```python
numbers.pop(2)
```

Removes the element at **index 2**.

---

### ❌ Thinking reverse() sorts a list

```python
numbers = [5,1,4]

numbers.reverse()
```

Output

```
[4,1,5]
```

This is **not sorted**.

---

# 💡 Best Practices

- Use meaningful variable names.
- Choose **Lists** for mutable data.
- Choose **Tuples** for immutable data.
- Avoid modifying a list while iterating over it.
- Use tuple unpacking for cleaner code.
- Keep related data together in a single collection.
- Prefer built-in methods instead of writing unnecessary loops.

---

# ⚡ Quick Revision Table

| Topic | List | Tuple |
|------|------|------|
| Mutable | ✅ Yes | ❌ No |
| Ordered | ✅ Yes | ✅ Yes |
| Duplicate Values | ✅ Yes | ✅ Yes |
| Indexing | ✅ Yes | ✅ Yes |
| Slicing | ✅ Yes | ✅ Yes |
| Add Elements | ✅ Yes | ❌ No |
| Remove Elements | ✅ Yes | ❌ No |
| Performance | Good | Better |
| Memory Usage | Higher | Lower |
| Best For | Dynamic Data | Fixed Data |

---

# 📖 Important Methods & Functions

## List Methods

```python
append()
extend()
insert()
remove()
pop()
clear()
sort()
reverse()
copy()
count()
index()
```

---

## Tuple Methods

```python
count()
index()
```

---

## Useful Built-in Functions

```python
len()
min()
max()
sum()
sorted()
tuple()
```

---

# ⭐ Key Takeaways

- Lists are mutable whereas tuples are immutable.
- Both support indexing and slicing.
- Lists provide many built-in methods.
- Tuples have only two built-in methods.
- Tuples are generally faster and consume less memory.
- Lists are ideal for data that changes frequently.
- Tuples are ideal for storing fixed information.
- Built-in methods simplify data manipulation.
- Choosing the right data structure improves program efficiency.

---

# 🚀 Summary

In this chapter, I learned:

- ✅ What are Lists
- ✅ Creating Lists
- ✅ Characteristics of Lists
- ✅ List Indexing
- ✅ List Slicing
- ✅ Nested Lists
- ✅ Modifying Lists
- ✅ List Methods
- ✅ What are Tuples
- ✅ Creating Tuples
- ✅ Characteristics of Tuples
- ✅ Tuple Indexing
- ✅ Tuple Slicing
- ✅ Tuple Methods
- ✅ Tuple Operations
- ✅ Tuple Packing & Unpacking
- ✅ Extended Unpacking
- ✅ Built-in Functions
- ✅ Difference Between Lists & Tuples
- ✅ Similarities Between Lists & Tuples
- ✅ Real-Life Applications
- ✅ Common Mistakes
- ✅ Best Practices

This chapter helped me understand how Python stores collections of data using **Lists** and **Tuples**. I learned how to choose the right data structure based on whether the data needs to be modified or remain constant. Mastering these concepts is essential for writing efficient and organized Python programs.

---

## 📚 Course Information

**Course:** CodeWithHarry Python Course

**Chapter:** 04 - Lists & Tuples

**Language:** Python

**Author:** Sonal Rai