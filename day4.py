# Randomization and Python Lists
    # Random Module
    # Understandin the Offset and Appending Items
    # Index Errors and Working with Nested Lists

# References: 
# Mersenne Twister: Python uses the Mersenne Twister as the core generator:
#                  - https://docs.python.org/3/library/random.html
#                  - https://en.wikipedia.org/wiki/Mersenne_Twister
# Khan Academy: PseudoRandom Number generators:
#                  - https://khanacademy.org/computing/computer-science/cryptography/crypt/v/random-vs-pseudorandom-number-generators
#                  - https://askpython.com

# Randomization helps to create programs that are unpredictable in nature.
# To tap into the random module we have to import it:

from multiprocessing import parent_process
from platform import python_branch
import random
from typing import ParamSpecArgs
import my_module

c = random.randint(100, 200)
#returns a random integer between 100 and 200 (both inclusive). It will also raise an error if a > b, 
#   eg. c = random.randint(200,100)

# (100, 200) represents the range of integers being specified for randomization
random_integer = random.randint(1, 10)
print(random_integer)
    # This will print an random number verytime, between 1 and 10, with 1 and 10 inclusive.

# Generates a random number between i and j
        # a = random.randrange(i, j)
        # try:
        #     b = random.randrange(j, i)
        # except ValueError:
        #     print('ValueError on randrange() since start > stop')

# Module: Every module is responsible for a different functionality in the program. 
# You can create your own modules in different files and call them in a different file altogether. eg:
print(my_module.pi)
    # 3.14159246

# Generating Random Floating Point Numbers:
#random.random() -> returns the next random floating point numner between [0.0 to 1.0] but does not include 1.0
random_float = random.random()
print(random_float)
        #  0.5177554813289391
    #  This will print random numbers between 0.0 and 1.0, but not inclusive of 1.0

# printing a random number between 0 and 5:
# random.random() will generate floating point numbers between 0.0 and 1.0, without including 1.0. 
# Therefore, if we were to multiply the random_float by 5, then we would get the random floats including but not equal to 5
random_float = random.random()
random_float * 5  #  This will generate floats between 0.000000 to 4.999999...
    # 4.3426445187734855

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}.")


# Instructions
# You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".
# Important, the first letter should be capitalised and spelt exactly like in the example e.g. Heads, not heads.
# When you run the code, just use a random number as the seed. e.g. 67346 It doesn't matter what you chose, it's only for our testing code to check your work.
# There are many ways of doing this. But to practice what we learnt in the last lesson, you should generate a random number, either 0 or 1. 
# Then use that number to print out Heads or Tails.
# e.g. 1 means Heads 
#      0 means Tails
# Example Output
    # Heads
    #or
    # Tails

#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
import random
# 🚨 Don't change the code below 👇
# test_seed = int(input("Create a seed number: \n"))
# random.seed(test_seed)
 # 🚨 Don't change the code above 👆 It's only for testing your code.
	 
#Write the rest of your code below this line 👇
random_coin_toss = random.randint(0, 1)
if random_coin_toss == 1:
    print("Heads")
else:
    print("Tails")

# Python Lists
# A list is a data structure. It is a way of organizing and storing data in python
# a = "hello" or b = 12, is an example of a simple variable where the variable is assigned one value- 
# when trying to create a more complex/grouped pieces of data like listing all countries in a data set called "countries", etc., 
# then we get into lists where the values have a connection to each other and are therefore stored in one variable. eg.
# fruits = [item1, item2, item3]
fruits = ["cherry", "apple", "pear"]
print(fruits[0])
    # cherry
# lists can have mixed data types, eg, integers, boolean vars, strings
# lists always open and close with a square bracket [] and the items are separated by a comma.
# to count from the right, or the beginning of the list, you start with [0], to count from the end of the list, you count from [-1].

fruits = ["cherry", "apple", "mango", "banana", "kiwi", "tomato", "tomatillo", "orange", "lemon"]
print(fruits[-1])
    # lemon
