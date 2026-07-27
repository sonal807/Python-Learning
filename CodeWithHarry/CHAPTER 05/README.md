# 📘 Chapter 05 - Dictionaries & Sets

## 🎯 Objective

The objective of this chapter is to understand **Dictionaries** and **Sets**, two powerful built-in data structures in Python.

In this chapter, I learned how to store data using **key-value pairs** with dictionaries and how to work with **unique collections of elements** using sets. I also learned how to access, modify, add, remove, and organize data efficiently using various built-in methods.

By the end of this chapter, I understood when to use a **Dictionary** and when a **Set** is the better choice.

---

# 📚 Topics Covered

- Dictionaries
- Creating Dictionaries
- Characteristics of Dictionaries
- Accessing Dictionary Values
- Adding Elements
- Updating Elements
- Removing Elements
- Nested Dictionaries
- Dictionary Methods
- Sets
- Creating Sets
- Characteristics of Sets
- Set Methods
- Set Operations
- Difference Between Dictionaries & Sets

---

# 📖 What is a Dictionary?

A **Dictionary** is a built-in Python data structure that stores data in the form of **key-value pairs**.

Each key in a dictionary is unique and is used to access its corresponding value.

Dictionaries are enclosed within **curly braces `{}`**.

### Syntax

```python
dictionary_name = {
    "key1": value1,
    "key2": value2
}
```

### Example

```python
student = {
    "name": "Sonal",
    "age": 21,
    "course": "B.Tech"
}

print(student)
```

**Output**

```
{'name': 'Sonal', 'age': 21, 'course': 'B.Tech'}
```

---

# ✨ Characteristics of Dictionaries

- Stores data as key-value pairs.
- Keys must be unique.
- Values can be duplicated.
- Dictionaries are mutable.
- Supports nested dictionaries.
- Dynamic in size.
- Fast searching using keys.
- Maintains insertion order (Python 3.7+).

---

# 🔑 Creating Dictionaries

### Dictionary with Multiple Elements

```python
student = {
    "name": "Rahul",
    "age": 20,
    "city": "Lucknow"
}
```

---

### Empty Dictionary

```python
student = {}
```

---

### Dictionary with Different Data Types

```python
person = {
    "name": "Sonal",
    "age": 21,
    "marks": 89.5,
    "passed": True
}

print(person)
```

---

# 🔍 Accessing Dictionary Values

Dictionary values are accessed using their keys.

### Using Square Brackets

```python
student = {
    "name": "Sonal",
    "age": 21
}

print(student["name"])
```

**Output**

```
Sonal
```

---

### Using get()

```python
student = {
    "name": "Sonal",
    "age": 21
}

print(student.get("age"))
```

**Output**

```
21
```

> **Note:** If the key does not exist, `get()` returns `None` instead of raising an error.

Example

```python
print(student.get("city"))
```

Output

```
None
```

---

# ➕ Adding New Elements

New key-value pairs can be added simply by assigning a new key.

Example

```python
student = {
    "name": "Sonal",
    "age": 21
}

student["city"] = "Lucknow"

print(student)
```

**Output**

```
{'name': 'Sonal', 'age': 21, 'city': 'Lucknow'}
```

---

# ✏️ Updating Existing Values

Existing values can be updated by assigning a new value to the same key.

Example

```python
student = {
    "name": "Sonal",
    "age": 21
}

student["age"] = 22

print(student)
```

**Output**

```
{'name': 'Sonal', 'age': 22}
```

---

# ❌ Removing Elements

Dictionary elements can be removed using methods like `pop()`, `popitem()`, or `clear()`. These methods will be discussed in detail later.

Example

```python
student = {
    "name": "Sonal",
    "age": 21
}

student.pop("age")

print(student)
```

**Output**

```
{'name': 'Sonal'}
```

---

# 🪺 Nested Dictionaries

A dictionary can contain another dictionary as its value. This is called a **Nested Dictionary**.

Example

```python
students = {
    "student1": {
        "name": "Rahul",
        "age": 20
    },
    "student2": {
        "name": "Sonal",
        "age": 21
    }
}

print(students["student2"]["name"])
```

**Output**

```
Sonal
```

Nested dictionaries are useful for storing structured data like student records, employee details, and user profiles.

---

