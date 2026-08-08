# 📘 Chapter 09 - File Input/Output (File I/O)

## 🎯 Objective

The objective of this chapter is to understand how Python programs can **create, open, read, write, append, and manage files**.

Until now, most of the data used in Python programs was stored temporarily in variables. File handling allows us to store information **permanently** so that it can be used even after the program has stopped running.

In this chapter, we will learn the fundamentals of **File Input/Output (File I/O)** and gradually move towards practical file-handling operations.

---

# 📌 Topics Covered

- What is File I/O?
- Why Do We Need File Handling?
- Advantages of File Handling
- Types of Files
  - Text Files
  - Binary Files
- File Paths
  - Relative Path
  - Absolute Path
  - Windows Paths
  - Raw Strings
- Current Working Directory
- `open()` Function
- File Modes
- Reading Files
- Writing Files
- Appending Data
- Creating Files
- Closing Files
- `with` Statement
- File Pointer
- `tell()`
- `seek()`
- Encoding
- File Modification
- Deleting Files
- `os` Module
- `pathlib`
- File-related Exceptions
- Exception Handling
- Practical File Handling Programs
- Best Practices
- Common Beginner Mistakes
- Quick Revision Tables

---

# 📂 What is File I/O?

**File I/O** stands for **File Input/Output**.

It refers to the process of reading data from files and writing data into files using a Python program.

There are two basic operations:

### 📥 Input

Input means **taking data from a file into the Python program**.

```text
File
  ↓
Python Program
```

For example:

```python
with open("notes.txt", "r") as f:
    data = f.read()

print(data)
```

Here, data is being read from the file and brought into the Python program.

---

### 📤 Output

Output means **sending data from the Python program into a file**.

```text
Python Program
  ↓
File
```

For example:

```python
with open("notes.txt", "w") as f:
    f.write("Learning Python File I/O")
```

Here, the Python program writes information into the file.

---

# ❓ Why Do We Need File Handling?

Variables are useful for storing data while a program is running.

For example:

```python
name = "Rahul"
age = 21
```

The values are stored temporarily in memory.

Once the program finishes, we cannot rely on those variables to keep our data permanently.

If we want to preserve information, we can store it in a file.

Example:

```python
name = "Rahul"
age = 21

with open("student.txt", "w") as f:
    f.write(f"Name: {name}\n")
    f.write(f"Age: {age}")
```

Now the information is stored in:

```text
student.txt
```

The data remains available even after the Python program terminates.

---

## 🧠 Temporary Data vs Permanent Data

### Using Variables

```python
name = "Rahul"
```

The data exists in memory while the program is running.

```text
Program Starts
      ↓
   Variable
      ↓
     Data
      ↓
Program Ends
      ↓
Temporary data is lost
```

---

### Using Files

```python
with open("student.txt", "w") as f:
    f.write("Rahul")
```

The data is stored in a file.

```text
Program Starts
      ↓
     Data
      ↓
     File
      ↓
Program Ends
      ↓
Data remains stored
```

---

# ⭐ Advantages of File Handling

File handling provides several important advantages.

### 1. 💾 Permanent Storage

Data stored in a file remains available even after the program terminates.

### 2. 📦 Large Data Storage

Files can store a large amount of information.

### 3. 🔄 Data Retrieval

A program can retrieve previously stored information whenever required.

### 4. 📤 Data Sharing

Files can be used to transfer information between different programs.

### 5. 📝 Data Organization

Related information can be stored together in files.

### 6. 💾 Backup

Important information can be stored for future use.

### 7. 📊 Data Processing

Python can read data from files, process it, and store the result.

---

# 🌍 Real-Life Applications of File Handling

File handling is used in many real-world applications.

### 🎓 Student Management Systems

Student information can be stored in files:

```text
Name
Roll Number
Course
Marks
Attendance
```

### 📝 Notes Applications

A notes application can store:

```text
Tasks
Ideas
Study Notes
Reminders
```

### 🎮 Games

Games can store:

```text
Player Score
Game Progress
Settings
Saved Data
```

### 📊 Data Processing

Python programs can read and process data stored in:

```text
.txt
.csv
.json
```

### 🤖 Artificial Intelligence and Machine Learning

Files can contain:

- Datasets
- Training data
- Text data
- Configuration information
- Results

### 🌐 Applications and Websites

Files can be used for:

- Logs
- Configuration
- Uploaded information
- Static data

---

# 📄 Types of Files

Files can broadly be divided into two major categories:

1. **Text Files**
2. **Binary Files**

---

## 1️⃣ Text Files

Text files contain information in the form of readable characters.

Examples include:

```text
.txt
.csv
.py
.html
.css
.json
.xml
```

For example, a file called:

```text
notes.txt
```

may contain:

```text
Python File Handling
Reading and Writing Files
Practice makes programming better.
```

Text files can generally be opened and understood by humans.

Python normally works with text files using **text mode**.

---

## 📝 Example of a Text File

Suppose `notes.txt` contains:

```text
Python File Handling
Reading and Writing Files
```

Python can read the contents:

```python
with open("notes.txt", "r") as f:
    data = f.read()

print(data)
```

### Output

```text
Python File Handling
Reading and Writing Files
```

---

## 2️⃣ Binary Files

Binary files store information in the form of **bytes** rather than ordinary readable characters.

Examples include:

```text
.jpg
.png
.mp3
.mp4
.pdf
.exe
.zip
```

Binary files are generally not directly readable as normal text.

They are handled using **binary mode**.

Example:

```python
with open("photo.jpg", "rb") as f:
    data = f.read()
```

Here:

```text
r → Read
b → Binary
```

Therefore:

```python
"rb"
```

means:

> Open the file for reading in binary mode.

---

## 📊 Text File vs Binary File

| Feature | Text File | Binary File |
|---|---|---|
| Data | Characters / Text | Bytes |
| Human Readable | Usually Yes | Usually No |
| Examples | `.txt`, `.csv`, `.py` | `.jpg`, `.mp3`, `.mp4` |
| Common Modes | `r`, `w`, `a` | `rb`, `wb`, `ab` |
| Encoding | Used to interpret text | Not treated as ordinary text |
| Common Usage | Documents and text data | Images, audio, video, etc. |

---

# 📍 File Paths

A **file path** tells Python where a file or folder is located on the computer.

For example:

```text
Documents/notes.txt
```

A path can be:

- Relative to the current directory
- The complete location of the file

The two important types are:

1. **Relative Path**
2. **Absolute Path**

---

## 🔹 Relative Path

A relative path specifies the location of a file **relative to the Current Working Directory**.

Example:

```python
open("notes.txt", "r")
```

Python searches for:

```text
notes.txt
```

inside the current working directory.

---

## 📂 Relative Path with a Folder

Suppose the project structure is:

```text
Project
│
├── main.py
│
└── data
    └── students.txt
```

We can access the file using:

```python
open("data/students.txt", "r")
```

Here:

```text
data/students.txt
```

is a relative path.

---

## 🔹 Absolute Path

An absolute path provides the **complete location** of a file.

Example:

```python
open(r"D:\Projects\Python\data\students.txt", "r")
```

The complete location is specified, so Python does not have to determine the location relative to the current directory.

---

## 📊 Relative Path vs Absolute Path

| Feature | Relative Path | Absolute Path |
|---|---|---|
| Location | Relative to current directory | Complete location |
| Length | Usually shorter | Usually longer |
| Example | `notes.txt` | `D:\Projects\Python\notes.txt` |
| Depends on CWD | Yes | No |
| Portability | Usually better | Often machine-specific |

---

# 🪟 Windows Paths

Windows commonly uses a backslash `\` when specifying paths.

Example:

```text
D:\Projects\Python\notes.txt
```

However, backslashes also have a special meaning in Python strings because they are used for **escape sequences**.

For example:

```python
"\n"
```

represents a newline.

Therefore, special care may be required when writing Windows paths inside normal Python strings.

---

## 🔹 Raw Strings

A **raw string** can be created by placing `r` before the string.

Example:

```python
path = r"D:\Projects\Python\notes.txt"
```

The `r` tells Python to treat backslashes as literal characters instead of interpreting them as escape sequences.

---

## 🔹 Forward Slashes

Forward slashes can also be used when specifying paths.

Example:

```python
path = "D:/Projects/Python/notes.txt"
```

This can make paths easier to write without dealing with backslash escape sequences.

---

# 📁 Current Working Directory

The **Current Working Directory**, commonly abbreviated as **CWD**, is the directory from which Python is currently working.

This is especially important when using **relative paths**.

We can find the current working directory using the `os` module.

```python
import os

print(os.getcwd())
```

The output depends on the directory from which the program is being executed.

---

# 🔎 `os.getcwd()`

The `getcwd()` function stands for:

> **Get Current Working Directory**

Example:

```python
import os

current_directory = os.getcwd()

print(current_directory)
```

It returns the path of the directory in which Python is currently working.

---

# 📂 `os.listdir()`

The `os.listdir()` function can be used to display the files and folders present inside a directory.

Example:

```python
import os

print(os.listdir())
```

Possible output:

```text
['main.py', 'notes.txt', 'data']
```

This is useful when checking what files and folders are available in the current directory.

---

# ⚠️ Understanding the Current Working Directory

Consider the following structure:

```text
Project
│
├── main.py
│
└── data
    └── notes.txt
