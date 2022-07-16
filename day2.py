#Data Types, Numbers, Operations, Type Conversion, F-strings
# Data Types - String, Integers Float, Boolean
# String- Pulling out a number from a string is called "subscripting". 
#         The number in the square [] bracket determines the character that is getting pulled out. The index starts from 0

print("Hello"[0])
    H
#When you put integers in a parentheses, the computer assumes it is a string and concatenates the numbers instead of doing a sum:

print("123" + "456")
    123456


#Integers: Whole numbers without decimals
print(123 + 456)
579

in python you can replace large integer commas eg. 123,456,789 (to make it more human-readable), with underscores: 123_456_789
print(123_456_789)
    123456789


Float: numbers with decimals. short for floating point number eg. 3.14159

print(3.14 + 5.66)
8.8


Boolean: True or False. capital first letters and no quotes


Type Error, Type Checking and Type Conversion:

You will get a type error if you try to concatenate a string and an integer. eg.:
num_char = len(input("what is your name? "))
print("your name has " + num_char + " characters.")
what is your name? phyllis
    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    ~\AppData\Local\Temp/ipykernel_6404/3655958709.py in <module>
        1 num_char = len(input("what is your name? "))
    ----> 2 print("your name has " + num_char + " characters.")

TypeError: means that  you can only concatenate str (not "int") to str

type() function: checks the type of data between the brackets.
num_char = len(input("what is your name? "))
print(type(num_char))
what is your name? phyllis
    <class 'int'>


Type conversion or type casting: changes one data from one data type to another. e.g.: turning an integer into a string.
num_char = len(input("what is your name? "))
new_num_char = str(num_char)
print("your name has " + new_num_char + " characters.")
what is your name? phyllis
    your name has 7 characters.

a = 123
print(type(a))
    <class 'int'>

a = str(123)
print(type(a))
    <class 'str'>

a = float(123)
print(type(a))
    <class 'float'>

print(678 + float(345.5768))
    1023.5768

print(str(70) + str(80))
    7080

Instructions: Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
Your program should work for different inputs. e.g. any two-digit number.

# Don't change the code below:
two_digit_number = input("Type a two digit number: ")
# Don't change the code above ^
print(int(two_digit_number[0]) + int(two_digit_number[1]))
    Type a two digit number: 67
    13

# or:
two_digit_number = input("Type a two digit number: ")
first_dig = two_digit_number[0]
second_dig = two_digit_number[1]
result = int(first_dig) + int(second_dig)
print(result)
    Type a two digit number: 56
    11

Mathematical operations in .py
# addition:
3 + 4
    7
#Subtraction:
7 - 4
    3
#multiplication:
7*3
    21
#division: the answer is a float
6/3
    2.0
#exponents: raising a number to the power of n:
2**8
    256

when using more than one formula in a function, then the priority order of operation (PEMDAS) applies: Parentheses, Exponents, Multiplication, Division, Addition, Subtraction:or (PEMDASLR) because it reads from left to right.
print(3*3+3/3-3)
    7.0
print(3*(3+3)/3-3)
    3.0

#BMI Calculator
Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
The BMI is a measure of some's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.
The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆
#Write your code below this line 👇
new_height = float(height)
new_weight = int(weight)
bmi = new_weight / ((new_height)**2)
print(bmi)
    enter your height in m: 1.6
    enter your weight in kg: 100
    39.06249999999999

# if you want the answer as an integer, not a float:
# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆
#Write your code below this line 👇
new_height = float(height)
new_weight = int(weight)
bmi = new_weight / ((new_height)**2)
print(int(bmi))
    enter your height in m: 1.6
    enter your weight in kg: 100
    39


# Number Manipulation and f-Strings in Python
# round()function: Used to round off numbers

# normally division will give you a float result.
print(8/3)
    2.6666666666666665

# when you use the round() function, the result is returned as aa rounded off integer
print(round(8/3))
    3

#to round off the result into two decimal places:
print(round(8/3, 2))
    2.67

print(round (2.666666, 2))
    2.67

#floor division: gives you an integer result
print(8//3)
    2


#Manipulation 
result = 4/2
print(result/2)
    1.0

8/3
    2.6666666666666665
8//3
    2
# % :This will give the remainder or the remaining numerator: 
    #8/3 in fraction is 2 2/3:
    
8%3
    2

#to manipulate a value based on its previous value:

score = 0
score *=1
print(score)
    0

score = 0
score +=1
print(score)
    1

score = 0
score /=1
print(score)
    0.0

score = 2
score **=0
print(score)
    1

f-Strings:Literal String Interpolation or more commonly as F-strings (because of the leading f character preceding the string literal), make string interpolation simpler. To create an f-string, prefix the string with the letter “ f ”. The string itself can be formatted in much the same way that you would with str.format(). F-strings provide a concise and convenient way to embed python expressions inside string literals for formatting. Using the f-strings helps eliminate the extra work of insterting str. into different data types.

score = 1
height = 1.8
win = True
print(f"Your score is {score}, your height is {height}, you are winning {win}")
Your score is 1, your height is 1.8, you are winning True

# Age Calculator:
# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
# It will take your current age as the input and output a message with our time left in this format:
# You have x days, y weeks, and z months left.
# Where x, y and z are replaced with the actual calculated numbers.

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

months_left = (90 -int(age))* 12
weeks_left = (90 -int(age)) * 52
days_left = (90 -int(age)) * 365
print(f"you have {days_left} days, {weeks_left} weeks, and {months_left} months left. ")
    What is your current age? 89
    you have 365 days, 52 weeks, and 12 months left. 
    print(6 + 4 / 2 - (1*2))
    6.0


#project: Tip Calculator

print("Welcome to the tip calculator.")
total_bill = input("what was the total bill? ")
bill = float(total_bill)
total_tip = int(input("what percentage tip would you like to give? "))
tip = float(bill * (total_tip/100))
people_sharing_bill = input("How many people will be splitting the bill? ")
people = int(people_sharing_bill)
bill_per_person = float((bill +tip)/people)
print(f"Each person will pay: ${round(bill_per_person,2)}")
    Welcome to the tip calculator.
    what was the total bill? 100
    what percentage tip would you like to give? 13
    How many people will be splitting the bill? 7
    Each person will pay: $16.14