# 🌍 Why Use Dictionaries?

Dictionaries are useful when:

- Data has a unique identifier.
- Fast searching is required.
- Information is stored as key-value pairs.
- Data needs to be updated frequently.
- Complex structured data needs to be stored.

### Real-Life Examples

- Student records
- Employee database
- Contact list
- User profiles
- Product details
- Online shopping cart
- Language translation dictionary
- JSON data

# 🛠️ Dictionary Methods

Python provides several built-in methods to perform different operations on dictionaries. These methods make it easy to access, update, copy, and manipulate dictionary data efficiently.

---

## 1. keys()

The `keys()` method returns a **view object** containing all the keys in the dictionary.

### Syntax

```python
dictionary_name.keys()
```

### Example

```python
student = {
    "name": "Sonal",
    "age": 21,
    "course": "B.Tech"
}

print(student.keys())
```

**Output**

```
dict_keys(['name', 'age', 'course'])
```

---

## 2. values()

The `values()` method returns a view object containing all the values in the dictionary.

### Syntax

```python
dictionary_name.values()
```

### Example

```python
student = {
    "name": "Sonal",
    "age": 21,
    "course": "B.Tech"
}

print(student.values())
```

**Output**

```
dict_values(['Sonal', 21, 'B.Tech'])
```

---

## 3. items()

The `items()` method returns both keys and values as tuples.

### Syntax

```python
dictionary_name.items()
```

### Example

```python
student = {
    "name": "Sonal",
    "age": 21
}

print(student.items())
```

**Output**

```
dict_items([('name', 'Sonal'), ('age', 21)])
```

---

## 4. get()

The `get()` method returns the value associated with a specified key.

If the key does not exist, it returns `None` instead of raising an error.

### Syntax

```python
dictionary_name.get(key)
```

### Example

```python
student = {
    "name": "Sonal",
    "age": 21
}

print(student.get("age"))
```

**Output**

```
21
```

Example with a missing key

```python
print(student.get("city"))
```

**Output**

```
None
```

---

## 5. update()

The `update()` method adds new key-value pairs or updates existing ones.

### Syntax

```python
dictionary_name.update(other_dictionary)
```

### Example

```python
student = {
    "name": "Sonal",
    "age": 21
}

student.update({"city": "Lucknow"})

print(student)
```

**Output**

```
{'name': 'Sonal', 'age': 21, 'city': 'Lucknow'}
```

Updating an existing value

```python
student.update({"age": 22})

print(student)
```

**Output**

```
{'name': 'Sonal', 'age': 22, 'city': 'Lucknow'}
```

---

## 6. pop()

The `pop()` method removes the specified key and returns its value.

### Syntax

```python
dictionary_name.pop(key)
```

### Example

```python
student = {
    "name": "Sonal",
    "age": 21
}

removed = student.pop("age")

print(removed)
print(student)
```

**Output**

```
21
{'name': 'Sonal'}
```

> **Note:** If the key does not exist, Python raises a `KeyError`.

---

## 7. popitem()

The `popitem()` method removes and returns the **last inserted key-value pair**.

### Syntax

```python
dictionary_name.popitem()
```

### Example

```python
student = {
    "name": "Sonal",
    "age": 21,
    "city": "Lucknow"
}

print(student.popitem())
```

**Output**

```
('city', 'Lucknow')
```

---

## 8. clear()

The `clear()` method removes all items from the dictionary.

### Syntax

```python
dictionary_name.clear()
```

### Example

```python
student = {
    "name": "Sonal",
    "age": 21
}

student.clear()

print(student)
```

**Output**

```
{}
```

---

## 9. copy()

The `copy()` method creates a shallow copy of the dictionary.

### Syntax

```python
new_dictionary = dictionary_name.copy()
```

### Example

```python
student = {
    "name": "Sonal",
    "age": 21
}

new_student = student.copy()

print(new_student)
```

**Output**

```
{'name': 'Sonal', 'age': 21}
```

---

## 10. fromkeys()

The `fromkeys()` method creates a new dictionary with specified keys and a common value.

### Syntax

```python
dict.fromkeys(keys, value)
```

### Example

```python
keys = ["name", "age", "city"]

student = dict.fromkeys(keys, "Not Available")

print(student)
```

**Output**