```

If the Current Working Directory is:

```text
Project
```

then:

```python
open("data/notes.txt", "r")
```

can locate the file.

However:

```python
open("notes.txt", "r")
```

will search directly inside:

```text
Project
```

It will **not automatically search inside the `data` folder**.

Therefore, understanding the Current Working Directory is essential when working with relative file paths.

---

# 🛠 `open()` Function

The `open()` function is the main function used to open a file in Python.

### Syntax

```python
open(file, mode)
```

Example:

```python
f = open("notes.txt", "r")
```

Here:

```text
f         → File object
notes.txt → File name
r         → File mode
```

---

## 📌 File Name or Path

The first argument specifies the name or path of the file.

Example:

```python
open("notes.txt", "r")
```

Here:

```text
notes.txt
```

is the file name.

A relative path can also be provided:

```python
open("data/notes.txt", "r")
```

An absolute path can also be provided:

```python
open(r"D:\Projects\Python\data\notes.txt", "r")
```

---

## 📌 File Mode

The second argument tells Python **how we want to access the file**.

For example:

```python
open("notes.txt", "r")
```

Here:

```text
r → Read mode
```

Some commonly used modes are:

```text
r → Read
w → Write
a → Append
x → Create
```

These modes will be discussed in detail later in the chapter.

---

# 📦 File Object

When we write:

```python
f = open("notes.txt", "r")
```

Python returns a **file object**.

The variable:

```python
f
```

refers to that file object.

The file object provides methods that allow us to interact with the file.

Some important file methods include:

```python
f.read()
f.readline()
f.readlines()
f.write()
f.writelines()
f.close()
f.tell()
f.seek()
```

Each of these methods will be discussed in the appropriate sections of this chapter.

---

# 🔄 Basic File Handling Workflow

A basic file-handling operation can be represented as:

```text
Open File
    ↓
Choose File Mode
    ↓
Perform Operation
    ↓
Read / Write / Append
    ↓
Close File
```

Example:

```python
f = open("notes.txt", "r")

data = f.read()

print(data)

f.close()
```

The program performs the following steps:

1. Opens the file.
2. Reads the contents.
3. Displays the contents.
4. Closes the file.

This **Open → Operate → Close** pattern forms the foundation of basic file handling in Python.

# 🛠 `open()` Function - File Modes

The `open()` function uses **file modes** to determine what operation Python should perform on a file.

### Syntax

```python
open("filename", "mode")
```

Example:

```python
f = open("notes.txt", "r")
```

Here:

```text
notes.txt → File name
r         → File mode
```

The most commonly used file modes are:

```text
r → Read
w → Write
a → Append
x → Create
```

---

# 📚 File Modes

## 1️⃣ `r` - Read Mode

The `r` mode is used to open an existing file for reading.

```python
f = open("notes.txt", "r")
```

### Important Points

- The file must already exist.
- It allows reading the contents of the file.
- It does not overwrite existing data.
- If the file does not exist, Python raises `FileNotFoundError`.

Example:

```python
with open("notes.txt", "r") as f:
    data = f.read()

print(data)
```

---

## 2️⃣ `w` - Write Mode

The `w` mode is used to write data into a file.

```python
f = open("notes.txt", "w")
```

### Important Points

- If the file does not exist, Python creates it.
- If the file already exists, its previous contents are **erased**.
- New data is then written into the file.

Example:

```python
with open("notes.txt", "w") as f:
    f.write("Python File Handling")
```

Suppose the file originally contains:

```text
Python
Java
C++
```

After opening it in `"w"` mode and writing:

```python
f.write("Python File Handling")
```

the previous content is replaced with:

```text
Python File Handling
```

⚠️ **Be careful with `w` mode because it can overwrite existing data.**

---

## 3️⃣ `a` - Append Mode

The `a` mode is used to add new data to the **end of an existing file**.

```python
f = open("notes.txt", "a")
```

Unlike `w` mode, append mode does not remove the existing content.

Example:

```python
with open("notes.txt", "a") as f:
    f.write("\nFile handling is important.")
```

If the file originally contains:

```text
Python File Handling
```

it becomes:

```text
Python File Handling
File handling is important.
```

### Important Points

- Existing content is preserved.
- New content is added at the end.
- If the file does not exist, Python creates it.

---

## 4️⃣ `x` - Create Mode

The `x` mode is used to create a **new file**.

```python
f = open("new_notes.txt", "x")
```

If the file does not already exist, Python creates it.

Example:

```python
with open("new_notes.txt", "x") as f:
    f.write("This is a new file.")
```

However, if the file already exists, Python raises:

```text
FileExistsError
```

Example:

```python
f = open("new_notes.txt", "x")
```

If `new_notes.txt` already exists, the program will produce an error.

---

# 📊 `r` vs `w` vs `a` vs `x`

| Mode | Purpose | Creates if Missing | Existing Content |
|---|---|---|---|
| `r` | Read | ❌ | Preserved |
| `w` | Write | ✅ | Overwritten |
| `a` | Append | ✅ | Preserved |
| `x` | Create | ✅ | Error if already exists |

---

# 🔤 Text Mode - `t`

The `t` mode represents **text mode**.

Example:

```python
f = open("notes.txt", "rt")
```

Here:

```text
r → Read
t → Text
```

Therefore:

```python
"rt"
```

means:

> Open the file for reading in text mode.

Text mode is the **default mode** for normal text files.

Therefore:

```python
open("notes.txt", "r")
```

and:

```python
open("notes.txt", "rt")
```

are generally equivalent.

---

# 💾 Binary Mode - `b`

The `b` mode represents **binary mode**.

It is used when working with files containing binary data, such as:

- Images
- Audio
- Video
- PDF files
- Executable files
- Compressed files

Example:

```python
with open("photo.jpg", "rb") as f:
    data = f.read()
```

Here:

```text
r → Read
b → Binary
```

Therefore:

```python
"rb"
```

means:

> Open the file for reading in binary mode.

---

## ✍️ Binary Write Mode

Binary data can also be written using `wb`.

Example:

```python
with open("copy.jpg", "wb") as f:
    f.write(data)
```

Here:

```text
w → Write
b → Binary
```

---

# ➕ Read and Write Modes

The `+` symbol means that the file can be opened for **both reading and writing**.

Important combinations include:

```text
r+
w+
a+
```

---

# 🔄 `r+` - Read and Write

The `r+` mode allows both reading and writing.

```python
f = open("notes.txt", "r+")
```

### Important Points

- The file must already exist.
- Reading is allowed.
- Writing is allowed.
- Existing content is not automatically erased.
- The writing position depends on the current file-pointer position.

Example:

```python
with open("notes.txt", "r+") as f:
    data = f.read()
    print(data)

    f.write("\nNew information")
```

---

# 📝 `w+` - Write and Read

The `w+` mode allows both writing and reading.

```python
f = open("notes.txt", "w+")
```

### Important Points

- Reading is allowed.
- Writing is allowed.
- If the file does not exist, it is created.
- If the file already exists, its previous contents are erased.

Example:

```python
with open("notes.txt", "w+") as f:
    f.write("Python")

    f.seek(0)

    print(f.read())
```

### Output

```text
Python
```

The `seek(0)` moves the file pointer back to the beginning so that the newly written content can be read.

---

# ➕ `a+` - Append and Read

The `a+` mode allows both appending and reading.

```python
f = open("notes.txt", "a+")
```

### Important Points

- Reading is allowed.
- Writing is performed as an append operation.
- Existing content is preserved.
- If the file does not exist, it is created.
- `seek()` may be required when we want to read from a particular position.

Example:

```python
with open("notes.txt", "a+") as f:
    f.write("\nNew topic")

    f.seek(0)

    print(f.read())
```

---

# 📊 Complete File Mode Comparison

| Mode | Read | Write | Append | Creates if Missing | Existing Data |
|---|:---:|:---:|:---:|:---:|---|
| `r` | ✅ | ❌ | ❌ | ❌ | Preserved |
| `w` | ❌ | ✅ | ❌ | ✅ | Overwritten |
| `a` | ❌ | ✅ | ✅ | ✅ | Preserved |
| `x` | ❌ | ✅ | ❌ | ✅ | Error if exists |
| `r+` | ✅ | ✅ | ❌ | ❌ | Preserved |
| `w+` | ✅ | ✅ | ❌ | ✅ | Overwritten |
| `a+` | ✅ | ✅ | ✅ | ✅ | Preserved |

---

# 📊 Text and Binary Mode Combinations

The `t` and `b` modes can be combined with other file modes.

| Mode | Meaning |
|---|---|
| `rt` | Read text |
| `wt` | Write text |
| `at` | Append text |
| `rb` | Read binary |
| `wb` | Write binary |
| `ab` | Append binary |
| `r+b` | Read and write binary |
| `w+b` | Write and read binary |
| `a+b` | Append and read binary |

Text mode is the default, so:

```python
"r"
```

normally means:

```python
"rt"
```

---

# 🧠 Understanding File Mode Combinations

File modes become easier to understand when we break them into individual characters.

For example:

```python
"rb"
```

means:

```text
r → Read
b → Binary
```

Similarly:

```python
"w+"
```

means:

```text
w → Write
+ → Also allow reading
```

And:

```python
"a+"
```

means:

```text
a → Append
+ → Also allow reading
```

Therefore, file modes are combinations of different instructions.

---

# 🔒 Closing Files

After completing operations on a file, it should be closed.

The traditional approach is:

```python
f = open("notes.txt", "r")

data = f.read()

print(data)

f.close()
```

The `close()` method closes the file.

---

# ❓ Why Should We Close a File?

Closing a file is important because it:

- Releases system resources.
- Finishes pending file operations.
- Prevents unnecessary open file handles.
- Indicates that the program has finished working with the file.

However, manually calling `close()` can sometimes be forgotten.

Python provides the `with` statement to make file handling safer and cleaner.

---

# ✨ `with` Statement

The `with` statement provides a convenient way to work with files.

Example:

```python
with open("notes.txt", "r") as f:
    data = f.read()
    print(data)
```

When the `with` block finishes, Python automatically closes the file.

---

## ❌ Without `with`

```python
f = open("notes.txt", "r")

data = f.read()

print(data)

f.close()
```

Here, we have to manually close the file.

---

## ✅ With `with`

```python
with open("notes.txt", "r") as f:

    data = f.read()

    print(data)
```

The file is automatically closed when the `with` block ends.

---

# ⭐ Advantages of the `with` Statement

### 1. 🔒 Automatic Closing

The file is automatically closed after the block finishes.

### 2. 🧹 Cleaner Code

There is no need to manually write:

```python
f.close()
```

### 3. 🛡 Safer File Handling

The file is properly managed even when an exception occurs inside the block.

### 4. 👍 Recommended Practice

Using `with` is generally the preferred approach for opening and working with files.

---

# 📌 Checking Whether a File is Closed

The `closed` attribute can be used to check whether a file has been closed.

Example:

```python
f = open("notes.txt", "r")