print(fruits[-3])
    # tomatillo

fruits = ["mango", "banana", "peach", "plum", "passion fruit", "guava", "plumcot", "loquat"]
print(len(fruits))
last_index = len(fruits)
print(fruits[last_index - 4])
print(fruits[7])
        # 8
        # passion fruit
        # loquat

# You can also change/replace the data in a list:
fruits[3] = "guava"
print(fruits)
    #  ['cherry', 'apple', 'mango', 'guava', 'kiwi', 'tomato', 'tomatillo', 'orange', 'lemon']


# To add an exactly one item to the end of the list, use the append()
fruits.append("banana")
print(fruits)
    # ['cherry', 'apple', 'mango', 'guava', 'kiwi', 'tomato', 'tomatillo', 'orange', 'lemon', 'banana']

# To add more than one item to the end of the list, use extend()
fruits.append(["plantain", "loquats", "pineapple"])
print(fruits)
    # ['cherry', 'apple', 'mango', 'guava', 'kiwi', 'tomato', 'tomatillo', 'orange', 'lemon', 'banana', 'plantain', 'loquats', 'pineapple']

#we can directly convert a string into a list by separating out the commas using str.split(',') eg.
str_inp = "Hello,from,the,other,side"
op = str_inp.split(',')
print(op)
    #  ['Hello', 'from', 'the', 'other', 'side']

# Python Random Choice() method: returns a random element from a list:
import random
my_list = ["apple", "banana", "cherry"]
print(random.choice(my_list))

# Banker Roulette- Who will Pay the Bill?
# Instructions
# You are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.
### Important: You are not allowed to use the choice() function.
# Line 8 splits the string names_string into individual names and puts them inside a List called names. For this to work, you must enter all the names as names followed by comma then space. e.g. name, name, name
# When you run the code, just use a random number as the seed. e.g. 67346 It doesn't matter what you chose, it's only for our testing code to check your work.

# Example Input
# Angela, Ben, Jenny, Michael, Chloe
# Note: notice that there is a space between the comma and the next name.

# Example Output
# Michael is going to buy the meal today!

# Hint
# You might need the help of the len() function.
import random
# 🚨 Don't change the code below 👇
# test_seed = int(input("Create a seed number: "))
# random.seed(test_seed)
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆
#Write your code below this line 👇

# eg. names_string = "Jim,Julia,Peter,George,Georgina,Georgette,Georgetta"

### Not allowed to use the choice() solution for this case :) ###
name_split = names_string.split(',')
random_name = random.choice(name_split)
print(f"{random_name} is going to buy the meal today!")

# Alternate solution: Using the len() function to solve Banker's Roulette:
import random
names_string = input("List everyone's names, separated by a comma. ")
names = names_string.split(",")
#print(names[0,x])
# Get the total number of names in the list:
# the len() can be used to get the number of characters in a string or the number of elements in a list
#print(len(names)) <-- this will be an integer
#random.randint(0,x) where x is the last item in the list. where the first position is 0 and the last position is usually -1 of the total items in the list.
num_items = len(names)
random_choice = random.randint(0, num_items - 1)
person_responsible = names[random_choice]
# print(f"{person_responsible} is going to pay today!") or 
print(person_responsible + " is going to but the meal this afternoon!")


# Index Errors and Working with Nested Lists

# IndexError: list index out of range
# This occurs when you try to get an index larger than the items on the list. eg.
fruits = ["mango", "banana", "peach", "plum", "passion fruit"]
print(len(fruits))
    # 5
# so the last index will be 4 in this case. If you try to get index 5 out of the list, it will return an index error
print(fruits[5])
        # Traceback (most recent call last):
        # File "<string>", line 5, in <module>
        # IndexError: list index out of range