```
{'name': 'Not Available', 'age': 'Not Available', 'city': 'Not Available'}
```

---

## 11. setdefault()

The `setdefault()` method returns the value of a key.

If the key does not exist, it inserts the key with the specified default value.

### Syntax

```python
dictionary_name.setdefault(key, default_value)
```

### Example

```python
student = {
    "name": "Sonal"
}

student.setdefault("age", 21)

print(student)
```

**Output**

```
{'name': 'Sonal', 'age': 21}
```

---

# 📖 Summary of Dictionary Methods

| Method | Purpose |
|---------|---------|
| `keys()` | Returns all keys |
| `values()` | Returns all values |
| `items()` | Returns all key-value pairs |
| `get()` | Returns the value of a key safely |
| `update()` | Adds or updates key-value pairs |
| `pop()` | Removes a key and returns its value |
| `popitem()` | Removes the last inserted item |
| `clear()` | Removes all items |
| `copy()` | Creates a copy of the dictionary |
| `fromkeys()` | Creates a new dictionary from keys |
| `setdefault()` | Returns or inserts a default value |

---

# ⚠️ Common Mistakes

❌ Accessing a non-existing key using square brackets.

```python
student["city"]
```

This raises a **KeyError**.

Instead, use:

```python
student.get("city")
```

---

❌ Thinking `update()` only adds new keys.

It can also update existing values.

---

❌ Assuming dictionaries allow duplicate keys.

```python
student = {
    "name": "Rahul",
    "name": "Sonal"
}
```

Output

```
{'name': 'Sonal'}
```

The second value replaces the first one.

---

# 💡 Best Practices

- Use meaningful and descriptive keys.
- Use `get()` when you're unsure if a key exists.
- Avoid duplicate keys in a dictionary.
- Use nested dictionaries for structured data.
- Use `copy()` if you want to preserve the original dictionary before making changes.


# 📦 What is a Set?

A **Set** is a built-in Python data structure used to store **multiple unique elements** in a single variable.

Unlike lists and tuples, sets **do not maintain the insertion order** (from a conceptual standpoint for beginners) and **do not allow duplicate values**.

Sets are mainly used when uniqueness of elements is important.

Sets are enclosed within **curly braces `{}`**.

### Syntax

```python
set_name = {item1, item2, item3}
```

### Example

```python
fruits = {"Apple", "Banana", "Orange"}

print(fruits)
```

**Output**

```
{'Apple', 'Banana', 'Orange'}
```

---

# ✨ Characteristics of Sets

- Stores only unique elements.
- Duplicate values are automatically removed.
- Mutable (elements can be added or removed).
- Unordered collection.
- Does not support indexing.
- Does not support slicing.
- Can store different immutable data types.
- Very fast for searching elements.

---

# 📝 Creating Sets

### Set with Multiple Elements

```python
numbers = {10, 20, 30, 40}

print(numbers)
```

---

### Empty Set

An empty set **cannot** be created using `{}`.

```python
empty_set = set()

print(type(empty_set))
```

**Output**

```
<class 'set'>
```

---

### Empty Dictionary vs Empty Set

```python
a = {}
b = set()

print(type(a))
print(type(b))
```

**Output**

```
<class 'dict'>
<class 'set'>
```

> **Note:** `{}` creates an **empty dictionary**, not an empty set.

---

# 🔄 Duplicate Elements

Sets automatically remove duplicate values.

Example

```python
numbers = {1,2,3,2,1,4,5}

print(numbers)
```

**Output**

```
{1,2,3,4,5}
```

---

# ➕ Adding Elements

New elements can be added using the `add()` method.

Example

```python
fruits = {"Apple", "Banana"}

fruits.add("Orange")

print(fruits)
```

---

# ✏️ Updating a Set

Multiple elements can be added using the `update()` method.

Example

```python
numbers = {1,2,3}

numbers.update([4,5,6])

print(numbers)
```

---

# ❌ Removing Elements

Elements can be removed using methods like:

- `remove()`
- `discard()`
- `pop()`
- `clear()`

These methods will be discussed in detail in the next section.

Example

```python
numbers = {10,20,30}

numbers.remove(20)

print(numbers)
```

---

# 🚫 Set Indexing

Sets do **not** support indexing because they are unordered.

Example