print(f.closed)

f.close()

print(f.closed)
```

### Output

```text
False
True
```

Before calling `close()`:

```text
False
```

After calling `close()`:

```text
True
```

---

# 🧠 Important Points

- `r` is used for reading.
- `w` is used for writing and can overwrite existing content.
- `a` is used for appending.
- `x` is used for creating a new file.
- `t` represents text mode.
- `b` represents binary mode.
- `+` allows both reading and writing.
- `r+`, `w+`, and `a+` have different behaviors.
- `close()` closes an opened file.
- The `with` statement automatically manages the file.
- The `closed` attribute tells whether a file is closed.
- `w` mode should be used carefully because it can erase existing content.

# 📖 Reading Files

Reading a file means retrieving the information stored inside the file and using it in a Python program.

Python provides several methods for reading file contents:

- `read()`
- `read(n)`
- `readline()`
- `readlines()`
- `for` loop

Before reading a text file, we normally open it using **read mode (`r`)**.

---

# 📥 Reading a File Using `read()`

The `read()` method is used to read the contents of a file.

### Syntax

```python
f.read()
```

### Example

Suppose `notes.txt` contains:

```text
Python is easy to learn.
Practice is important.
File handling is useful.
```

We can read the complete file using:

```python
with open("notes.txt", "r") as f:
    data = f.read()

print(data)
```

### Output

```text
Python is easy to learn.
Practice is important.
File handling is useful.
```

By default, `read()` reads the remaining contents of the file from the current file-pointer position.

---

# 🔢 Reading a Specific Number of Characters Using `read(n)`

The `read()` method can also accept a number as an argument.

```python
f.read(n)
```

Here, `n` represents the number of characters to read.

### Example

```python
with open("notes.txt", "r") as f:
    data = f.read(10)

print(data)
```

If the file begins with:

```text
Python is easy to learn.
```

the output will be:

```text
Python is
```

Only the first 10 characters are read.

---

## 📌 Multiple `read()` Calls

The file pointer moves forward whenever data is read.

Example:

```python
with open("notes.txt", "r") as f:
    print(f.read(6))
    print(f.read(5))
```

Suppose the file contains:

```text
Python Programming
```

The first call:

```python
f.read(6)
```

reads:

```text
Python
```

The file pointer then moves forward.

The second call:

```python
f.read(5)
```

continues from the current position rather than starting again from the beginning.

---

# 📖 `readline()` Method

The `readline()` method is used to read **one line at a time** from a file.

### Syntax

```python
f.readline()
```

Suppose `subjects.txt` contains:

```text
Python
Java
C++
JavaScript
```

Example:

```python
with open("subjects.txt", "r") as f:
    line = f.readline()

print(line)
```

### Output

```text
Python
```

Only the first line is read.

---

# 🔄 Reading Multiple Lines Using `readline()`

We can call `readline()` multiple times to read multiple lines.

```python
with open("subjects.txt", "r") as f:
    print(f.readline())
    print(f.readline())
    print(f.readline())
```

### Output

```text
Python

Java

C++
```

Each call reads the next line.

The file pointer automatically moves forward after each `readline()` call.

---

# 📌 Reading Only the First Two Lines

If we want only the first two lines, we can call `readline()` twice.

```python
with open("subjects.txt", "r") as f:
    print(f.readline(), end="")
    print(f.readline(), end="")
```

### Output

```text
Python
Java
```

The `end=""` prevents `print()` from adding an additional newline because the line read from the file may already contain `\n`.

---

# 📚 `readlines()` Method

The `readlines()` method reads all the lines of a file and returns them as a **list**.

### Syntax

```python
f.readlines()
```

Example:

```python
with open("subjects.txt", "r") as f:
    lines = f.readlines()

print(lines)
```

If the file contains:

```text
Python
Java
C++
```

the result will be similar to:

```python
['Python\n', 'Java\n', 'C++']
```

The `\n` represents the newline character.

---

# 🔍 Accessing Individual Lines from `readlines()`

Since `readlines()` returns a list, we can use list indexing to access individual lines.

```python
with open("subjects.txt", "r") as f:
    lines = f.readlines()

print(lines[0])
print(lines[1])
```

### Output

```text
Python

Java
```

Python uses **zero-based indexing**:

```text
Python → 0
Java   → 1
C++    → 2
```

---

# 🔁 Reading a File Using a `for` Loop

A file object can directly be used with a `for` loop.

The loop reads the file **line by line**.

Example:

```python
with open("subjects.txt", "r") as f:
    for line in f:
        print(line, end="")
```

### Output

```text
Python
Java
C++
JavaScript
```

This is a convenient way to process a file one line at a time.

---

# 🎯 Reading Only the First Two Lines Using a `for` Loop

We can use a counter and the `break` statement to stop the loop after reading two lines.

```python
with open("subjects.txt", "r") as f:

    count = 0

    for line in f:
        print(line, end="")

        count += 1

        if count == 2:
            break
```

### Output

```text
Python
Java
```

### How It Works

Initially:

```python
count = 0
```

After reading the first line:

```python
count += 1
```

the value becomes:

```text
1
```

After reading the second line:

```text
2
```

The condition:

```python
if count == 2:
    break
```

becomes true and the loop stops.

---

# 🧹 Using `strip()` While Reading

Lines read from a text file may contain a newline character:

```python
"Aman\n"
```

The `strip()` method can remove surrounding whitespace, including the newline character.

Example:

```python
with open("students.txt", "r") as f:

    for line in f:
        print(line.strip())
```

If `students.txt` contains:

```text
Aman
Riya
Karan
```

the output will be:

```text
Aman
Riya
Karan
```

This is particularly useful when processing each line as individual data.

---

# 🧠 `read()` vs `readline()` vs `readlines()`

## `read()`

Reads the remaining contents as a single string.

```python
data = f.read()
```

Return type:

```text
String
```

---

## `readline()`

Reads one line.

```python
line = f.readline()
```

Return type:

```text
String
```

---

## `readlines()`

Reads all lines and returns them as a list.

```python
lines = f.readlines()
```

Return type:

```text
List
```

---

# 📊 Reading Methods Comparison

| Method | Purpose | Return Type |
|---|---|---|
| `read()` | Reads remaining file contents | String |
| `read(n)` | Reads `n` characters | String |
| `readline()` | Reads one line | String |
| `readlines()` | Reads all lines | List |
| `for line in f` | Processes file line by line | Line-by-line iteration |

---

# 📌 `read()` vs `readlines()`

Suppose the file contains:

```text
Python
Java
C++
```

Using:

```python
data = f.read()
```

produces one string conceptually like:

```python
"Python\nJava\nC++"
```

Whereas:

```python
data = f.readlines()
```

produces a list:

```python
['Python\n', 'Java\n', 'C++']
```

Therefore:

```text
read()       → String
readlines()  → List
```

---

# 📌 `readline()` vs `readlines()`

The names are similar, but their behavior is different.

### `readline()`

Reads one line:

```python
line = f.readline()
```

### `readlines()`

Reads all remaining lines and returns them as a list:

```python
lines = f.readlines()
```

Therefore:

```text
readline()   → One line
readlines()  → Multiple/all lines as a list
```

---

# 📍 File Pointer During Reading

Python maintains a **file pointer** that keeps track of the current position in a file.

Suppose a file contains:

```text
Python
```

Initially, the pointer is at the beginning:

```text
Python
^
```

After reading some characters, the pointer moves forward.

```text
Python
   ^
```

Therefore, when we perform another reading operation, Python continues from the current position.

---

# 🔄 Reading from the Current File-Pointer Position

Consider:

```python
with open("notes.txt", "r") as f:

    first = f.read(6)
    second = f.read(5)

    print(first)
    print(second)
```

If the file begins with:

```text
Python Programming
```

then:

```python
f.read(6)
```

reads:

```text
Python
```

The next:

```python
f.read(5)
```

continues from the new pointer position.

It does **not** start again from the beginning.

The file-pointer concept becomes especially important when using:

```python
tell()
```

and:

```python
seek()
```

which will be covered later.

---

# 📄 Reading an Empty File

If a file contains no data:

```python
with open("empty.txt", "r") as f:
    data = f.read()

print(data)
```

the result is an empty string:

```python
''
```

Similarly, when `readline()` reaches the end of a file, it returns:

```python
''
```

This indicates that there is no more data to read.

---

# 💻 Practical Example - Counting Lines

We can use a `for` loop to count the number of lines in a file.

```python
count = 0

with open("students.txt", "r") as f:

    for line in f:
        count += 1

print("Total lines:", count)
```

If the file contains:

```text
Aman
Riya
Karan
Neha
```

the output will be:

```text
Total lines: 4
```

---

# 💻 Practical Example - Displaying Numbered Lines

A `for` loop can also be used to display line numbers.

```python
line_number = 1

with open("subjects.txt", "r") as f:

    for line in f:
        print(line_number, line.strip())
        line_number += 1
```

### Output

```text
1 Python
2 Java
3 C++
4 JavaScript
```

This demonstrates how file reading can be combined with normal Python logic.

---

# 💻 Practical Example - Searching for a Word

We can read a file line by line and search for a particular word.

```python
with open("notes.txt", "r") as f:

    for line in f:

        if "Python" in line:
            print(line.strip())
```

If the file contains:

```text
Python is easy to learn.
Java is also popular.
Python is widely used.
```

the output will be:

```text
Python is easy to learn.
Python is widely used.
```

This is a simple example of processing file data using Python.

---

# ⚠️ Common Beginner Mistakes While Reading Files

## 1. Trying to Read a Non-existent File

```python
with open("missing.txt", "r") as f:
    data = f.read()
