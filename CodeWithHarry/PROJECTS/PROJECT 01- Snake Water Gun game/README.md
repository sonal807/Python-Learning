# 🐍 Project 01 - Snake Water Gun Game

> A simple command-line **Snake Water Gun Game** developed in Python as part of the **CodeWithHarry Python Course**.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Project](https://img.shields.io/badge/Project-01-success?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge)

---

# 📖 About

This project is a Python implementation of the classic **Snake, Water, Gun** game.

The player competes against the computer by choosing **Snake**, **Water**, or **Gun**. The computer randomly selects one of the three options, and the winner is decided according to the game rules.

The game also keeps track of the player's score, the computer's score, and the number of draws until the player decides to quit.

---

# 🎯 Objective

The main objective of this project is to practice Python fundamentals by building a simple command-line game.

This project helped me understand:

- Conditional Statements
- Loops
- Functions
- Dictionaries
- Lists
- Modules
- User Input
- Random Number Generation
- Score Management
- Basic Game Logic

---

# 🎮 Game Rules

| Player | Computer | Winner |
|---------|----------|---------|
| 🐍 Snake | 💧 Water | 🐍 Snake |
| 💧 Water | 🔫 Gun | 💧 Water |
| 🔫 Gun | 🐍 Snake | 🔫 Gun |
| Same Choice | Same Choice | 🤝 Draw |

---

# ✨ Features

- 🎮 Interactive command-line gameplay
- 🤖 Random computer choices
- 🌈 Colorful terminal interface using **Colorama**
- 🐍 Emoji support
- 📊 Live score tracking
- 🤝 Draw counter
- ✅ Input validation
- 🔄 Play Again option
- 🏆 Final winner announcement
- ⏳ Computer thinking animation

---

# 🛠 Technologies Used

- Python 3
- random
- os
- time
- colorama

---

# 📂 Project Structure

```text
Project 01 - Snake Water Gun Game
│
├── snake_water_gun.py
└── README.md
```

---

# ⚙ Modules Used

## 1. random

Used to generate the computer's random choice.

Example

```python
computer = random.choice(choices)
```

---

## 2. os

Used to clear the terminal screen.

Example

```python
os.system("cls" if os.name == "nt" else "clear")
```

---

## 3. time

Used to create small delays for a better user experience.

Example

```python
time.sleep(0.5)
```

---

## 4. colorama

Used to display colorful text in the terminal.

Example

```python
print(Fore.GREEN + "You Win!")
```

---

# 🧠 Concepts Used

This project uses the following Python concepts:

- Variables
- Data Types
- Lists
- Dictionaries
- Functions
- Loops
- Conditional Statements
- User Input
- Modules
- Operators
- String Methods
- Score Management

---

# ▶️ How to Run

## Clone the Repository

```bash
git clone <repository-url>
```

---

## Install Required Package

```bash
pip install colorama
```

---

## Run the Project

```bash
python snake_water_gun.py
```

---

# 🎯 Game Flow

1. The game starts by displaying the title and rules.
2. The player selects Snake, Water, or Gun.
3. The computer randomly selects its choice.
4. Both choices are displayed.
5. The winner of the round is determined.
6. Scores are updated.
7. The player can choose to play another round.
8. The final winner is displayed after exiting.

---

# 🌍 Real-Life Learning Outcomes

By building this project, I learned how to:

- Build a complete command-line application.
- Organize code using functions.
- Use Python modules effectively.
- Validate user input.
- Generate random values.
- Maintain scores using variables.
- Improve terminal output using colors and emojis.
- Apply programming logic to solve real-world problems.

---

# 🚀 Future Improvements

Some features that can be added in future versions:

- Best of 3 Mode
- Best of 5 Mode
- Difficulty Levels
- Sound Effects
- Leaderboard
- Save High Scores
- Multiplayer Mode
- Graphical User Interface (Tkinter)
- Pygame Version

---

# ⭐ Key Takeaways

- Functions improve code organization.
- Random module helps generate unpredictable outcomes.
- Dictionaries simplify data mapping.
- Loops allow continuous gameplay.
- Input validation makes programs more reliable.
- Small UI improvements create a better user experience.

---

# 📚 Project Information

**Project:** Snake Water Gun Game

**Course:** CodeWithHarry Python Course

**Language:** Python

**Difficulty:** Beginner

**Status:** ✅ Completed

---

# 👨‍💻 Author

**Sonal Rai**

B.Tech CSE Student

Aspiring AI & Machine Learning Engineer

Learning • Building • Improving Every Day 🚀

---

⭐ *This project was built as part of my Python learning journey through the CodeWithHarry Python Course.*