```python
numbers = {10,20,30}

print(numbers[0])
```

**Output**

```
TypeError
```

---

# 🚫 Set Slicing

Sets also do **not** support slicing.

Example

```python
numbers = {10,20,30,40}

print(numbers[1:3])
```

**Output**

```
TypeError
```

---

# 🤝 Set Operations

Python provides powerful mathematical operations on sets.

The most common operations are:

- Union
- Intersection
- Difference
- Symmetric Difference

These operations are explained in detail later.

---

# 🌍 Why Use Sets?

Sets are useful when:

- Duplicate values should not be stored.
- Fast searching is required.
- Mathematical set operations need to be performed.
- Checking membership efficiently.
- Removing duplicate elements from a collection.

---

# 📌 Real-Life Applications

Sets are commonly used in:

- Removing duplicate values from a list.
- Finding common friends on social media.
- Student attendance systems.
- Searching unique products.
- Tags in blogging platforms.
- Unique visitor tracking.
- Permission management.
- Database operations involving unique records.

---

# ⚠️ Common Mistakes

### ❌ Creating an empty set using `{}`

```python
data = {}
```

This creates a **dictionary**, not a set.

Correct way

```python
data = set()
```

---

### ❌ Trying to access elements using indexing

```python
numbers = {1,2,3}

print(numbers[0])
```

This raises a **TypeError**.

---

### ❌ Expecting duplicate values to be stored

```python
numbers = {1,2,2,3,3}

print(numbers)
```

Output

```
{1,2,3}
```

Duplicates are removed automatically.

---

# 💡 Best Practices

- Use sets when duplicate values are not required.
- Use sets for fast membership testing.
- Use meaningful variable names.
- Use mathematical set operations whenever possible instead of writing lengthy loops.
- Use `set()` to remove duplicates from a list.

Example

```python
numbers = [1,2,2,3,4,4,5]

unique_numbers = list(set(numbers))

print(unique_numbers)
```

# 🛠️ Set Methods

Python provides several built-in methods to perform different operations on sets. These methods help in adding, removing, copying, and performing mathematical operations on sets efficiently.

---

## 1. add()

The `add()` method adds a single element to the set.

### Syntax

```python
set_name.add(element)
```

### Example

```python
fruits = {"Apple", "Banana"}

fruits.add("Orange")

print(fruits)
```

**Output**

```
{'Apple', 'Banana', 'Orange'}
```

> **Note:** If the element already exists, it will not be added again.

---

## 2. update()

The `update()` method adds multiple elements from another iterable such as a list, tuple, or another set.

### Syntax

```python
set_name.update(iterable)
```

### Example

```python
numbers = {1,2,3}

numbers.update([4,5,6])

print(numbers)
```

**Output**

```
{1,2,3,4,5,6}
```

---

## 3. remove()

The `remove()` method removes the specified element from the set.

### Syntax

```python
set_name.remove(element)
```

### Example

```python
numbers = {10,20,30}

numbers.remove(20)

print(numbers)
```

**Output**

```
{10,30}
```

> **Note:** If the element does not exist, Python raises a `KeyError`.

---

## 4. discard()

The `discard()` method removes the specified element.

Unlike `remove()`, it does **not** raise an error if the element is not found.

### Syntax

```python
set_name.discard(element)
```

### Example

```python
numbers = {10,20,30}

numbers.discard(40)

print(numbers)
```

**Output**

```
{10,20,30}
```

---

## 5. pop()

The `pop()` method removes and returns a random element from the set.

### Syntax

```python
set_name.pop()
```

### Example

```python
numbers = {10,20,30}

removed = numbers.pop()

print(removed)
print(numbers)
```

> **Note:** Since sets are unordered, the removed element may vary.

---

## 6. clear()

The `clear()` method removes all elements from the set.

### Syntax

```python
set_name.clear()
```

### Example

```python
numbers = {1,2,3}

numbers.clear()

print(numbers)
```

**Output**

```
set()
```

---

## 7. copy()

The `copy()` method creates a shallow copy of the set.

### Syntax

```python
new_set = set_name.copy()
```

### Example

```python
numbers = {1,2,3}

new_numbers = numbers.copy()

print(new_numbers)
```

**Output**

```
{1,2,3}
```

---

## 8. union()