```

If the file does not exist, Python raises:

```text
FileNotFoundError
```

---

## 2. Reading from the End of the File

After reading all the contents:

```python
data = f.read()
```

the file pointer may be at the end.

Another:

```python
f.read()
```

may return:

```python
''
```

because there is no more data available from the current position.

---

## 3. Forgetting About Newline Characters

A line may contain:

```text
\n
```

For example:

```python
line = "Python\n"
```

If necessary, use:

```python
line.strip()
```

to remove the newline and surrounding whitespace.

---

## 4. Reading an Entire Very Large File at Once

This:

```python
data = f.read()
```

loads the remaining contents into memory.

For very large files, processing them line by line can be more appropriate:

```python
for line in f:
    ...
```

---

# 💡 Choosing the Right Reading Method

Use:

```text
read()
```

when you want the complete remaining content as a string.

Use:

```text
read(n)
```

when you need a specific number of characters.

Use:

```text
readline()
```

when you need one line at a time manually.

Use:

```text
readlines()
```

when you need the lines as a list.

Use:

```text
for line in f
```

when you want to process a file line by line.

---

# 🔑 Important Points

- `read()` reads the remaining file contents.
- `read(n)` reads `n` characters.
- `readline()` reads one line.
- `readlines()` returns the lines as a list.
- A file can be directly iterated using a `for` loop.
- The file pointer moves forward as data is read.
- Reading methods continue from the current file-pointer position.
- `strip()` can remove newline characters and surrounding whitespace.
- `read()` returns a string.
- `readlines()` returns a list.
- Reading line by line is useful when processing large files.
- `readline()` returns an empty string when the end of the file is reached.

# ✍️ Writing Files

Writing to a file means storing data from a Python program inside a file.

Python provides several ways to write data into files.

The most commonly used methods are:

- `write()`
- `writelines()`

Writing is generally performed using:

```text
w → Write mode
```

or:

```text
a → Append mode
```

---

# 📝 Writing Using `w` Mode

The `w` mode is used to write data into a file.

Example:

```python
f = open("notes.txt", "w")

f.write("Python File Handling")

f.close()
```

If `notes.txt` does not exist, Python creates it.

If it already exists, its previous contents are **overwritten**.

---

## 📌 Example

Suppose `notes.txt` initially contains:

```text
Python
Java
C++
```

Now we execute:

```python
with open("notes.txt", "w") as f:
    f.write("Python File Handling")
```

The previous contents are replaced.

The file now contains:

```text
Python File Handling
```

⚠️ This is an important property of `w` mode.

---

# ⚠️ `w` Mode Can Overwrite Existing Data

Consider:

```python
with open("notes.txt", "w") as f:
    f.write("New Content")
```

If the file already contains important information, that information will be removed before the new content is written.

Therefore:

```text
w → Write / Replace
```

Use `w` mode carefully when working with existing files.

---

# 🛠 `write()` Method

The `write()` method is used to write a string into a file.

### Syntax

```python
f.write(string)
```

Example:

```python
with open("notes.txt", "w") as f:
    f.write("Learning Python")
```

The string:

```text
Learning Python
```

is stored in the file.

---

# 🔢 Return Value of `write()`

The `write()` method returns the **number of characters written**.

Example:

```python
with open("notes.txt", "w") as f:
    result = f.write("Python")

print(result)
```

### Output

```text
6
```

Because:

```text
Python
```

contains 6 characters.

---

## 📌 Another Example

```python
with open("notes.txt", "w") as f:
    count = f.write("Hello World")

print("Characters written:", count)
```

### Output

```text
Characters written: 11
```

The return value represents the number of characters written, not the number of lines.

---

# 📄 Writing Multiple Lines

We can use the newline character `\n` to write multiple lines.

Example:

```python
with open("subjects.txt", "w") as f:
    f.write("Python\n")
    f.write("Java\n")
    f.write("C++\n")
```

The file will contain:

```text
Python
Java
C++
```

Here:

```python
\n
```

moves the next text to a new line.

---

# 🔤 Newline Character `\n`

The `\n` character represents a **new line**.

Example:

```python
with open("notes.txt", "w") as f:
    f.write("First Line\nSecond Line\nThird Line")
```

The file will contain:

```text
First Line
Second Line
Third Line
```

Without `\n`:

```python
f.write("First Line")
f.write("Second Line")
```

the result would be:

```text
First LineSecond Line
```

Therefore, when writing multiple lines, `\n` is often required.

---

# 📚 `writelines()` Method

The `writelines()` method is used to write multiple strings to a file.

### Syntax

```python
f.writelines(iterable)
```

Example:

```python
lines = [
    "Python\n",
    "Java\n",
    "C++\n"
]

with open("subjects.txt", "w") as f:
    f.writelines(lines)
```

The file will contain:

```text
Python
Java
C++
```

---

# ⚠️ Important: `writelines()` Does Not Automatically Add Newlines

Consider:

```python
lines = [
    "Python",
    "Java",
    "C++"
]

with open("subjects.txt", "w") as f:
    f.writelines(lines)
```

The file will contain:

```text
PythonJavaC++
```

This happens because `writelines()` writes the strings exactly as they are.

It does **not** automatically insert `\n` between them.

To create separate lines:

```python
lines = [
    "Python\n",
    "Java\n",
    "C++\n"
]

with open("subjects.txt", "w") as f:
    f.writelines(lines)
```

Now the file contains:

```text
Python
Java
C++
```

---

# 📊 `write()` vs `writelines()`

| Feature | `write()` | `writelines()` |
|---|---|---|
| Purpose | Writes a string | Writes multiple strings |
| Input | String | Iterable of strings |
| Adds `\n` automatically | ❌ No | ❌ No |
| Common Use | Single piece of text | Multiple lines/strings |
| Return Value | Number of characters written | `None` |

---

# 🔢 Writing Numbers to a File

The `write()` method expects a **string**.

Therefore, we cannot directly write an integer using:

```python
f.write(100)
```

This produces a `TypeError`.

Instead, convert the number to a string:

```python
with open("marks.txt", "w") as f:
    f.write(str(100))
```

Now:

```text
100
```

is stored in the file.

---

# 🔄 Using Variables While Writing

We can write the values of variables into a file.

Example:

```python
name = "Aarav"
marks = 92

with open("result.txt", "w") as f:
    f.write("Name: " + name + "\n")
    f.write("Marks: " + str(marks))
```

The file will contain:

```text
Name: Aarav
Marks: 92
```

---

# 📝 Using f-Strings While Writing

f-strings make it easier to write variables into files.

Example:

```python
name = "Aarav"
marks = 92

with open("result.txt", "w") as f:
    f.write(f"Name: {name}\n")
    f.write(f"Marks: {marks}")
```

The file contains:

```text
Name: Aarav
Marks: 92
```

This is often cleaner than repeatedly using string concatenation.

---

# 📋 Writing a List of Names

Suppose we have:

```python
names = ["Aarav", "Meera", "Kabir"]
```

We can write them into a file.

One approach is:

```python
names = ["Aarav", "Meera", "Kabir"]

with open("students.txt", "w") as f:
    for name in names:
        f.write(name + "\n")
```

The file will contain:

```text
Aarav
Meera
Kabir
```

---

# 📚 Writing a List Using `writelines()`

The same task can be performed using `writelines()`.

```python
names = ["Aarav\n", "Meera\n", "Kabir\n"]

with open("students.txt", "w") as f:
    f.writelines(names)
```

The file contains:

```text
Aarav
Meera
Kabir
```

Again, the newline characters must be included manually.

---

# 🔄 Writing Data in a Loop

We can use a loop to repeatedly write information into a file.

Example:

```python
with open("numbers.txt", "w") as f:

    for number in range(1, 6):
        f.write(str(number) + "\n")
```

The file will contain:

```text
1
2
3
4
5
```

This demonstrates how normal Python loops can be combined with file handling.

---

# 🧑‍🎓 Practical Example - Saving Student Names

We can take names from the user and save them into a file.

```python
with open("students.txt", "w") as f:

    for i in range(3):
        name = input("Enter student name: ")
        f.write(name + "\n")
```

If the user enters:

```text
Aarav
Meera
Kabir
```

the file will contain:

```text
Aarav
Meera
Kabir
```

---

# 📌 Writing User Input to a File

A simple example:

```python
name = input("Enter your name: ")

with open("profile.txt", "w") as f:
    f.write(name)
```

If the user enters:

```text
Aarav
```

the file will contain:

```text
Aarav
```

---

# ⚠️ Difference Between `w` and `a` While Writing

Suppose the file already contains:

```text
Python
```

### Using `w`

```python
with open("notes.txt", "w") as f:
    f.write("Java")
```

Result:

```text
Java
```

The old content is replaced.

---

### Using `a`

```python
with open("notes.txt", "a") as f:
    f.write("Java")
```

Result:

```text
PythonJava
```

The new data is added after the existing content.

If we want it on a new line:

```python
with open("notes.txt", "a") as f:
    f.write("\nJava")
```

Result:

```text
Python
Java
```

---

# 🧠 Writing vs Appending

```text
Writing
   ↓
w mode
   ↓
Existing content may be replaced
```

```text
Appending
   ↓
a mode
   ↓
Existing content is preserved
   ↓
New content is added at the end
```

---

# 📊 `w` vs `a`

| Feature | `w` Mode | `a` Mode |
|---|---|---|
| Purpose | Write | Append |
| Existing content | Overwritten | Preserved |
| Creates file if missing | ✅ | ✅ |
| New data | Replaces old content | Added at end |
| Risk of accidental data loss | Higher | Lower |

---

# 🔒 Closing a File After Writing

When using the traditional approach:

```python
f = open("notes.txt", "w")

f.write("Python")

f.close()
```

we manually close the file.

A better approach is:

```python
with open("notes.txt", "w") as f:
    f.write("Python")
```

The `with` statement automatically handles closing the file.

---

# 💡 Best Practice for Writing Files

Prefer:

```python
with open("notes.txt", "w") as f:
    f.write("Python")
```

instead of:

```python
f = open("notes.txt", "w")

