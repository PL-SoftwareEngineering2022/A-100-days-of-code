# Functions, Code Blocks and While Loops
# Reference: https://docs.python.org/3/library/functions.html

# Defining Functions
        # def myfunctions():
            # Do this
            # Then do this
            # Finally do this
# to make our own functions:
# 1. start out with the keyword "def" to create or define the function, 
# 2. then give the function a name.
# what differentiates a variable from a function is the parentheses.
# the colon helps to define that everything that comes after that line and is indented is part of the function.
# 3. Calling the functions so that you can actually use them, this includes printing the name of the function and the parentheses. 
# This will let the computer know to carry out all the functions defined in the function:
        #  my_function()

def my_function():
    print("You say 'hello'")
    print("I say 'goodbye'")
# calling the function: We can define as many functions as needed and then trigger them later, which is termed as calling the function.
# this involves typing the name of the function and parentheses and any necessary inputs.
my_function()
        # You say 'hello'
        # I say 'goodbye'

# Reeborg's world:
# Draw Square
# I want to go home!
# Write a program that makes Reeborg go home.
# What you need to know
# The function move().
# Difficulty level: 1
# A robot located at (x, y) = (3, 1) carries no objects.
# Goal to achieve:
# The final position of the robot must be (x, y) = (1, 1)
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_around():
    turn_left()
    turn_left()

turn_left()
move()
turn_right()
move()
turn_right()
move()
turn_right()
move()
turn_around()

        # Reeborg says: I'm done!
        # Reeborg is at the correct x position.
        # Reeborg is at the correct y position.

# Hurdle 1 challenge:
# Hurdles race
# Reeborg has entered a hurdles race. Make him run the course, following the path shown.
# What you need to know
# The functions move() and turn_left().
# Difficulty level: 2
# More advanced:
# You may have noticed that your solution has some repeated patterns. If you know how to define functions, define a function named jump() and use it to simplify your program.
# Difficulty level: 3
# A robot located at (x, y) = (13, 1) carries no objects.
# Goal to achieve:
# The final position of the robot must be (x, y) = (13, 1)

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for number in range(6):
    jump()

        # Reeborg says: I'm done!
        # Reeborg is at the correct x position.
        # Reeborg is at the correct y position.

# Indentation:
# in Python indentation can be done with either spaces or tabs
# reference: https://python.org/dev/peps/pep-0008/#tabs-or-spaces
# Spaces are the preferred indentation method.
# Tabs should be used solely to remain consistent with code that is already indented with tabs.
# Python disallows mixing tabs and spaces for indentation.

# While Loops:
# while something_is_true:
    # Do something repeatedly
# while the condition is true, go into the loop and do something repeatedly until the condition becomes false.

# Hurdle 1 challenge with while loop:
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

number_of_hurdles = 6
while number_of_hurdles > 0:
    jump()
    number_of_hurdles -= 1
    print(number_of_hurdles)
    # reeborg writes:
    # 5
    # 4
    # 3
    # 2
    # 1
    # 0
        # Reeborg says: I'm done!
        # Reeborg is at the correct x position.
        # Reeborg is at the correct y position.
# Hurdle  2:
# Hurdles race
# Reeborg has entered a hurdle race, but he does not know in advance how long the race is. Make him run the course, following a path similar to the one shown, but stopping at the only flag that will be shown after the race has started.
# What you need to know
# The functions move() and turn_left().
# The condition at_goal() and its negation.
# How to use a while loop.
# Your program should also be valid for world Hurdles 1.
# Difficulty level: 3
# A robot located at (x, y) = (1, 1) carries no objects.
# Goal to achieve:
# The final required position of the robot will be chosen at random.
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def moves():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
while at_goal() != True:
    moves()
        # Reeborg says: I'm done!
        # Reeborg is at the correct x position.
        # Reeborg is at the correct y position.
#  Alternative:
while not at_goal():
    moves()
        # Reeborg says: I'm done!
        # Reeborg is at the correct x position.
        # Reeborg is at the correct y position.

