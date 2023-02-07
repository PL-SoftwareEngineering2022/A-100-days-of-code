# printing, commenting, debugging, string manipulation and variables
# ==================================================================

#DataType: string

# print() echoes back the string or characters in between the ""
print("something")
    #--> something
print("you\'ve")
    # you've

# Instructions:
# After you have written your code, you should run your program and it should print the following:

        # Day 1 - Python Print Function
        # The function is declared like this:
        # print('what to print')
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")


#Concatenate: join
print("Hello" + "Phyllis")
    # --> HelloPhyllis


#Line Break:
print("Hello Phyllis\nHello phyllis\nhello phyllis")
    #  Hello Phyllis
    #  Hello phyllis
    #  hello phyllis 


#String concatenation:
# Concatenate with space in between- Options: space after Hello, space before phyllis and an empty " " between the two words:
print("hello " + "phyllis")
    # --> hello phyllis
print("hello" + " phyllis")
    #--> hello phyllis
print("hello" + " " + "phyllis")
    # --> hello phyllis


# Instructions:
# When you run your program, it should print the following:

        # Day 1 - String Manipulation
        # String Concatenation is done with the "+" sign.
        # e.g. print("Hello " + "world")
        # New lines can be created with a backslash and n.

#Fix the code below 👇
# print(Day 1 - String Manipulation")
# print("String Concatenation is done with the "+" sign.")
#   print('e.g. print("Hello " + "world")')
# print(("New lines can be created with a backslash and n.")

print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")


# Input:
# =======

# input() - It creates a prompt for the user. The input function waits for the user to add the input before proceeding:
# eg:
input("what is your name? ")
    # --> phyllis

# example use case:
print("Hello " + input("what is your name? ") + "!")
    # --> what is your name? phyllis
    # --> Hello phyllis!


#len():
# ======

# the length function prints the length of the characters in the string

# Instructions:
# Write a program that prints the number of characters in a user's name. You might need to Google for a function that calculates the length of a string.
# e.g.
# https://www.google.com/search?q=how+to+get+the+length+of+a+string+in+python+stack+overflow
# Warning. Your program should work for different inputs. e.g. any name that you input.
        # Example Input
        # Angela
        # Example Output
        # 6

#Write your code below this line 👇
print(len(input("what is your name? ")))
    # --> what is your name? phyllis
    # --> 7


# variables():
# ============
# ref: https://www.w3schools.com/python/python_variables.asp

# Variables are containers for storing data values.
# Python has no command for declaring a variable.
# A variable is created the moment you first assign a value to it.
# Variables do not need to be declared with any particular type, and can even change type after they have been set.
    # eg.
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

# Casting:
# If you want to specify the data type of a variable, this can be done with casting.

# Example:
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

# You can get the data type of a variable with the type() function.
x = 5
y = "John"
print(type(x))
print(type(y))

# String variables can be declared either by using single or double quotes:
x = "John"
# is the same as
x = 'John'

# Variable names are case-sensitive.
# Example
# This will create two variables:

a = 4
A = "Sally"
    # A will not overwrite a

# Variable Rules:
# 1. A variable name must start with a letter or the underscore character. variables have to be one word and in python you can use an underscore, eg. user_name, or _user_name.
# 2. You can use a digit but it cannot be the at the beginning of the variable. you can have "length1" but not "1length"
# 3. A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# 4. Variable names are case-sensitive (age, Age and AGE are three different variables)
# 5. You should use the special words like "print" or "input" as a variables as these are functions
# 6. Any mistype/variation from the original variable will cause python not to pick up the variable later in the code, 
    # eg. "name" needs to remain as exactly that for the rest of the code. 
    # Any errors like "name" or "nime"... will result in an error of "variable not previously defined."

# Example:
# Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Example:
# Illegal variable names:
    # 2myvar = "John"
    # my-var = "John"
    # my var = "John"

# Making variable names more readable:
# =====================================
# Variable names with more than one word can be difficult to read.
# There are several techniques you can use to make them more readable:

# 1. Camel Case:
# Each word, except the first, starts with a capital letter:
myVariableName = "John"

# 2. Pascal Case:
# Each word starts with a capital letter:
MyVariableName = "John"

# 3. Snake Case:
# Each word is separated by an underscore character:
my_variable_name = "John"

# Many Values to Multiple Variables:
# Python allows you to assign values to multiple variables in one line:
# Example:
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
    # Orange
    # Banana
    # Cherry
# Note: Make sure the number of variables matches the number of values, or else you will get an error.

# One Value to Multiple Variables:
# And you can assign the same value to multiple variables in one line:
# Example
x = y = z = "Orange"
print(x)
print(y)
print(z)
    # Orange
    # Orange
    # Orange

# Use case:
name = input("what is your name? ")
length= len(name)
print(length)
    # --> what is your name? phyllis
    # --> 7

# Instructions:
#Write a program that switches the values stored in the variables a and b.
# Example Input
    # a: 3
    # b: 5
# Example Output
    # a: 5
    # b: 3

####Hint:####
# You should not have to type any numbers in your code.
# You might need to make some more variables.

# Your program should work for different inputs. e.g. any value of a and b.
# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
# solution: Think about it like switching liquids in two cups, you get a third cup to make this possible
c = a
a = b
b = c
# Write your code above this line 👆
# 🚨 Don't change the code below 👇
#test:
print("a: " + a)
print("b: " + b)
    # a: 6
    # b: 8
    # a: 8
    # b: 6
# 🚨 Don't change the code above 👆


#================================
# Project - Band Name Generator:
# ===============================

#1. Create a greeting for your program.
#2. Ask the user for the city that they grew up in.
#3. Ask the user for the name of a pet.
#4. Combine the name of their city and pet and show them their band name.
#5. Make sure the input cursor shows on a new line

print("Hello! Welcome to the band name generator.")
city = input("What is the name of the city you grew up in?\n")
pet = input("What is the name of your first pet?\n")
print("The name of your band could be: " + city + " " + pet )
    # Hello! Welcome to the band name generator.
    # What is the name of the city you grew up in?
    # Nairobi
    # What is the name of your first pet?
    # Chips
    # The name of your band could be: Nairobi Chips