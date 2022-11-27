# reference: https://hangmanwordgame.com

#Step 1- How to check the User's Answer
# ===================================== #

word_list = ["aardvark", "baboon", "camel"]
#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
import random
chosen_word = random.choice(word_list)
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter: ").lower()
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")

        # Guess a letter: a
        # Right
        # Right
        # Wrong
        # Wrong
        # Wrong
        # Right
        # Wrong
        # Wrong

# Step 2 - Replacing Blanks with Guesses
# ====================================== #
#  my solution:
import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')
#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
for letter in chosen_word:
  print("_",end='')
guess = input("Guess a letter: ").lower()

#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
for letter in chosen_word:
    if letter == guess:
      print(guess, end='')
    else:
        print("_", end='')

        # Pssst, the solution is aardvark.
        # ________Guess a letter: d
        # ___d____
        
#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

# Alternate Solution:
import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

print(f'Pssst, the solution is {chosen_word}.')
display = []
        # for letter in chosen_word:
        #     display += "_"
        # print(display)
#  we are not actually using the letter  and so this can be represented by a dash as well:
        # for _ in chosen_word:
        #     display += "_"
        # print(display)
#  Alternatively, we can use the range function:
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"
print(display)
guess = input("Guess a letter: ").lower()

for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter

print(display)
        # Pssst, the solution is baboon.
        # ['_', '_', '_', '_', '_', '_']
        # Guess a letter: b
        # ['b', '_', 'b', '_', '_', '_']

#Step 3- checking if the player has won
# ====================================== #

#Step 3

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

#TODO-1: - Use a while loop to let the user guess again. 
# The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). 
# Then you can tell the user they've won.
end_of_game = False # define a new variable here to define when the game should be considered done.

while not end_of_game: # define a while loop and indent the code so that the loop can continue until the condition is met.
    guess = input("Guess a letter: ").lower()

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    print(display)

    #Check if there are no more "_" left in 'display'. Then all letters have been guessed.
    if "_" not in display: # this will check if the blanks are all filled, in which case, the loops is done.
        end_of_game = True
        print("You win.")
        # Pssst, the solution is baboon.
        # Guess a letter: b
        # ['b', '_', 'b', '_', '_', '_']
        # Guess a letter: o
        # ['b', '_', 'b', 'o', 'o', '_']
        # Guess a letter: n
        # ['b', '_', 'b', 'o', 'o', 'n']
        # Guess a letter: a
        # ['b', 'a', 'b', 'o', 'o', 'n']
        # You win.

# Step 4: Keeping Track of the Player's Lives
# =========================================== #
import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
lives = 6
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game == True
            print ("You lose.")
    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])

        # Pssst, the solution is aardvark.
        # Guess a letter: g
        # _ _ _ _ _ _ _ _

        #   +---+
        #   |   |
        #   O   |
        #       |
        #       |
        #       |
        # =========

        # Guess a letter: h
        # _ _ _ _ _ _ _ _

        #   +---+
        #   |   |
        #   O   |
        #   |   |
        #       |
        #       |
        # =========

        # Guess a letter: k
        # _ _ _ _ _ _ _ k

        #   +---+
        #   |   |
        #   O   |
        #   |   |
        #       |
        #       |
        # =========

        # Guess a letter: h
        # _ _ _ _ _ _ _ k

        #   +---+
        #   |   |
        #   O   |
        #  /|   |
        #       |
        #       |
        # =========
        # Guess a letter: e
        # _ _ _ _ _ _ _ k

        #   +---+
        #   |   |
        #   O   |
        #  /|\  |
        #       |
        #       |
        # =========

        # Guess a letter: s
        # _ _ _ _ _ _ _ k

        #   +---+
        #   |   |
        #   O   |
        #  /|\  |
        #  /    |
        #       |
        # =========

        # Guess a letter: m
        # You Lose
        # _ _ _ _ _ _ _ k

        #   +---+
        #   |   |
        #   O   |
        #  /|\  |
        #  / \  |
        #       |
        # =========

#Step 5- Imporving the User Experience - How to add ASCII Art and Improve the UI:
# =============================================================================== #
# reference: https://www.askpython.com/python/python-import-statement
import random
import hangman_art
import hangman_words

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
word_list = hangman_words.word_list # can also be done as: from hangman_words import word_list, this would eliminate: import hangman_words
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
# from hangman_art import logo, stages
# print(logo) or print(stages[lives])
print(hangman_art.logo)
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #TODO-4: - If the user has entered a letter they've already guessed, print a
    if guess in display:
        print("You have already guessed this letter. Please try again.")
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    #Check if user is wrong.
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
        print(f"You have entered the letter {guess}, which is not part of {chosen_word}, so you lose a life.")
        
    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    print(hangman_art.stages[lives])
        # _                                             
        # | |                                            
        # | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
        # | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
        # | | | | (_| | | | | (_| | | | | | | (_| | | | |
        # |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
        #                     __/ |                      
        #                    |___/    
        # Pssst, the solution is kazoo.
        # Guess a letter: k
        # k _ _ _ _

        # +---+
        # |   |
        #     |
        #     |
        #     |
        #     |
        # =========

        # Guess a letter: g
        # You have entered the letter g, which is not part of kazoo, so you lose a life.
        # k _ _ _ _

        # +---+
        # |   |
        # O   |
        #     |
        #     |
        #     |
        # =========

        # Guess a letter: k
        # You have already guessed this letter. Please try again.
        # k _ _ _ _

        # +---+
        # |   |
        # O   |
        #     |
        #     |
        #     |
        # =========
        