The `union()` method combines two or more sets and returns a new set containing all unique elements.

### Syntax

```python
set1.union(set2)
```

### Example

```python
A = {1,2,3}
B = {3,4,5}

print(A.union(B))
```

**Output**

```
{1,2,3,4,5}
```

---

## 9. intersection()

The `intersection()` method returns the common elements present in both sets.

### Syntax

```python
set1.intersection(set2)
```

### Example

```python
A = {1,2,3}
B = {2,3,4}

print(A.intersection(B))
```

**Output**

```
{2,3}
```

---

## 10. difference()

The `difference()` method returns the elements that are present in the first set but not in the second set.

### Syntax

```python
set1.difference(set2)
```

### Example

```python
A = {1,2,3,4}
B = {3,4,5}

print(A.difference(B))
```

**Output**

```
{1,2}
```

---

## 11. symmetric_difference()

The `symmetric_difference()` method returns elements that are present in either set but **not in both**.

### Syntax

```python
set1.symmetric_difference(set2)
```

### Example

```python
A = {1,2,3}
B = {3,4,5}

print(A.symmetric_difference(B))
```

**Output**

```
{1,2,4,5}
```

---

## 12. issubset()

Checks whether all elements of one set are present in another set.

### Syntax

```python
set1.issubset(set2)
```

### Example

```python
A = {1,2}
B = {1,2,3,4}

print(A.issubset(B))
```

**Output**

```
True
```

---

## 13. issuperset()

Checks whether a set contains all elements of another set.

### Syntax

```python
set1.issuperset(set2)
```

### Example

```python
A = {1,2,3,4}
B = {1,2}

print(A.issuperset(B))
```

**Output**

```
True
```

---

## 14. isdisjoint()

Returns `True` if two sets have no common elements.

### Syntax

```python
set1.isdisjoint(set2)
```

### Example

```python
A = {1,2}
B = {3,4}

print(A.isdisjoint(B))
```

**Output**

```
True
```

---

# 📖 Summary of Set Methods

| Method | Purpose |
|---------|---------|
| `add()` | Adds one element |
| `update()` | Adds multiple elements |
| `remove()` | Removes an element (raises error if not found) |
| `discard()` | Removes an element safely |
| `pop()` | Removes a random element |
| `clear()` | Removes all elements |
| `copy()` | Creates a copy of the set |
| `union()` | Combines two sets |
| `intersection()` | Returns common elements |
| `difference()` | Returns unique elements of the first set |
| `symmetric_difference()` | Returns non-common elements |
| `issubset()` | Checks subset relationship |
| `issuperset()` | Checks superset relationship |
| `isdisjoint()` | Checks whether two sets have no common elements |

---

# ⚠️ Common Mistakes

### ❌ Using `remove()` for a missing element

```python
numbers.remove(100)
```

Raises a **KeyError**.

Instead, use:

```python
numbers.discard(100)
```

---

### ❌ Assuming `pop()` removes the first element

Sets are unordered, so `pop()` removes an arbitrary element.

---

### ❌ Expecting `union()` to modify the original set

```python
C = A.union(B)
```

`union()` returns a **new set**. It does not change `A`.

---

# 💡 Best Practices

- Use `discard()` when you're unsure whether an element exists.
- Use `union()` and `intersection()` instead of writing loops for set operations.
- Use `issubset()` and `issuperset()` to compare sets efficiently.
- Keep set elements immutable (such as integers, strings, and tuples).
- Use meaningful variable names like `students`, `employees`, or `permissions` instead of `a` and `b`.

# 📊 Difference Between Dictionary & Set

| Feature | Dictionary | Set |
|---------|------------|-----|
| Syntax | `{key: value}` | `{value1, value2}` |
| Stores | Key-Value Pairs | Unique Values |
| Duplicate Values | Keys must be unique, values can be duplicated | Duplicate values are not allowed |
| Access | Using keys | No indexing or keys |
| Mutable | ✅ Yes | ✅ Yes |
| Ordered | Maintains insertion order (Python 3.7+) | Unordered collection |
| Indexing | ❌ No | ❌ No |
| Slicing | ❌ No | ❌ No |
| Best Use | Structured data | Unique collections and mathematical operations |

---

# 📊 Difference Between List, Tuple, Dictionary & Set

