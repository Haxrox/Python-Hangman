import HangmanSinglePlayer
import sys

def greeting():
    print('Hello! What is your name?')
    

def gameMode():
    print('Okay ' + myName + ', Do you want to play Single Player Hangman or Multiplayer Hangman?')
    A = input().upper()

    if A in 'SINGLE PLAYER':
        print('Do you know how to play single player hangman?')
        A = input().upper()

        if A in ('YES', 'Y'):
            HangmanSinglePlayer.HangmanSinglePlayer()

    if A in ('NO', 'N'):
        print('Okay then. Goodbye')
        sys.exit

    if A in ('YES', 'Y'):
        print('Great! Which mode of Hangman do you want to play? Singer Player or Multiplayer?')

        if A in 'SINGLE PLAYER':
            print('Do you know how to play single player hangman?')
            A = input().upper()

        if A in ('YES', 'Y'):
            HangmanSinglePlayer.HangmanSinglePlayer()

    else:
        gameMode()


greeting()
myName = input()
gameMode()
    
