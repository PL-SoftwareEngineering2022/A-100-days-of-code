# Conditional Statements and Logical Operators
    # 1. Control Flow with if/else and Conditional Operators
    # 2. Nested if and elif statements
    # 3. Multiple if statements in succession
    # 4. Logical operators

#Conditional statements: Control Flow with If/else and Conditional Operators
        # if condition:
        #     do this
        # else:
        #     do this

print("Welcome to the rollercoaster")
height = int(input("what is you height in cm? "))
if height > 60:
    print("You can ride the rollercoaster.")
else:
    print("sorry, you are too short for this ride.")
    # Welcome to the rollercoaster
    # what is you height in cm? 60
    # sorry, you are too short for this ride.

print("Welcome to the rollercoaster")
height = int(input("what is you height in cm? "))
if height >= 60:
    print("You can ride the rollercoaster.")
else:
    print("sorry, you are too short for this ride.")
        # Welcome to the rollercoaster
        # what is you height in cm? 60
        # You can ride the rollercoaster.

#comparison operators: 
    # > Greater than
    # < Lesser than
    # >= Greater than or equal to
    # <= Lesser than or equal to
    # == Equal to
    # != Not equal to

    # To note: 
    # = is used for assignment; assigning value to a variable
    # eg. a = apples, b = oranges
    # == is used to check equality
    # eg. if height == 120 ...  


# Instructions: Even Numbers
# Write a program that works out whether if a given number is an odd or even number.
# Even numbers can be divided by 2 with no remainder.
# e.g. 86 is even because 86 ÷ 2 = 43
# 43 does not have any decimal places. Therefore the division is clean.
# e.g. 59 is odd because 59 ÷ 2 = 29.5
# 29.5 is not a whole number, it has decimal places. Therefore there is a remainder of 0.5, so the division is not clean.

# The modulo is written as a percentage sign (%) in Python. It gives you the remainder after a division.
# e.g. 6 ÷ 2 = 3 with no remainder.
# therefore: 6 % 2 = 0
# 5 ÷ 2 = 2 x 2 + 1, remainder is 1.
# therefore: 5 % 2 = 1
# 14 ÷ 4 = 3 x 4 + 2, remainder is 2.
# therefore: 14 % 4 = 2 

   
# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if number % 2 == 0 :
    print("This is an even number")
else:
    print("This is an odd number")
    # Which number do you want to check? 34
    # This is an even number

# Nested if and elif statements:
# if condition:
#     if another condition:
#         do this
#     else:
#         do this
# else:
#         do this

print("Welcome to the rollercoaster")
height = int(input("what is you height in cm? "))
if height >= 60:
    print("You can ride the rollercoaster.")
    age =int(input("what is your age? "))
    if age <= 18:
        print("please pay $7.00")
    else:
        print("please pay $12.00")
else:
    print("sorry, you are too short for this ride.")
        # Welcome to the rollercoaster
        # what is you height in cm? 67
        # You can ride the rollercoaster.
        # what is your age? 56
        # please pay $12.00

# if / elif /else : used when you want to construct a more complex if conditional statement.
#     if condition1:
#         do A
#     elif condition2:
#         do B
#     else:
#         do C

print("Welcome to the rollercoaster")
height = int(input("what is you height in cm? "))
if height >= 60:
    print("You can ride the rollercoaster.")
    age =int(input("what is your age? "))
    if age <= 12:
        print("please pay $5.00")
    elif age <= 18:
        print("please pay $7.00")
    else:
        print("please pay $12.00")
else:
    print("sorry, you are too short for this ride.")
        # Welcome to the rollercoaster
        # what is you height in cm? 65
        # You can ride the rollercoaster.
        # what is your age? 11
        # please pay $5.00

# BMI 2.0 Calculator:
# Instructions
# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
# It should tell them the interpretation of their BMI based on the BMI value.
# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.
# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):
    # Hint
    # Try to use the exponent operator in your code.
    # Remember to round your result to the nearest whole number.
    # Make sure you include the words in bold from the interpretations.

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
bmi = round(weight/((height)**2), 1)

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight")
elif bmi <= 25.0:
    print(f"Your BMI is {bmi}, you have a normal weight")
elif bmi <=30.0:
    print(f"Your BMI is {bmi}, you are slightly overweight")
elif bmi <= 35.0:
    print(f"Your BMI is {bmi}, you are obese")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")
        # enter your height in m: 1.5
        # enter your weight in kg: 88
        # Your BMI is 39.1, you are clinically obese.

