#For Loops, Ranges and Clode Blocks
# Using the for loop with Python Lists
# for loops and the range() function

# For loop
# for item in list_of_items:
    # do something to each item

fruits = ["Apple", "Pear", "Banana"]
for fruit in fruits:
    print(fruit)
        # Apple
        # Pear
        # Banana

#fruit represents a name for each of the items in the list. Can be any name
# fruits represents the list we need to loops through.

#for loops are not limited to a single statement. They can also be used to print out code blocks within the for loops statement. eg.:
fruits = ["Apple", "Pear", "Banana"]
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")
        # Apple
        # Apple Pie
        # Pear
        # Pear Pie
        # Banana
        # Banana Pie
# the iterations will continue until the loop is done with every single item in the list.
# if the indentations are off, it gives the code a while different meaning:
fruits = ["Apple", "Pear", "Banana"]
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")
    print(fruits)
        # Apple
        # Apple Pie
        # ['Apple', 'Pear', 'Banana']
        # Pear
        # Pear Pie
        # ['Apple', 'Pear', 'Banana']
        # Banana
        # Banana Pie
        # ['Apple', 'Pear', 'Banana']
# vs:
fruits = ["Apple", "Pear", "Banana"]
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")
print(fruits)
        # Apple
        # Apple Pie
        # Pear
        # Pear Pie
        # Banana
        # Banana Pie
        # ['Apple', 'Pear', 'Banana']
#  This will only print the "fruits" once because it is outside of the for loop,
#  so it will only be printed after the for loop has already been run.


#Average Height Exercise
# Instructions
# You are going to write a program that calculates the average student height from a List of heights.
# e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]
# The average height can be calculated by adding all the heights together and dividing by the total number of heights.
# e.g.
# 180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146
# There are a total of 7 heights in student_heights
# 1146 ÷ 7 = 163.71428571428572
# Average height rounded to the nearest whole number = 164
# Important You should not use the sum() or len() functions in your answer. You should try to replicate their functionality using what you have learnt about for loops.

# Example Input
# 156 178 165 171 187
# In this case, student_heights would be a list that looks like: [156, 178, 165, 171, 187]

# Example Output
# 171

# Hint:
# Remember to use the round() function to round the average height before you print 
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
#Write your code below this row 👇
# Solution 1:
# the sum() function will give you the sum of the total number of items in the list:
total_height = sum(student_heights)
total_students = len(student_heights)
average = round(total_height / total_students)
print(average)

# Solution 2:
# replicate the sum function first:
total_height = 0
for height in student_heights:
    total_height += height
print(total_height)
# replicate the len function:
total_students = 0
for student in student_heights:
    total_students += 1
print(total_students)

average = round(total_height / total_students)
print(average)
    # Input a list of student heights 156 178 165 171 187
    # 857
    # 5
    # 171

# Exercise: Highest and lowest score
# Instructions:
# You are going to write a program that calculates the highest score from a List of scores.
# e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
# Important you are not allowed to use the max() or min() functions. The output words must match the example. i.e
# The highest score in the class is: x

# Example Input:
# 78 65 89 86 55 91 64 89
# In this case, student_scores would be a list that looks like: [78, 65, 89, 86, 55, 91, 64, 89]

# Example Output:
# The highest score in the class is: 91

# Hint:
# Think about the logic before writing code. How can you compare numbers against each other to see which one is larger?

# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆
#Write your code below this row 👇

# Solution 1:
# using min() and max() functions:
# min and max functions will loop through the list and print out the least and largest values correspondingly
max_score = max(student_scores)
min_score = min(student_scores)
print(f"The highest score is: {max_score}")
print(f"The lowest score is: {min_score}")
        # Input a list of student scores 23 34 45 56 78 90 100
        # [23, 34, 45, 56, 78, 90, 100]
        # The highest score in the class is: 100
        # The lowest score in the class is: 23

# Solution 2:
# using the for loop() function:
highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"The highest score is: {highest_score}")
        # Input a list of student scores 23 34 45 56 67 78 90 100
        # [23, 34, 45, 56, 67, 78, 90, 100]
        # The highest score is: 100

lowest_score = student_scores[0]
for score in student_scores:
    if score < lowest_score:
        lowest_score = score
print(f"The lowest score is: {lowest_score}")
        # Input a list of student scores 130 34 45 56 78 90 137
        # [130, 34, 45, 56, 78, 90, 137]
        # The lowest score is: 34

# For Loops and the Range() Function:
# for number in range(a, b):
    # print(number)

# The range funcions is useful to generate numbers to loops through a list. 
# The range() function returns a sequence of numbers, starting from 0 by default, 
# and increments by 1 (by default), and stops before a specified number. 

# Syntax:
# range(start, stop, step)

# Parameter Values:
# Parameter	Description
# start	Optional. An integer number specifying at which position to start. Default is 0
# stop	Required. An integer number specifying at which position to stop (not included).
# step	Optional. An integer number specifying the incrementation. Default is 1

# Example
# Create a sequence of numbers from 0 to 5, and print each item in the sequence:
x = range(6)
for n in x:
  print(n)
        # 0
        # 1
        # 2
        # 3
        # 4
        # 5

# Example:
# Create a sequence of numbers from 3 to 5, and print each item in the sequence:
# This does not include the last number in the loop(it will include the first digit which is 3 in this case, but 6 is not included)
x = range(3, 6)
for n in x:
  print(n)
        # 3
        # 4
        # 5

# Example:
for number in range(1, 10):
  print(number)
        # 1
        # 2
        # 3
        # 4
        # 5
        # 6
        # 7
        # 8
        # 9