f.write("Python")

f.close()
```

The `with` statement makes the code cleaner and safer.

---

# ⚠️ Common Beginner Mistakes While Writing

## 1. Forgetting the `\n`

Incorrect:

```python
with open("subjects.txt", "w") as f:
    f.write("Python")
    f.write("Java")
```

Result:

```text
PythonJava
```

Correct:

```python
with open("subjects.txt", "w") as f:
    f.write("Python\n")
    f.write("Java\n")
```

Result:

```text
Python
Java
```

---

## 2. Using `w` When You Actually Need `a`

If you want to preserve existing data, do not use:

```python
open("notes.txt", "w")
```

Use:

```python
open("notes.txt", "a")
```

when you want to add data to the existing content.

---

## 3. Trying to Write an Integer Directly

Incorrect:

```python
with open("marks.txt", "w") as f:
    f.write(95)
```

Correct:

```python
with open("marks.txt", "w") as f:
    f.write(str(95))
```

Or use an f-string:

```python
marks = 95

with open("marks.txt", "w") as f:
    f.write(f"{marks}")
```

---

## 4. Forgetting That `writelines()` Does Not Add Newlines

Incorrect:

```python
lines = ["Python", "Java", "C++"]

with open("subjects.txt", "w") as f:
    f.writelines(lines)
```

Result:

```text
PythonJavaC++
```

Correct:

```python
lines = ["Python\n", "Java\n", "C++\n"]

with open("subjects.txt", "w") as f:
    f.writelines(lines)
```

---

# 🔑 Important Points

- `w` mode is used to write data.
- `w` mode creates a file if it does not exist.
- `w` mode can overwrite existing content.
- `write()` writes a string to a file.
- `write()` returns the number of characters written.
- `\n` is used to move to a new line.
- `writelines()` writes multiple strings.
- `writelines()` does not automatically add newline characters.
- Numbers should be converted to strings before using `write()`.
- Variables can be written using string concatenation or f-strings.
- Loops can be used to write multiple pieces of data.
- `a` mode should be used when existing content needs to be preserved.
- Using `with` is recommended when writing files.

# ➕ Append Mode

Append mode is used when we want to **add new data to an existing file without deleting its previous contents**.

Append mode is represented by:

```text
a
```

### Syntax

```python
f = open("notes.txt", "a")
```

---

# 📝 Writing Data Using Append Mode

Example:

```python
with open("notes.txt", "a") as f:
    f.write("New topic")
```

If the file already contains:

```text
Python
Java
```

after running the program, it will contain:

```text
Python
Java
New topic
```

The existing data remains unchanged.

---

# 📌 Appending Data on a New Line

If we want the new data to appear on a separate line, we need to add `\n`.

```python
with open("notes.txt", "a") as f:
    f.write("\nC++")
```

If the file contains:

```text
Python
Java
```

it becomes:

```text
Python
Java
C++
```

---

# 🔄 Appending Multiple Values

We can use a loop to append multiple values.

```python
subjects = ["Python", "Java", "C++"]

with open("subjects.txt", "a") as f:
    for subject in subjects:
        f.write(subject + "\n")
```

The values are added to the end of the file.

---

# 🧑‍🎓 Practical Example - Adding Student Names

Suppose we already have a file containing student names.

We can add another student without removing the existing names:

```python
name = input("Enter student name: ")

with open("students.txt", "a") as f:
    f.write(name + "\n")
```

If the file initially contains:

```text
Aarav
Meera
```

and the user enters:

```text
Kabir
```

the file becomes:

```text
Aarav
Meera
Kabir
```

---

# 📊 Write Mode vs Append Mode

| Feature | `w` Mode | `a` Mode |
|---|---|---|
| Existing content | Removed | Preserved |
| New content | Replaces old content | Added at the end |
| Creates file if missing | ✅ | ✅ |
| Suitable for adding records | ❌ | ✅ |
| Risk of losing existing data | Yes | Much lower |

---

# 🆕 Create Mode

Create mode is represented by:

```text
x
```

It is specifically used to **create a new file**.

### Syntax

```python
f = open("new_file.txt", "x")
```

If the file does not exist, Python creates it.

---

# 📄 Creating a New File

Example:

```python
with open("new_notes.txt", "x") as f:
    f.write("This file was created using Python.")
```

Python creates:

```text
new_notes.txt
```

and stores:

```text
This file was created using Python.
```

inside it.

---

# ⚠️ What Happens If the File Already Exists?

The purpose of `x` mode is to create a file that does not already exist.

If the specified file already exists:

```python
with open("new_notes.txt", "x") as f:
    f.write("Hello")
```

Python raises:

```text
FileExistsError
```

This behavior helps prevent accidentally overwriting an existing file.

---

# 🔍 `x` Mode vs `w` Mode

Both modes can create a file if it does not exist, but their behavior is different when the file already exists.

### `w` Mode

```python
open("notes.txt", "w")
```

If the file exists:

```text
Existing content
       ↓
   Removed
       ↓
New content
```

### `x` Mode

```python
open("notes.txt", "x")
```

If the file exists:

```text
Existing file
      ↓
FileExistsError
```

Therefore:

```text
w → Create if missing + overwrite if existing

x → Create only if missing
```

---

# 📊 `w` vs `x`

| Feature | `w` | `x` |
|---|---|---|
| Creates missing file | ✅ | ✅ |
| Opens existing file | ✅ | ❌ |
| Existing content | Overwritten | Protected |
| Error if file exists | ❌ | ✅ `FileExistsError` |
| Main purpose | Writing | Creating a new file |

---

# 🔒 Closing Files

After completing file operations, the file should be closed.

Traditional approach:

```python
f = open("notes.txt", "w")

f.write("Python")

f.close()
```

The `close()` method closes the file.

---

# ✨ Using `with` Instead of `close()`

A cleaner approach is to use the `with` statement:

```python
with open("notes.txt", "w") as f:
    f.write("Python")
```

When the `with` block finishes, Python automatically closes the file.

This is generally preferred over manually calling `close()`.

---

# 📌 Checking Whether a File is Closed

A file object has a `closed` attribute.

Example:

```python
f = open("notes.txt", "w")

print(f.closed)

f.close()

print(f.closed)
```

### Output

```text
False
True
```

Before closing:

```text
False
```

After closing:

```text
True
```

---

# 📍 File Pointer

Whenever a file is opened, Python maintains a **file pointer**.

The file pointer represents the current position from which the next read or write operation will take place.

For example, consider:

```text
Python Programming
^
```

Initially, the pointer is at the beginning.

After reading some characters:

```text
Python Programming
      ^
```

the pointer moves forward.

---

# 🔎 `tell()` Method

The `tell()` method returns the current position of the file pointer.

### Syntax

```python
f.tell()
```

Example:

```python
with open("notes.txt", "r") as f:

    print(f.tell())

    f.read(6)

    print(f.tell())
```

If the file begins with:

```text
Python Programming
```

the output will be similar to:

```text
0
6
```

The exact position depends on the data and the file mode.

---

# 📌 Understanding `tell()`

At the beginning:

```text
File:
Python Programming
^

Pointer position = 0
```

After reading 6 characters:

```text
Python Programming
      ^

Pointer position = 6
```

Therefore:

```python
f.tell()
```

helps us determine where the file pointer currently is.

---

# 🎯 `seek()` Method

The `seek()` method is used to **move the file pointer to a particular position**.

### Syntax

```python
f.seek(position)
```

For example:

```python
f.seek(0)
```

moves the pointer to the beginning of the file.

---

# 🔄 Using `tell()` and `seek()` Together

Example:

```python
with open("notes.txt", "r") as f:

    print(f.tell())

    print(f.read(6))

    print(f.tell())

    f.seek(0)

    print(f.tell())
```

Possible output:

```text
0
Python
6
0
```

### What Happened?

Initially:

```text
Pointer = 0
```

After:

```python
f.read(6)
```

the pointer moves forward.

Then:

```python
f.tell()
```

shows the new position.

Finally:

```python
f.seek(0)
```

moves the pointer back to the beginning.

---

# 📖 Reading the Same Content Again Using `seek()`

We can use `seek()` to return to the beginning and read the file again.

```python
with open("notes.txt", "r") as f:

    print(f.read(6))

    f.seek(0)

    print(f.read(6))
```

If the file begins with:

```text
Python Programming
```

the output will be:

```text
Python
Python
```

The first `read(6)` moves the pointer forward.

Then:

```python
f.seek(0)
```

returns it to the beginning.

---

# 📊 `tell()` vs `seek()`

| Method | Purpose |
|---|---|
| `tell()` | Returns current file-pointer position |
| `seek()` | Moves file pointer to a specified position |

Simple way to remember:

```text
tell() → Where am I?

seek() → Go there.
```

---

# ⚠️ Important Points About File Pointers

- A file has a current position called the file pointer.
- Reading generally moves the pointer forward.
- Writing also affects the current file position.
- `tell()` tells us the current position.
- `seek()` changes the position.
- `seek(0)` commonly moves the pointer back to the beginning.
- File-pointer behavior becomes especially important when performing multiple read/write operations on the same file.

---

# 🧠 File Pointer Example

Consider:

```python
with open("notes.txt", "r") as f:

    print(f.tell())

    f.read(5)

    print(f.tell())

    f.seek(2)

    print(f.tell())
```

The sequence is:

```text
Start
  ↓
Pointer = 0
  ↓
Read 5 characters
  ↓
Pointer moves forward
  ↓
seek(2)
  ↓
Pointer moves to position 2
```

This demonstrates how Python keeps track of the current position while working with a file.

# 🔤 Encoding

Encoding is the process of converting text into a particular format of bytes so that it can be stored and interpreted correctly by a computer.

When Python works with text files, encoding determines how characters are converted into bytes and how those bytes are converted back into characters.

---

# 🌐 Why is Encoding Important?

Different languages and symbols contain many characters that are not represented by basic English letters.

For example:

```text
Hello
Python
Café
नमस्ते
你好
```

Python needs a way to correctly represent these characters when storing them in a file.

Encoding provides that representation.

---

# ⭐ UTF-8 Encoding

**UTF-8** is one of the most commonly used text encodings.

It supports a very large range of characters and is widely used for text files and web applications.

Example:

```python
with open("message.txt", "w", encoding="utf-8") as f:
    f.write("Hello नमस्ते")
