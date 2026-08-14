#The game() function in a program lets a user play a game and returns the score as an integer.
#You meed to read a file 'Hi-score.txt which is either blank or contains the prevoious Hi-score whenever the
#game() function breaks the Hi-score

import random

def game():
    print("You are playing the game....")
    score = random.randint(1, 100)

    with open("high_score.txt") as file:
        highscore = file.read()

        if(highscore !=""):
            highscore = int(highscore)
        else:
            highscore = 0

    print(f"Your score: {score}")

    if (score>highscore):
        with open("high_score.txt", "w") as file:
            file.write(str(score))

    return score

game()
