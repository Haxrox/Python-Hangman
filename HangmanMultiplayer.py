

NotInService = ['Sorry! You can\'t play Multiplayer Hangman!',
                'Multiplayer Hangman is currently underdevelopment and won\'t',
                'be complete in a bit. Please play one of the developed gamemodes',
                'such as, Single Player Hangman.'
                ]

for line in NotInService:
    print(line, sep='\n')

from Hangman import __gameMode__