# Leap Year Exercise
# 💪This is a Difficult Challenge 💪
# Instructions
# Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February. The reason why we have leap years is really fascinating, this video does it more justice:
# https://www.youtube.com/watch?v=xX96xng7sAE
# This is how you work out whether if a particular year is a leap year.
# on every year that is evenly divisible by 4 
# **except** every year that is evenly divisible by 100 
# **unless** the year is also evenly divisible by 400
# e.g. The year 2000:
# 2000 ÷ 4 = 500 (Leap)
# 2000 ÷ 100 = 20 (Not Leap)
# 2000 ÷ 400 = 5 (Leap!)
# So the year 2000 is a leap year.
# But the year 2100 is not a leap year because:
# 2100 ÷ 4 = 525 (Leap)
# 2100 ÷ 100 = 21 (Not Leap)
# 2100 ÷ 400 = 5.25 (Not Leap)

# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.") 
        # Which year do you want to check? 2026
        # Not leap year.


# Multiple If Statements in Successsion
        # if condition1:
        #     do A
        # if condition2:
        #     do B
        # if condition3:
        #     do C
# if all conditions 1-3 are true, they will all be executed as compared to if/elif/else conditions where only one is executed.
print("welcome to the rollercoaster!")
height = int(input("what is your height in cm? "))
bill = 0
if height>= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age <= 12:
        print("child tickets are $5.")
        bill = 5
    elif age <=18:
        print("Youth tickets are $7.")
        bill = 7
    else:
        print("Adult tickets are 12.")
        bill =12
    wants_photo = input("Do you want a photo taken? y or n. ")
    if wants_photo == "y":
        # bill = bill + 3
        bill += 3
    print(f"Your final bill is ${bill}")
else:
    print("Sorry, you have to be taller to ride the rollercoaster.")
        # welcome to the rollercoaster!
        # what is your height in cm? 135
        # You can ride the rollercoaster!
        # What is your age? 45
        # Adult tickets are 12.
        # Do you want a photo taken? y or n. y
        # Your final bill is $15

# Instructions:
# Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.
# Based on a user's order, work out their final bill.
#     Small Pizza: $15
#     Medium Pizza: $20
#     Large Pizza: $25
#     Pepperoni for Small Pizza: +$2
#     Pepperoni for Medium or Large Pizza: +$3
#     Extra cheese for any size pizza: + $1
# Example Input:
#     size = "L"
#     add_pepperoni = "Y"
#     extra_cheese = "N"
# Example Output:
#     Your final bill is: $28.

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if size == "S":
    bill = 15
    if add_pepperoni == "Y":
        bill +=2
if size == "M":
    bill = 20
    if add_pepperoni == "Y":
        bill +=3
if size == "L":
    bill = 25
    if add_pepperoni == "Y":
        bill += 3
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")
        # Welcome to Python Pizza Deliveries!
        # What size pizza do you want? S, M, or L S
        # Do you want pepperoni? Y or N Y
        # Do you want extra cheese? Y or N N
        # Your final bill is: $17.

#   Alternate solution:
#=========================#
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill +=20
else:
    bill += 25

if add_pepperoni =="Y":
    if size =="S":
        bill +=2
    else:
        bill +=3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is ${bill}.")
        # Welcome to Python Pizza Deliveries!
        # What size pizza do you want? S, M, or L L
        # Do you want pepperoni? Y or N Y
        # Do you want extra cheese? Y or N N
        # Your final bill is $28.

# Logical Operators: checks for multiple conditions in the same line of code
# if condition1 & condition2 & condtion3:
#     do this
# else:
#     do this

# Logical Operators:
#  A & B: both A and B have to be true. If either one is false, then it is evaluated as False
#eg. 
a = 12
a > 15
False
a > 10
True
a > 10 and a <13
True
#  C or D: Used if you only need one of the operators to be True, either C or D
a = 12
a < 11 or a <15
True
#  not E: it reverses the condition. if the true, it gives false and vice versa
a = 12
not a > 15
True

print("welcome to the rollercoaster!")
height = int(input("what is your height in cm? "))
bill = 0
if height>= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age <= 12:
        print("child tickets are $5.")
        bill = 5
    elif age <=18:
        print("Youth tickets are $7.")
        bill = 7
    elif age >=45 and age <=55:
        print("Middle age crisis tickets are free.")
        bill = 0
    else:
        print("Adult tickets are 12.")
        bill =12
    wants_photo = input("Do you want a photo taken? y or n. ")
    if wants_photo == "y":
        # bill = bill + 3
        bill += 3
    print(f"Your final bill is ${bill}")
else:
    print("Sorry, you have to be taller to ride the rollercoaster.")
        # welcome to the rollercoaster!
        # what is your height in cm? 121
        # You can ride the rollercoaster!
        # What is your age? 47
        # Middle age crisis tickets are free.
        # Do you want a photo taken? y or n. y
        # Your final bill is $3

# lower(): the lower function changes all the letters in s a string to lower case:
"Phyllis".lower()
    # 'phyllis'

# count(): the count function gives the number of times a letter occurs in a string:
"Phyllis".count("p")
    # 0
lowercase_name = "Phyllis".lower()
lowercase_name.count("p")
    # 1

"PHYLLIS".count("l")
    # 0
