import random
import os
import time
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

choices = ["snake", "water", "gun"]

emoji = {
    "snake": "🐍",
    "water": "💧",
    "gun": "🔫"
}

user_score = 0
computer_score = 0
draw_score = 0


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def title():
    print(Fore.CYAN + "=" * 45)
    print("      🐍 SNAKE WATER GUN GAME 🔫")
    print("=" * 45)


def rules():
    print(Fore.YELLOW + "\nRules")
    print("-" * 30)
    print("🐍 Snake drinks Water")
    print("💧 Water defeats Gun")
    print("🔫 Gun kills Snake\n")


while True:

    clear()
    title()

    print(Fore.GREEN + f"Your Score      : {user_score}")
    print(Fore.RED + f"Computer Score  : {computer_score}")
    print(Fore.YELLOW + f"Draws           : {draw_score}")

    print()

    rules()

    print("Choose")
    print("1. Snake 🐍")
    print("2. Water 💧")
    print("3. Gun 🔫")

    choice = input("\nEnter choice (1-3): ")

    if choice not in ["1", "2", "3"]:
        print(Fore.RED + "\nInvalid Choice!")
        time.sleep(2)
        continue

    user = choices[int(choice) - 1]

    print("\nComputer is choosing", end="")

    for i in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)

    print()

    computer = random.choice(choices)

    print(f"\nYou      : {emoji[user]} {user.capitalize()}")
    print(f"Computer : {emoji[computer]} {computer.capitalize()}")

    print()

    if user == computer:
        print(Fore.YELLOW + "🤝 Match Draw!")
        draw_score += 1

    elif (
        (user == "snake" and computer == "water")
        or (user == "water" and computer == "gun")
        or (user == "gun" and computer == "snake")
    ):
        print(Fore.GREEN + "🎉 You Win This Round!")
        user_score += 1

    else:
        print(Fore.RED + "💻 Computer Wins This Round!")
        computer_score += 1

    print()

    again = input("Play Again? (yes/no): ").lower()

    if again != "yes":
        break

clear()

title()

print("\n🏆 FINAL SCORE\n")

print(Fore.GREEN + f"You       : {user_score}")
print(Fore.RED + f"Computer  : {computer_score}")
print(Fore.YELLOW + f"Draw      : {draw_score}")

print()

if user_score > computer_score:
    print(Fore.GREEN + "🎉 Congratulations! You Won the Match!")

elif computer_score > user_score:
    print(Fore.RED + "💻 Computer Won the Match!")

else:
    print(Fore.YELLOW + "🤝 Match Tied!")
