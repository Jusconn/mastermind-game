# Justin Chacon
# CSC 110
# Mastermind Project

# The following code plays the game of Mastermind, where the computer comes up with a secret code of four colors
# and the user has ten tries to guess the code before they lose the game. Hints are given after each guess, based
# on if the user got any of the colors and placements correct. Upon winning or losing the player will be asked if they
# want to play again.

# Import libraries needed(random for secretCode)
import random

# global variable for colors
ALL_COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']


# function to generate secret code
def secretCode():
    secret = []
    for i in range(4):
        color = ALL_COLORS[(random.randint(0, 5))]
        secret.append(color)
    print('The secret code has been chosen. You have 10 tries to guess the code.\n')
    return secret

# repeatedly asks user to guess until valid guess is made, then displays guess
def validNumber():
    while True:
        try:
            colorint = int(input('Guess color: '))
            if colorint in range(6):
                break
            else:
                print('Invalid guess, try again:')
        except ValueError:
            print('Invalid number, try again:')
    return colorint

def validChoice():
    while True:
        choice = input("Would you like to play again? (Y/N)")
        if choice in 'yYnN':
            break
        else:
            print('Invalid choice, try again')
    return choice


def makeGuess():
    print('''-----------------------------
Make a guess of four colors: 
0  -  red
1  -  orange
2  -  yellow
3  -  green
4  -  blue
5  -  purple
-----------------------------''')
    # takes valid guess
    guess = []
    for i in range(4):
        colorint = validNumber()
        guess.append(ALL_COLORS[colorint])

    # displays guess
    print(f'''-----------------------------
Your guess is:
{guess}''')
    return guess


# Checks guess for hints to give
def checkGuess(guess, secret):
    clue = []
    # creates a set to keep track of positions that have already been awarded a hint
    clueGiven = set()
    # ends game if code is guessed
    if guess == secret:
        clue.append(3)
        return clue
    else:
        # checks for correct color correct position
        for i in range(len(guess)):
            if guess[i] == secret[i]:
                clue.append(2)
                clueGiven.add(i)
        # Check for correct color but incorrect position
        for i in range(len(guess)):
            if guess[i] != secret[i] and guess[i] in secret:
                for j in range(len(secret)):
                    if secret[j] == guess[i] and j not in clueGiven:
                        clue.insert(0, 1)
                        clueGiven.add(j)
                        break

    return clue


# asks to play again
def playAgain():
    while True:
        choice = input('Would you like to play again? (Y/N)')
        if choice in 'yY':
            return True
        elif choice in 'nN':
            print("\nThank you for playing.  Good-bye!")
            return False
# executes game
def main(seedValue):
    random.seed(seedValue)
    replay = True
    while replay:
        #sets game start
        lives = 10
        secret = secretCode()
        for i in range(lives):
            #gameplay loop
            guess = makeGuess()
            clue = checkGuess(guess, secret)
            lives -= 1
            if 3 in clue:
                print(f'''
                Correct! You finished in {10 - lives} guesses
                ''')
                replay = playAgain()
                break
            print(f'\nYour clue is: {clue}\n')
            if lives != 0:
                print(f'You have {lives} guesses left')
            else:
                print(f'''No more guesses, the hidden colors were:

    {secret}
    ''')
                replay = playAgain()
    return