```

The file can then store the text correctly using UTF-8 encoding.

---

# 📌 Specifying Encoding While Opening a File

The `encoding` parameter can be passed to `open()`.

### Syntax

```python
open("filename", "mode", encoding="encoding_name")
```

Example:

```python
with open("message.txt", "r", encoding="utf-8") as f:
    data = f.read()

print(data)
```

Here:

```text
encoding="utf-8"
```

tells Python to interpret the file using UTF-8.

---

# ✍️ Writing Using UTF-8

Encoding can also be specified while writing.

```python
with open("message.txt", "w", encoding="utf-8") as f:
    f.write("Python supports Unicode text.")
```

This explicitly tells Python which encoding to use while writing the text.

---

# 🔄 Reading and Writing with the Same Encoding

When possible, it is useful to use the same encoding when writing and reading a text file.

Example:

```python
with open("message.txt", "w", encoding="utf-8") as f:
    f.write("Python File I/O")
```

Then:

```python
with open("message.txt", "r", encoding="utf-8") as f:
    data = f.read()

print(data)
```

This ensures that the text is interpreted consistently.

---

# ⚠️ Encoding Errors

If a file is saved using one encoding but Python attempts to read it using an incompatible encoding, an encoding-related error can occur.

A common exception is:

```text
UnicodeDecodeError
```

This generally means Python could not correctly decode the file's bytes into text using the selected encoding.

---

# 📄 Text Encoding vs Binary Data

Encoding is particularly relevant when working with **text**.

For example:

```python
with open("message.txt", "r", encoding="utf-8") as f:
    data = f.read()
```

For binary files, we normally use binary mode:

```python
with open("photo.jpg", "rb") as f:
    data = f.read()
```

Binary data is handled as bytes rather than ordinary decoded text.

---

# 📊 Text Mode vs Binary Mode

| Feature | Text Mode | Binary Mode |
|---|---|---|
| Mode Example | `r`, `w` | `rb`, `wb` |
| Data Type | Text / strings | Bytes |
| Encoding | Relevant | Not used for ordinary text decoding |
| Example | `.txt` | `.jpg` |
| Common Use | Documents | Images, audio, video |

---

# 🗑 File Modification

Python allows us to modify files by reading their existing contents and then writing updated content back to the file.

For example, suppose `students.txt` contains:

```text
Aarav
Meera
Kabir
```

If we want to replace `Meera` with `Riya`, we can read the contents first.

```python
with open("students.txt", "r") as f:
    data = f.read()

data = data.replace("Meera", "Riya")

with open("students.txt", "w") as f:
    f.write(data)
```

The file will now contain:

```text
Aarav
Riya
Kabir
```

---

# 🔄 General Process of Modifying a File

A simple file-modification process is:

```text
Read Existing Data
       ↓
Modify Data in Python
       ↓
Open File for Writing
       ↓
Write Updated Data
```

For example:

```python
with open("notes.txt", "r") as f:
    data = f.read()

data = data.replace("old", "new")

with open("notes.txt", "w") as f:
    f.write(data)
```

---

# 📌 Replacing Text in a File

The `replace()` string method can be used to replace one piece of text with another.

Example:

```python
with open("notes.txt", "r") as f:
    data = f.read()

data = data.replace("Python", "Python Programming")

with open("notes.txt", "w") as f:
    f.write(data)
```

If the original file contains:

```text
Python is useful.
I am learning Python.
```

the modified file becomes:

```text
Python Programming is useful.
I am learning Python Programming.
```

---

# ⚠️ Important Point About `replace()`

The `replace()` method does not directly modify the file.

It modifies the **string stored in the Python variable**.

For example:

```python
data = data.replace("old", "new")
```

changes the value of `data`.

The actual file is updated only when the modified data is written back:

```python
with open("notes.txt", "w") as f:
    f.write(data)
```

---

# 💻 Practical Example - Removing Text

Suppose a file contains:

```text
Python
Java
C++
JavaScript
```

We can remove a particular line by replacing it with an empty string.

```python
with open("subjects.txt", "r") as f:
    data = f.read()

data = data.replace("Java\n", "")

with open("subjects.txt", "w") as f:
    f.write(data)
```

The resulting file becomes:

```text
Python
C++
JavaScript
```

---

# 💻 Practical Example - Updating a Student Record

Suppose a file contains:

```text
Name: Aarav
Marks: 75
```

We can update the marks:

```python
with open("student.txt", "r") as f:
    data = f.read()

data = data.replace("Marks: 75", "Marks: 90")

with open("student.txt", "w") as f:
    f.write(data)
```

The file becomes:

```text
Name: Aarav
Marks: 90
```

---

# ⚠️ Limitations of Simple Text Replacement

Using `replace()` is useful for simple files, but it may replace **every occurrence** of the specified text.

For example:

```python
data = data.replace("Python", "Python Programming")
```

will replace every occurrence of `"Python"` in the string.

For structured or complex data, more controlled techniques may be required.

---

# ❌ Deleting Files

Writing an empty string into a file does **not** delete the file itself.

For example:

```python
with open("notes.txt", "w") as f:
    f.write("")
```

This makes the file empty, but the file still exists.

To actually delete a file, we can use Python's `os` module.

---

# 🗑 Deleting a File Using `os.remove()`

The `os.remove()` function deletes a file.

Example:

```python
import os

os.remove("notes.txt")
```

After successful execution, the file is removed from the filesystem.

---

# ⚠️ File Must Exist

If we try to delete a file that does not exist:

```python
import os

os.remove("missing.txt")
```

Python raises:

```text
FileNotFoundError
```

Therefore, we should make sure that the file exists before attempting to remove it.

---

# 🔍 Checking Whether a File Exists

The `os.path.exists()` function can be used to check whether a path exists.

Example:

```python
import os

if os.path.exists("notes.txt"):
    os.remove("notes.txt")
    print("File deleted.")
else:
    print("File does not exist.")
```

This avoids attempting to remove a file that is not present.

---

# 📂 Deleting a File Using `pathlib`

The `pathlib` module provides another modern way to work with paths.

Example:

```python
from pathlib import Path

file_path = Path("notes.txt")

if file_path.exists():
    file_path.unlink()
    print("File deleted.")
else:
    print("File does not exist.")
```

Here:

```python
unlink()
```

is used to remove the file.

---

# 📚 `os` Module

The `os` module provides functions for interacting with the operating system.

It is useful for working with:

- Files
- Directories
- Paths
- Current working directory
- File existence
- File deletion

Example:

```python
import os

print(os.getcwd())
```

---

# 📌 Commonly Used `os` Functions for File Handling

### `os.getcwd()`

Returns the Current Working Directory.

```python
import os

print(os.getcwd())
```

---

### `os.listdir()`

Returns the files and directories inside a location.

```python
import os

print(os.listdir())
```

---

### `os.path.exists()`

Checks whether a file or directory exists.

```python
import os

print(os.path.exists("notes.txt"))
```

---

### `os.remove()`

Deletes a file.

```python
import os

os.remove("notes.txt")
```

---

# 📁 `pathlib`

`pathlib` is a Python module designed for working with filesystem paths using objects.

Example:

```python
from pathlib import Path

path = Path("notes.txt")
```

The `Path` object can then be used for various file and directory operations.

---

# 🔍 Checking File Existence with `pathlib`

```python
from pathlib import Path

path = Path("notes.txt")

if path.exists():
    print("File exists.")
else:
    print("File does not exist.")
```

---

# 📄 Checking Whether a Path is a File

The `is_file()` method checks whether a path points to a file.

```python
from pathlib import Path

path = Path("notes.txt")

if path.is_file():
    print("It is a file.")
```

---

# 📂 Checking Whether a Path is a Directory

The `is_dir()` method checks whether a path points to a directory.

```python
from pathlib import Path

path = Path("data")

if path.is_dir():
    print("It is a directory.")
```

---

# 🗑 Removing a File with `pathlib`

The `unlink()` method can remove a file.

```python
from pathlib import Path

path = Path("notes.txt")

if path.exists():
    path.unlink()
```

---

# 📊 `os` vs `pathlib`

| Feature | `os` | `pathlib` |
|---|---|---|
| Current Directory | `os.getcwd()` | `Path.cwd()` |
| File Exists | `os.path.exists()` | `Path.exists()` |
| Delete File | `os.remove()` | `Path.unlink()` |
| File Check | `os.path.isfile()` | `Path.is_file()` |
| Directory Check | `os.path.isdir()` | `Path.is_dir()` |
| Style | Function-based | Object-oriented |

---

# ⚠️ File-Related Exceptions

File operations can produce errors when something goes wrong.

Some common file-related exceptions are:

- `FileNotFoundError`
- `FileExistsError`
- `PermissionError`
- `IsADirectoryError`
- `NotADirectoryError`
- `UnicodeDecodeError`

---

# ❌ `FileNotFoundError`

This occurs when Python tries to access a file that does not exist.

Example:

```python
with open("missing.txt", "r") as f:
    data = f.read()
```

Possible error:

```text
FileNotFoundError
```

---

# 🆕 `FileExistsError`

This commonly occurs when using `x` mode to create a file that already exists.

Example:

```python
with open("notes.txt", "x") as f:
    f.write("Hello")
```

If `notes.txt` already exists:

```text
FileExistsError
```

---

# 🔒 `PermissionError`

This occurs when Python does not have sufficient permission to perform an operation.

For example, a program may attempt to access a protected file or directory.

---

# 📂 `IsADirectoryError`

This can occur when an operation expects a file but the provided path refers to a directory.

For example:

```python
with open("data", "r") as f:
    data = f.read()