# Example:
# the step denotes the number the range is going to be increased by if not the default of 1.
# Create a sequence of numbers from 3 to 19, but increment by 2 instead of 1:
x = range(3, 20, 2)
for n in x:
  print(n)
        # 3
        # 5
        # 7
        # 9
        # 11
        # 13
        # 15
        # 17
        # 19

# Find the sum of all numbers from 1 to 100:
total = 0
for number in range(1,101):
    total += number
print(total)
        # 5050

# Exercise: Adding Even Numbers
# Instructions
# You are going to write a program that calculates the sum of all the even numbers from 1 to 100. Thus, the first even number would be 2 and the last one is 100:
# i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100
# Important, there should only be 1 print statement in your console output. It should just print the final total and not every step of the calculation.

# Hint
# There are quite a few ways of solving this problem, but you will need to use the range() function in any of the solutions.
#Write your code below this row 👇
sum = 0
for number in range(2, 101, 2):
    sum += number
print(sum)
        # 2550

#Solution 2:
sum = 0
for number in range(1, 101):
    if number % 2 == 0:
        sum += number
print(sum)
        # 2550


#  Exercise: FizzBuzz 
# Instructions
# You are going to write a program that automatically prints the solution to the FizzBuzz game.
# Your program should print each number from 1 to 100 in turn.
# When the number is divisible by 3 then instead of printing the number it should print "Fizz".
# When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"
# e.g. it might start off like this:
        # 1
        # 2
        # Fizz
        # 4
        # Buzz
        # Fizz
        # 7
        # 8
        # Fizz
        # Buzz
        # 11
        # Fizz
        # 13
        # 14
        # FizzBuzz
# .... etc.
# Hint
# 1. Remember your answer should start from 1 and go up to and including 100.
# 2. Each number/text should be printed on a separate line.
# Write your code below this row 👇
x = range(1,101)
for number in x: # or for number in range(1,101): <== without adding x =range() as shown here.
    if number % 15 == 0: # using lcm(least common factor) of 3 and 5 with is 15 which can also be written out as:
    # if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else: 
        print(number)
        # 1
        # 2
        # Fizz
        # 4
        # Buzz
        # Fizz
        # 7
        # 8
        # Fizz
        # Buzz
        # 11
        # Fizz
        # 13
        # 14
        # FizzBuzz
        # 16
        # 17
        # Fizz
        # 19
        # Buzz
        # Fizz
        # 22
        # 23
        # Fizz
        # Buzz
        # 26
        # Fizz
        # 28
        # 29
        # FizzBuzz
        # 31
        # 32
        # Fizz
        # 34
        # Buzz
        # Fizz
        # 37
        # 38
        # Fizz
        # Buzz
        # 41
        # Fizz
        # 43
        # 44
        # FizzBuzz
        # 46
        # 47
        # Fizz
        # 49
        # Buzz
        # Fizz
        # 52
        # 53
        # Fizz
        # Buzz
        # 56
        # Fizz
        # 58
        # 59
        # FizzBuzz
        # 61
        # 62
        # Fizz
        # 64
        # Buzz
        # Fizz
        # 67
        # 68
        # Fizz
        # Buzz
        # 71
        # Fizz
        # 73
        # 74
        # FizzBuzz
        # 76
        # 77
        # Fizz
        # 79
        # Buzz
        # Fizz
        # 82
        # 83
        # Fizz
        # Buzz
        # 86
        # Fizz
        # 88
        # 89
        # FizzBuzz
        # 91
        # 92
        # Fizz
        # 94
        # Buzz
        # Fizz
        # 97
        # 98
        # Fizz
        # Buzz

# Project of the Day: Password Generator
# Welcome to the PyPassword generator! 
# How many letters would you like in your password?
# 14
# How many symbols would you like?
# 3
# How many numbers would you like?
# 4
# Here is your password: 4FW*K*x4%Y8VwKFZMxxku(

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 
'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'W', 'Y', 'Z']

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0' ]

symbols = ["!", "@", "#", "$", "%", "&", "*", "+", '(', ')']

print("Welcome to the PyPassword generator!")
nr_letters = int(input("How many letters would you like to use in your password? \n"))
nr_numbers = int(input("How many numbers would you like to use in your password? \n"))
nr_symbols = int(input("How many symbols would you like to use in your password? \n"))

# Solution 1- Easier to guess option:
password = ""
# for char in range(1, nr_letters + 1):
#     random_char = random.choice(letters)
#     password += random_char
        # or:
for char in range(1, nr_letters +1):
    password += random.choice(letters)
for char in range(1, nr_numbers + 1):
    password += random.choice(numbers)
for char in range(1, nr_symbols + 1):
    password += random.choice(symbols)
print(password)
        # Welcome to the PyPassword generator!
        # How many letters would you like to use in your password? 
        # 4
        # How many numbers would you like to use in your password? 
        # 4
        # How many symbols would you like to use in your password? 
        # 4
        # SHGe1269$!&! <== this is easy to guess because the output is not random enough

#solution 2- (harder to guess option):
password_list = []
for char in range(1, nr_letters +1):
    password_list += random.choice(letters) # password_list.append(random.choice(letters))
for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)
for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)
        # print(password_list) <== this will be generated as a list[].
        #to reorder/rearrange the items in a list, you can either use a for loop (tedious because you have to create another list) or use the shuffle() function:
random.shuffle(password_list)
        # print(password_list)
password = ""
for char in password_list:
    password += char
print(f"your password is: {password}") # print(password)

        # Welcome to the PyPassword generator!
        # How many letters would you like to use in your password? 
        # 4
        # How many numbers would you like to use in your password? 
        # 4
        # How many symbols would you like to use in your password? 
        # 4
        # 7%50S@++if2T




