| Feature | List | Tuple | Dictionary | Set |
|---------|------|-------|------------|-----|
| Syntax | `[]` | `()` | `{key: value}` | `{}` |
| Ordered | ✅ Yes | ✅ Yes | ✅ Yes | ❌ No |
| Mutable | ✅ Yes | ❌ No | ✅ Yes | ✅ Yes |
| Duplicate Elements | ✅ Allowed | ✅ Allowed | Keys ❌, Values ✅ | ❌ Not Allowed |
| Indexing | ✅ Yes | ✅ Yes | ❌ No | ❌ No |
| Slicing | ✅ Yes | ✅ Yes | ❌ No | ❌ No |
| Key-Value Pair | ❌ No | ❌ No | ✅ Yes | ❌ No |
| Best For | Dynamic Data | Fixed Data | Structured Data | Unique Data |

---

# 🤝 Similarities Between Dictionary & Set

Although dictionaries and sets are different data structures, they share some common features.

- Both are mutable.
- Both use curly braces `{}`.
- Both can grow dynamically.
- Both provide fast searching.
- Both are built-in Python data structures.
- Both support iteration using loops.
- Both can be modified after creation.

---

# 💡 When to Use What?

## ✅ Use a Dictionary When:

- Data is stored as **key-value pairs**.
- Fast lookup using a unique key is required.
- You need to represent structured information.
- Values need to be updated frequently.

### Example

```python
student = {
    "name": "Sonal",
    "age": 21,
    "course": "B.Tech"
}
```

---

## ✅ Use a Set When:

- Duplicate values should not be stored.
- Fast membership checking is required.
- Mathematical set operations are needed.
- You only care about unique values.

### Example

```python
languages = {"Python", "Java", "C++"}
```

---

# 🌍 Real-Life Applications

## Dictionary

- Student Information System
- Employee Database
- Contact List
- Product Catalog
- User Profiles
- JSON Data
- Online Shopping Websites
- Language Translation

---

## Set

- Removing duplicate values
- Attendance System
- Friend Suggestions
- Unique Visitor Tracking
- Search Engines
- Permission Management
- Mathematical Calculations
- Database Operations

---

# 📖 Important Dictionary Methods

```python
keys()
values()
items()
get()
update()
pop()
popitem()
clear()
copy()
fromkeys()
setdefault()
```

---

# 📖 Important Set Methods

```python
add()
update()
remove()
discard()
pop()
clear()
copy()
union()
intersection()
difference()
symmetric_difference()
issubset()
issuperset()
isdisjoint()
```

---

# ⭐ Key Takeaways

- Dictionaries store data as **key-value pairs**.
- Dictionary keys must be unique.
- Sets store only unique elements.
- Dictionaries are ideal for structured data.
- Sets are ideal for unique collections.
- Both dictionaries and sets are mutable.
- Sets do not support indexing or slicing.
- Dictionaries allow fast access using keys.
- Set operations simplify mathematical operations.
- Choosing the appropriate data structure improves code readability and efficiency.

---

# 🚀 Summary

In this chapter, I learned:

- ✅ Dictionaries
- ✅ Creating Dictionaries
- ✅ Dictionary Characteristics
- ✅ Accessing Dictionary Values
- ✅ Adding and Updating Elements
- ✅ Removing Elements
- ✅ Nested Dictionaries
- ✅ Dictionary Methods
- ✅ Sets
- ✅ Creating Sets
- ✅ Set Characteristics
- ✅ Empty Set vs Empty Dictionary
- ✅ Set Operations
- ✅ Set Methods
- ✅ Difference Between Dictionary & Set
- ✅ Difference Between List, Tuple, Dictionary & Set
- ✅ Similarities
- ✅ Real-Life Applications
- ✅ Best Practices
- ✅ Common Mistakes

This chapter helped me understand two powerful Python data structures: **Dictionaries** and **Sets**. I learned how dictionaries efficiently organize data using key-value pairs and how sets automatically manage unique elements while supporting mathematical operations. These concepts are fundamental for writing clean, efficient, and organized Python programs.

---

## 📚 Course Information

**Course:** CodeWithHarry Python Course

**Chapter:** 05 - Dictionaries & Sets

**Language:** Python

**Author:** Sonal Rai