```

if `data` is a directory rather than a file.

---

# 📁 `NotADirectoryError`

This can occur when a path contains a component that Python expects to be a directory but it is actually a file.

For example, trying to access something like:

```text
notes.txt/data.txt
```

when `notes.txt` is a file.

---

# 🔤 `UnicodeDecodeError`

This can occur when Python tries to decode file contents using an encoding that is not compatible with the file's data.

Example:

```python
with open("data.txt", "r", encoding="utf-8") as f:
    data = f.read()
```

If the file is not encoded in a compatible way, Python may raise:

```text
UnicodeDecodeError
```

---

# 🛡 Exception Handling

Python provides `try` and `except` blocks to handle errors without abruptly terminating the program.

Example:

```python
try:
    with open("notes.txt", "r") as f:
        data = f.read()

    print(data)

except FileNotFoundError:
    print("The file was not found.")
```

If the file does not exist, instead of displaying a full traceback, the program displays:

```text
The file was not found.
```

---

# 🔐 Handling Multiple File Exceptions

We can handle different exceptions separately.

```python
try:
    with open("notes.txt", "r") as f:
        data = f.read()

except FileNotFoundError:
    print("File does not exist.")

except PermissionError:
    print("Permission denied.")

except UnicodeDecodeError:
    print("Unable to decode the file.")
```

This makes the program more robust because different problems can receive different responses.

---

# 🧠 General File Exception Handling Pattern

A useful pattern is:

```python
try:
    # File operation
    pass

except FileNotFoundError:
    # Handle missing file
    pass

except PermissionError:
    # Handle permission problem
    pass
```

Exception handling should be used when an error is reasonably expected and the program can respond appropriately.

---

# ⭐ Key Points

- Encoding determines how text is represented as bytes and decoded back into characters.
- UTF-8 is a widely used text encoding.
- The `encoding` parameter can be supplied to `open()`.
- File contents can be modified by reading them, changing the data, and writing it back.
- `replace()` modifies a Python string, not the file directly.
- The modified data must be written back to update the file.
- `os.remove()` can delete a file.
- `pathlib.Path.unlink()` can also delete a file.
- `os.path.exists()` checks whether a path exists.
- `Path.exists()` performs a similar check using `pathlib`.
- `os` provides operating-system-level file and directory functions.
- `pathlib` provides an object-oriented approach to filesystem paths.
- File operations can raise different exceptions.
- `try` and `except` can be used to handle expected file-related errors.

# 💻 Common Practical Programs

The concepts of File I/O become easier to understand when they are used in practical programs.

The following programs demonstrate common file-handling tasks using Python.

---

# 1️⃣ Read the Complete Contents of a File

```python
with open("notes.txt", "r") as f:
    data = f.read()

print(data)
```

This program reads the complete contents of the file and displays them.

---

# 2️⃣ Read a File Line by Line

```python
with open("notes.txt", "r") as f:

    for line in f:
        print(line, end="")
```

This reads and processes the file one line at a time.

---

# 3️⃣ Count the Number of Lines

```python
count = 0

with open("notes.txt", "r") as f:

    for line in f:
        count += 1

print("Total lines:", count)
```

If the file contains 5 lines:

```text
Total lines: 5
```

---

# 4️⃣ Count the Number of Words

```python
count = 0

with open("notes.txt", "r") as f:

    for line in f:
        words = line.split()
        count += len(words)

print("Total words:", count)
```

The `split()` method divides each line into individual words.

---

# 5️⃣ Count the Number of Characters

```python
with open("notes.txt", "r") as f:
    data = f.read()

print("Total characters:", len(data))
```

The `len()` function returns the number of characters in the string.

---

# 6️⃣ Search for a Word in a File

```python
word = input("Enter word to search: ")

with open("notes.txt", "r") as f:
    data = f.read()

if word in data:
    print("Word found.")
else:
    print("Word not found.")
```

This program searches for a particular word inside the file.

---

# 7️⃣ Search Line by Line

Instead of reading the complete file at once, we can search each line separately.

```python
word = input("Enter word to search: ")

with open("notes.txt", "r") as f:

    for line in f:

        if word in line:
            print(line.strip())
```

This is useful when we want to know which lines contain a particular word.

---

# 8️⃣ Copy Contents from One File to Another

We can read data from one file and write it into another file.

```python
with open("source.txt", "r") as source:
    data = source.read()

with open("backup.txt", "w") as destination:
    destination.write(data)
```

The contents of `source.txt` are copied into `backup.txt`.

---

# 9️⃣ Add New Data to an Existing File

```python
new_data = input("Enter information: ")

with open("notes.txt", "a") as f:
    f.write("\n" + new_data)
```

The new information is added to the end of the file without removing the existing content.

---

# 🔟 Save Multiple Names to a File

```python
with open("students.txt", "w") as f:

    for i in range(3):
        name = input("Enter student name: ")
        f.write(name + "\n")
```

If the user enters:

```text
Aarav
Meera
Kabir
```

the file will contain:

```text
Aarav
Meera
Kabir
```

---

# 1️⃣1️⃣ Append Multiple Names

If we want to preserve the existing names and add new ones:

```python
with open("students.txt", "a") as f:

    for i in range(3):
        name = input("Enter student name: ")
        f.write(name + "\n")
```

The new names are added after the existing data.

---

# 1️⃣2️⃣ Replace Text in a File

```python
with open("notes.txt", "r") as f:
    data = f.read()

data = data.replace("Python", "Python Programming")

with open("notes.txt", "w") as f:
    f.write(data)
```

The program:

```text
Read
  ↓
Modify
  ↓
Rewrite
```

the file contents.

---

# 1️⃣3️⃣ Remove a Particular Line

Suppose a file contains:

```text
Python
Java
C++
JavaScript
```

We can remove a specific line:

```python
with open("subjects.txt", "r") as f:
    lines = f.readlines()

with open("subjects.txt", "w") as f:

    for line in lines:

        if line.strip() != "Java":
            f.write(line)
```

The resulting file becomes:

```text
Python
C++
JavaScript
```

---

# 1️⃣4️⃣ Display Numbered Lines

```python
line_number = 1

with open("notes.txt", "r") as f:

    for line in f:
        print(f"{line_number}: {line.strip()}")
        line_number += 1
```

Possible output:

```text
1: Python is easy to learn.
2: File handling is useful.
3: Practice improves programming.
```

---

# 1️⃣5️⃣ Read Only the First Two Lines

Using `readline()`:

```python
with open("notes.txt", "r") as f:
    print(f.readline(), end="")
    print(f.readline(), end="")
```

Using a `for` loop:

```python
with open("notes.txt", "r") as f:

    count = 0

    for line in f:
        print(line, end="")

        count += 1

        if count == 2:
            break
```

Both approaches allow us to read only the first two lines.

---

# 1️⃣6️⃣ Create a File Only If It Does Not Exist

```python
try:

    with open("new_notes.txt", "x") as f:
        f.write("New file created.")

    print("File created successfully.")

except FileExistsError:
    print("File already exists.")
```

This prevents an existing file from being accidentally overwritten.

---

# 1️⃣7️⃣ Check Whether a File Exists

Using `os`:

```python
import os

if os.path.exists("notes.txt"):
    print("File exists.")
else:
    print("File does not exist.")
```

Using `pathlib`:

```python
from pathlib import Path

path = Path("notes.txt")

if path.exists():
    print("File exists.")
else:
    print("File does not exist.")
```

---

# 1️⃣8️⃣ Delete a File Safely

Using `os`:

```python
import os

if os.path.exists("notes.txt"):
    os.remove("notes.txt")
    print("File deleted.")
else:
    print("File does not exist.")
```

This first checks whether the file exists before attempting to delete it.

---

# 1️⃣9️⃣ Read and Write Using `r+`

The `r+` mode allows both reading and writing.

```python
with open("notes.txt", "r+") as f:

    data = f.read()

    print(data)

    f.write("\nNew information")
```

The file must already exist.

The exact location of the writing operation depends on the current file-pointer position.

---

# 2️⃣0️⃣ Using `tell()` and `seek()`

```python
with open("notes.txt", "r") as f:

    print("Initial position:", f.tell())

    print(f.read(5))

    print("Current position:", f.tell())

    f.seek(0)

    print("After seek:", f.tell())
```

This demonstrates how Python can track and change the file-pointer position.

---

# ⚖️ Important Comparisons

## `read()` vs `readline()` vs `readlines()`

| Method | Purpose | Result |
|---|---|---|
| `read()` | Reads remaining contents | String |
| `read(n)` | Reads `n` characters | String |
| `readline()` | Reads one line | String |
| `readlines()` | Reads all remaining lines | List |

---

## `write()` vs `writelines()`

| Feature | `write()` | `writelines()` |
|---|---|---|
| Input | String | Iterable of strings |
| Multiple strings | One call for one string | Multiple strings |
| Adds newline automatically | ❌ | ❌ |
| Return value | Number of characters | `None` |

---

## `w` vs `a`

| Feature | `w` | `a` |
|---|---|---|
| Existing content | Overwritten | Preserved |
| New data | Replaces old data | Added at end |
| Creates missing file | ✅ | ✅ |
| Best for | Replacing content | Adding content |

---

## `w` vs `x`

| Feature | `w` | `x` |
|---|---|---|
| Creates missing file | ✅ | ✅ |
| Existing file | Overwrites | Raises error |
| Main purpose | Writing | Creating |
| Protects existing content | ❌ | ✅ |

---

## `r` vs `r+`

| Feature | `r` | `r+` |
|---|---|---|
| Read | ✅ | ✅ |
| Write | ❌ | ✅ |
| File must exist | ✅ | ✅ |
| Existing data automatically erased | ❌ | ❌ |

---

## `w+` vs `a+`

| Feature | `w+` | `a+` |
|---|---|---|
| Read | ✅ | ✅ |
| Write | ✅ | ✅ |
| Existing content | Overwritten | Preserved |
| Creates if missing | ✅ | ✅ |
| Writing behavior | Normal write | Append |

---

# 🌍 Real-Life Applications of File I/O

File handling is not limited to simple text files. It forms the foundation of many real-world data-storage operations.

### 🎓 1. Student Management

Student information can be stored and updated using files.

```text
Name
Roll Number
Marks
Attendance
```

---

### 💰 2. Financial Records

Applications can store information such as:

```text
Transactions
Expenses
Payments
Reports
```

---

### 🎮 3. Game Save Systems

Games can store:

```text
Player Name
Score
Level
Settings
Progress
```

---

### 📝 4. Notes and To-Do Applications

Applications can save:

```text
Tasks
Notes
Reminders
Ideas
```

---

### 📊 5. Data Analysis

Python programs frequently read data from files before processing it.

Examples:

```text
CSV files
Text files
JSON files
Log files
```

---

### 🤖 6. AI and Machine Learning

File handling is important when working with:

```text
Datasets
Training data
Text documents
Configuration files
Model outputs
```

---

### 🌐 7. Application Logs

Programs can store information about events and errors in log files.

Example:

```text
Application started
User logged in
File processed
Error occurred
```

---

# 💡 Best Practices

## 1. Prefer the `with` Statement

Use:

```python
with open("notes.txt", "r") as f:
    data = f.read()