# Nested Lists: List within a list
#dirty_dozen = ["strawberries", "spinach", "kale", "nectarines", "apples", "grapes", "peaches", "cherries", "pears", "tomatoes", "celery", "potatoes"]
# This list above has both fruits and vegetables. so we can further separate them as such.
fruits = ["strawberries", "nectarines", "apples", "grapes", "peaches", "cherries", "pears"]
vegetables = ["spinach", "kale", "tomatoes", "celery", "potatoes"]

# We can now insert the fruit and vegetables into a list called dirty_dozen:
dirty_dozen = [fruits, vegetables]
print(dirty_dozen)
    # [['strawberries', 'nectarines', 'apples', 'grapes', 'peaches', 'cherries', 'pears'], ['spinach', 'kale', 'tomatoes', 'celery', 'potatoes']]
# The reason there are now two brackets is because there are two lists (fruits, vegetables) inside a new list (dirty_dozen)

# 


# To print item on the list index[x], at index[y]:
    # print(dirty_dozen[x][y]) where x represents the index of the list and y represents the index of the item.
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen = [fruits, vegetables]
print(dirty_dozen[1][1])
    # kale
print(dirty_dozen[0][4])
    # peaches


# Treasure Map
# Instructions
# You are going to write a program that will mark a spot with an X.
# In the starting code, you will find a variable called map.
# This map contains a nested list. When map is printed this is what the nested list looks like:
# [['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]

# This is a bit hard to work with. 
# we've used this line of code print(f"{row1}\n{row2}\n{row3}" to format the 3 lists to be printed as a 3 by 3 square, each on a new line. 
# ['⬜️', '⬜️', '⬜️']

# ['⬜️', '⬜️', '⬜️']

# ['⬜️', '⬜️', '⬜️']
# Now it looks a bit more like the coordinates of a real map:
# Your job is to write a program that allows you to mark a square on the map using a two-digit system. 
# The first digit is the vertical location and the second digit is the horizontal location. 
# So an input of 23 should place an X at the position shown below:
# x= map[2][3]
#      1      2      3
# 1 ['⬜️', '⬜️', '⬜️']

# 2 ['⬜️', '⬜️', '⬜️']

# 3 ['⬜️', 'x', '⬜️']
# First, your program must take the user input and convert it to a usable format.
# Next, you need to use that input to update your nested list with an "x". Remember that your nested list map actually looks like this: [['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']].
# Example Input 1
# column 2, row 3 would be entered as:
# 23
# Example Output 1
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', 'x', '⬜️']

        # Hint
        # Remember that Lists start at index 0!
        # map is just a variable that contains a nested list. It's not related to the map function in Python.
        # Remember that nested lists are accessed from out to in. So if list=[[A,B,C],[E,F,G]] then E = list[1][0]
        # Check that you haven't accidentally added extra spaces and the X is a capital X with a single quote around it. 

# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
column = int(position[0]) - 1
row = int(position[1]) - 1
map [column][row] = "X"

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")


# Project: Rock, Paper, Scissors
# What Do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors
# rock wins against scissors
# scissors wins against paper 
# paper wins against rock

import random
user_choice = input(" What Do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors \n")
computer_choice = random.randint(0, 2)
print(f"Computer chose {computer_choice}")
tool_items = ["rock", "paper", "scissors"]
# Rules of the game:
# rock beats scissors, scissors beat paper, paper beats rock
if user_choice <= 2 and user_choice >= 0:
    print(f"You chose {user_choice}")
    computer = computer_choice
    print(f"Computer chose {computer}")
    
    if user_choice == 0 and computer == 2:
        print("You win.")
    elif user_choice == 2 and computer == 1:
        print("You win.")
    elif user_choice == 1 and computer == 0:
        print("You win.")
    elif user_choice == computer_choice:
        print("It is a draw.")
    else: 
        print("You lose")
else:
    print("Not a valid option. Choose a whole integer between 0 and 2. You lose this round.")
       
#         Choose a whole number between zero and two. 0, 1, or 2: 0
#         You chose 0
#         Computer chose 1
#         You lose

