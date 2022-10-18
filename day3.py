# Conditional Statements, Logical Operators, Code Blocks and Scope
#Conditional statements: If/else
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
#     else:
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
#         do this

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
    print(f"Your BMI is {bmi}  you are underweight")
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

# Multiple If S tatements in Successsion