#  for loops are great for when iterating over something 
# and to do something with each thing that you are iterating over.
#  for loops' we are setting ahead of time how many times something is going to run,
#  and it going to stop once it reaches the end of the list of items or the upper bound of the range set.
fruits = ["Apple", "pear", "orange"]
for fruit in fruits:
    print(fruit)

# or:
for n in range(1,6):
    print(n)
#  while loops are best for when you don't care what number in a sequence you are in; 
#  which item you are iterating through in a list and you simply want to carry some 
#  sort of functionality many times until some sort if condition is set. 
#  While loops continue running until thos particular condition switches to false.
#  if the while loop never becomes false, then it becomes an infinite loop.
#  eg. 
#  while 5 > 3:
#     do abc
#  5 is larger than 3 so this while loop will never be false, 
# so the code will run until it crashes or it is stopped.

# Hurdle 3:
# Reeborg has entered a hurdle race. Make him run the course, following the path shown.
# The position and number of hurdles changes each time this world is reloaded.
# What you need to know
# The functions move() and turn_left().
# The conditions front_is_clear() or wall_in_front(), at_goal(), and their negation.
# How to use a while loop and an if statement.
# Your program should also be valid for worlds Hurdles 1 and Hurdles 2.
# Difficulty level: 4
# A robot located at (x, y) = (1, 1) carries no objects.
# Goal to achieve:
# The final position of the robot must be (x, y) = (13, 1)

def turn_right():
    turn_left()
    turn_left()
    turn_left() 
def evade_wall():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
while not at_goal():
    while front_is_clear():
        move()
    while wall_in_front():
        evade_wall()

#  Alternate solution:
while not at_goal():
    if wall_in_front():
        evade_wall()
    else:
        move()

# Hurdle 4:
# Reeborg has entered a hurdle race. Make him run the course, following the path shown.
# The position, the height and the number of hurdles changes each time this world is reloaded.
# What you need to know
# You should be able to write programs that are valid for worlds Around 4 and Hurdles 3, and ot combine them for this last hurdles race.
# Your program should also be valid for worlds Hurdles 1, Hurdles 2 et Hurdles 3
# Difficulty level: 5
# A robot located at (x, y) = (1, 1) carries no objects.
# Goal to achieve:
# The final position of the robot must be (x, y) = (13, 1)

# Conditions:
# at_goal() front_is_clear() right_is_clear() wall_in_front() 
# wall_on_right() object_here() carries_object() is_facing_north()

def turn_right():
    turn_left()
    turn_left()
    turn_left() 
def evade_wall():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
        
while not at_goal():
    if wall_in_front():
        evade_wall()
    else:
        move()

# Day 6 Project: Escaping the Maze
# Lost in a maze
# Reeborg was exploring a dark maze and the battery in its flashlight ran out.
# Write a program using an if/elif/else statement so Reeborg can find the exit. The secret is to have Reeborg follow along the right edge of the maze, turning right if it can, going straight ahead if it can’t turn right, or turning left as a last resort.
# What you need to know
# The functions move() and turn_left().
# Either the test front_is_clear() or wall_in_front(), right_is_clear() or wall_on_right(), and at_goal().
# How to use a while loop and if/elif/else statements.
# It might be useful to know how to use the negation of a test (not in Python).
# Difficulty level: 4
# A robot located at (x, y) = (4, 3) carries no object
# Conditions: at_goal() front_is_clear() right_is_clear() 
#             wall_in_front() wall_on_right() object_here() carries_object() is_facing_north()
# Goal to achieve:
# The final position of the robot must be (x, y) = (6, 4)

def turn_right():
    turn_left()
    turn_left()
    turn_left() 
    
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
# this solution has an edge case that creates an infinite loop. To solve this infinite loop:
def turn_right():
    turn_left()
    turn_left()
    turn_left() 

while front_is_clear():
    move()
turn_left()
    
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()