lowercase_name = "PHYLLIS".lower()
lowercase_name.count("l")
    # 2

type("Angelita".count("t"))
    # int

#Love Calculator:
# 💪 This is a Difficult Challenge 💪
# Instructions
# You are going to write a program that tests the compatibility between two people.
# To work out the love score between two people:
# Take both people's names and check for the number of times the letters in the word TRUE occurs. 
# Then check for the number of times the letters in the word LOVE occurs. 
# Then combine these numbers to make a 2 digit number.
# For Love Scores less than 10 or greater than 90, the message should be:

# "Your score is **x**, you go together like coke and mentos."
# For Love Scores between 40 and 50, the message should be:

# "Your score is **y**, you are alright together."
# Otherwise, the message will just be their score. e.g.:

# "Your score is **z**."
# e.g.

# name1 = "Angela Yu"
# name2 = "Jack Bauer"
# T occurs 0 times
# R occurs 1 time
# U occurs 2 times
# E occurs 2 times
# Total = 5

# L occurs 1 time
# O occurs 0 times
# V occurs 0 times
# E occurs 2 times
# Total = 3

# Love Score = 53
# Print: "Your score is 53."

# Example Input 1
# name1 = "Kanye West"
# name2 = "Kim Kardashian"
# Example Output 1
# Your score is 42, you are alright together.

# Example Input 2
# name1 = "Brad Pitt"
# name2 = "Jennifer Aniston"
# Example Output 2

# Your score is 73.

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆
#Write your code below this line 👇

lower_name1 = name1.lower()
lower_name2 = name2.lower()

T = lower_name1.count("t") + lower_name2.count("t")
R = lower_name1.count("r") + lower_name2.count("r")
U = lower_name1.count("u") + lower_name2.count("u")
E = lower_name1.count("e") + lower_name2.count("e")
total1 = T + R + U + E
L = lower_name1.count("l") + lower_name2.count("l")
O = lower_name1.count("o") + lower_name2.count("o")
V = lower_name1.count("v") + lower_name2.count("v")
E = lower_name1.count("e") + lower_name2.count("e")
total2 = L + O + V + E

love_score = str(total1)+ str(total2)
love_score1 = int(love_score)

 # or love_score = int(str(total1)+ str(total2))
if love_score1 < 10 or love_score1 > 90:
    print(f"Your score is {love_score1}, you go together like coke and mentos")
elif love_score1 >= 40 and love_score1 <= 50:
    print(f"Your score is {love_score1}, you are alright together.")
else:
    print(f"Your score is {love_score1}.")

        # Welcome to the Love Calculator!
        # What is your name? 
        # samson
        # What is their name? 
        # delilah
        # Your score is 24.

        # Welcome to the Love Calculator!
        # What is your name? 
        # Barbie
        # What is their name? 
        # Ken doll
        # Your score is 45, you are alright together.

#Treasure Island:
        # Welcome to Treasure Island:
        # Your Mission is to find treasure.
        # left or right. Right = Game Over, Left = continue
        # Swim or wait. Swim = Game over, wait = continue
        # which door? blue and red = game over; Yellow = You win!

print("Welcome to Treasure Island.\nYour mission is to find treasure.")
choice1 =input("Which direction do you want to go? Left or Right: ").lower()

if choice1 == "right":
    print(" You can proceed to the next level.")
    choice2 = input("What do you want to do? Swim or Wait: ").lower()
    if choice2 == "swim":
        print("Game Over!")
    if choice2 == "wait":
        print("You can choose a door to see you prize.")
        choice3 = input("Which door would you like? Red, Yellow or Blue: ").lower()
        if choice3 == "red":
            print("Game over! Nice try.")
        elif choice3 == "blue":
            print("Game over! Nice try.")
        elif choice3 == "yellow":
            print("You win!")
        else:
            print("That door doesn\'t exist. You lose")
else:
    print("Game over!")

        # Welcome to Treasure Island.
        # Your mission is to find treasure.
        # Which direction do you want to go? Left or Right: right
        # You can proceed to the next level.
        # What do you want to do? Swim or Wait: wait
        # You can choose a door to see you prize.
        # Which door would you like? Red, Yellow or Blue: green
        # That door doesn't exist. You lose

        # Welcome to Treasure Island.
        # Your mission is to find treasure.
        # Which direction do you want to go? Left or Right: right
        # You can proceed to the next level.
        # What do you want to do? Swim or Wait: wait
        # You can choose a door to see you prize.
        # Which door would you like? Red, Yellow or Blue: red
        # Game over! Nice try.

        # Welcome to Treasure Island.
        # Your mission is to find treasure.
        # Which direction do you want to go? Left or Right: right
        # You can proceed to the next level.
        # What do you want to do? Swim or Wait: wait
        # You can choose a door to see you prize.
        # Which door would you like? Red, Yellow or Blue: red
        # Game over! Nice try.