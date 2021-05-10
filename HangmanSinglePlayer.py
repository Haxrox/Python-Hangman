import random
import detectEnglish
import re

def HangmanSinglePlayer():

    #Variables
    guessesTaken = 0
    guessedLetters = []
    WORDS = (open('dictionary.txt').read().splitlines())
    word = random.choice(WORDS)
    A = len(word)
    B = list(word)
    B[0:] = '_' * A
    C = A + 1
    D = C

    #Program

    if A in ('8', '11', '18'):
        print('Okay, I\'m thinking of an ' + str(A) + ' letter word.')

    else:
        print('Okay, I\'m thinking of a ' + str(A) + ' letter word.')

    print('Guess a letter to figure out what word I\'m thinking of!\nYou get ' + str(C) +' tries to guess the word.')
    # print(word)
    print(' '.join(B))

    while guessesTaken < D:
        guess = input().upper()

        if guess in guessedLetters:
            print('You have already guessed that letter. \nGuess a different letter or solve the puzzle.')
            guess = input().upper()

        if guess == 'SOLVE':
            print('Okay, type out the full word if you want to solve.')
            solveResponse = input().upper()

            if solveResponse == word:
                print('Good job! ' + word + 'Was the word I was thinking of. You solved the puzzle in ' + str(guessesTaken) + ' tries')
                print('Do you want to play again?')
                A = input.upper()

                if A in ('YES','Y'):
                    from Hangman import __gameMode__

            if solveResponse != word:
                print('Sorry, the word you guessed was not the word I was thinking of. Guess a letter.')
                guess = input().upper()

                while guess in ('SOLVE'):
                    print('Sorry you cannot solve again. Guess a letter.')
                    guess = input().upper()

        while not guess.isalpha():
            print('Guess a letter! Not a number!')
            guess = input().upper()

        while len(guess) > 1:
            print('Guess one letter only or solve the puzzle!')
            guess = input().upper()

        guessedLetters.append(guess)
        guessesTaken = guessesTaken + 1
        C = C - 1

        for char in range(len(word)):

            if guess == word[char]:
                B[char] = guess

        if guess not in word:
            print('The letter you guessed is not in the word I\'m thinking of.\nYou have ' + str(C) + ' tries left to either guess another letter or solve the puzzle.')

        if guess in word:
            print('The letter you guessed is in the word I\'m thinking of. \nYou have ' + str(C) + ' tries left to guess another letter or solve the puzzle.')

        print(' '.join(B))  

        if B == list(word):
            break

    if B == list(word):
        print('Good job! ' + word + ' was the word I was thinking of!\nYou guessed the word in ' + str(guessesTaken) + 'tries')

    else:
        print('Sorry the word I was thinking of was ' + word + '.')

    print('Do you want to play again?')
    A = input().upper()

    if A in ('YES', 'Y'):
        from Hangman import __gameMode__

    
              
                                            