```

instead of manually managing the file whenever possible.

---

## 2. Specify Encoding for Text Files When Appropriate

For predictable text handling:

```python
with open("notes.txt", "r", encoding="utf-8") as f:
    data = f.read()
```

---

## 3. Choose the Correct File Mode

Use the mode according to the required operation:

```text
r → Read
w → Replace / Write
a → Append
x → Create
```

Choosing the wrong mode can result in unexpected data loss.

---

## 4. Be Careful with `w`

Before using:

```python
open("notes.txt", "w")
```

remember that existing contents can be overwritten.

---

## 5. Use `a` When Existing Data Must Be Preserved

If the goal is to add new information:

```python
with open("notes.txt", "a") as f:
    f.write("\nNew information")
```

---

## 6. Handle Expected Errors

For operations where errors are possible:

```python
try:
    with open("notes.txt", "r") as f:
        data = f.read()

except FileNotFoundError:
    print("File not found.")
```

---

## 7. Use Meaningful File Names

Prefer names such as:

```text
students.txt
expenses.txt
notes.txt
results.txt
```

instead of unclear names such as:

```text
abc.txt
file1.txt
test123.txt
```

---

## 8. Use Paths Carefully

When working with multiple folders, make sure the path points to the intended file.

Relative paths should always be understood in relation to the Current Working Directory.

---

## 9. Avoid Unnecessary Repeated File Operations

If a file can be read once and processed in memory efficiently, avoid repeatedly opening and reading it unnecessarily.

---

## 10. Protect Important Data

Before performing operations that may overwrite or delete data, make sure the operation is intentional.

---

# ⚠️ Common Beginner Mistakes

### 1. Using the Wrong File Mode

```python
open("notes.txt", "w")
```

when the intention was to append data can accidentally remove existing contents.

---

### 2. Forgetting the File Path

Python searches for relative paths from the Current Working Directory.

If the file is somewhere else, a `FileNotFoundError` may occur.

---

### 3. Forgetting `\n`

Writing:

```python
f.write("Python")
f.write("Java")
```

produces:

```text
PythonJava
```

If separate lines are required:

```python
f.write("Python\n")
f.write("Java\n")
```

---

### 4. Expecting `writelines()` to Add Newlines

This:

```python
f.writelines(["Python", "Java", "C++"])
```

does not automatically create separate lines.

Use:

```python
f.writelines(["Python\n", "Java\n", "C++\n"])
```

---

### 5. Trying to Write an Integer Directly

Incorrect:

```python
f.write(100)
```

Correct:

```python
f.write(str(100))
```

---

### 6. Forgetting About the File Pointer

After reading data, the pointer moves forward.

Therefore:

```python
f.read()
f.read()
```

does not read the complete file twice.

Use:

```python
f.seek(0)
```

when you need to return to the beginning.

---

### 7. Trying to Read a Deleted or Missing File

Always make sure that the file exists before attempting to read it when necessary.

---

### 8. Using a File Path as if It Were a Directory

A path such as:

```text
notes.txt/data.txt
```

will not work if `notes.txt` is a file.

---

### 9. Forgetting Encoding

Files containing special or non-ASCII characters may require an appropriate encoding.

For example:

```python
open("message.txt", "r", encoding="utf-8")
```

---

### 10. Deleting Without Checking

Before deleting important files, verify the path carefully.

```python
os.remove("notes.txt")
```

permanently removes the file from its location.

---

# ⭐ Key Points

- File I/O allows Python programs to store and retrieve persistent data.
- `open()` is used to open files.
- `r` reads data.
- `w` writes and can overwrite existing data.
- `a` appends data.
- `x` creates a new file.
- `t` represents text mode.
- `b` represents binary mode.
- `+` allows both reading and writing.
- `read()` reads file contents.
- `readline()` reads one line.
- `readlines()` returns multiple lines as a list.
- A `for` loop can process a file line by line.
- `write()` writes a string.
- `writelines()` writes multiple strings.
- `\n` represents a newline.
- `with` provides safer file management.
- `tell()` returns the current file-pointer position.
- `seek()` changes the file-pointer position.
- Encoding controls how text is interpreted.
- `os` provides operating-system-related file operations.
- `pathlib` provides an object-oriented way to work with paths.
- `try` and `except` can handle file-related errors.
- File modification generally involves reading, changing, and rewriting data.
- `os.remove()` and `Path.unlink()` can delete files.

---

# 📊 Quick Revision Tables

## 📖 Basic File Modes

| Mode | Meaning | Existing File |
|---|---|---|
| `r` | Read | Must exist |
| `w` | Write | Overwrites |
| `a` | Append | Preserves |
| `x` | Create | Error if exists |

---

## 📖 Additional Mode Characters

| Character | Meaning |
|---|---|
| `t` | Text |
| `b` | Binary |
| `+` | Read and Write |

---

## 📖 Reading Methods

| Method | Use |
|---|---|
| `read()` | Read remaining contents |
| `read(n)` | Read `n` characters |
| `readline()` | Read one line |
| `readlines()` | Read lines into a list |
| `for line in f` | Iterate through lines |

---

## 📖 Writing Methods

| Method | Use |
|---|---|
| `write()` | Write a string |
| `writelines()` | Write multiple strings |

Remember:

```text
Neither write() nor writelines() automatically adds \n.
```

---

## 📖 File Pointer Methods

| Method | Purpose |
|---|---|
| `tell()` | Returns current pointer position |
| `seek()` | Moves pointer to a specified position |

Easy way to remember:

```text
tell() → Where am I?
seek() → Move there.
```

---

## 📖 Useful `os` Functions

| Function | Purpose |
|---|---|
| `os.getcwd()` | Get Current Working Directory |
| `os.listdir()` | List files and directories |
| `os.path.exists()` | Check whether a path exists |
| `os.remove()` | Delete a file |

---

## 📖 Useful `pathlib` Methods

| Method | Purpose |
|---|---|
| `Path.exists()` | Check existence |
| `Path.is_file()` | Check whether it is a file |
| `Path.is_dir()` | Check whether it is a directory |
| `Path.unlink()` | Delete a file |

---

## 📖 Common Exceptions

| Exception | Common Cause |
|---|---|
| `FileNotFoundError` | File does not exist |
| `FileExistsError` | File already exists with `x` mode |
| `PermissionError` | Insufficient permission |
| `IsADirectoryError` | Path refers to a directory instead of a file |
| `NotADirectoryError` | A path component is not a directory |
| `UnicodeDecodeError` | Incorrect/incompatible text decoding |

---

# ⭐ Key Takeaways

The most important File I/O concepts can be summarized as:

```text
Open
  ↓
Choose Mode
  ↓
Read / Write / Append
  ↓
Process Data
  ↓
Close
```

### File Modes

```text
r → Read
w → Write / Overwrite
a → Append
x → Create
```

### Reading

```text
read()       → Complete remaining content
read(n)      → n characters
readline()   → One line
readlines()  → Lines as a list
for loop     → Line-by-line processing
```

### Writing

```text
write()      → Write a string
writelines() → Write multiple strings
```

### File Pointer

```text
tell() → Current position
seek() → Change position
```

### File Management

```text
os       → Operating-system file operations
pathlib  → Modern path handling
```

### Safe File Handling

```python
with open("notes.txt", "r", encoding="utf-8") as f:
    data = f.read()
```

This approach keeps file handling clean, readable, and safe.

---

# 🚀 Summary

In this chapter, I learned how Python can interact with files and use them for persistent data storage.

I learned:

- What File I/O is
- Why File Handling is required
- Advantages of File Handling
- Text and Binary Files
- Relative and Absolute Paths
- Windows Paths and Raw Strings
- Current Working Directory
- `open()` Function
- File Objects
- File Modes
- `r`, `w`, `a`, and `x`
- Text and Binary Modes
- `r+`, `w+`, and `a+`
- Reading Files
- `read()`
- `read(n)`
- `readline()`
- `readlines()`
- Reading using `for` loops
- Writing Files
- `write()`
- `writelines()`
- Newline character `\n`
- Append Mode
- Create Mode
- Closing Files
- `with` Statement
- File Pointer
- `tell()`
- `seek()`
- Encoding
- File Modification
- `replace()`
- File Deletion
- `os` Module
- `pathlib`
- File-related Exceptions
- Exception Handling
- Practical File I/O Programs
- Best Practices
- Common Beginner Mistakes

File handling is an important Python concept because it allows programs to work with **persistent data instead of only temporary variables**.

Understanding File I/O also provides a foundation for working with larger concepts such as **CSV files, JSON files, databases, logs, configuration files, and data processing**.

---

# 📚 Course Information

**Course:** CodeWithHarry Python Course

**Chapter:** 09 - File Input/Output (File I/O)

**Language:** Python

**Topic:** File Handling

**Author:** Sonal Rai