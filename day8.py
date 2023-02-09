# Functions with Inputs
# Functions are a handy way of taking a complex set of instructions and packaging them together inside a block of code. 
        # def my_function():
            # Do this
            # then do this
            # finally do this
# and then later all you have to do is call the function by calling the name of the function and then a set of parentheses.
        # my_function()

def greet():
    print("Hallo!")
    print("Bonjour!")
    print("Habari Yako?")

greet()
        # Output:
        # Hallo!
        # Bonjour!
        # Habari Yako?
# Functions with Inputs
            # def my_function(something): 
                # Do this
                # then do this
                # finally do this
# To add the functionality of the input, we can add the name of a variable within the parentheses 
# and this can then be used inside this block of code.
# In order to actually pass this value when we call the function, we have to add the data inside the parentheses.
#  for example:
        # my_function(123)
# When this line of code gets triggered, the computer is going to search for where this function is declared, 
# and then it is going to pass the data (123),to the variable called something.
#  So now effectively, inside this function called my_function, we now have a variable called something that is equal to 123
# this is then passed on to the block of code to do something with that piece of data:
            # def my_function(something):
                # Do this with 123

#  In addition to a simple function we can also create:
# Function that allows for input
# 
def greet_with_name(name):
    print(f"Hallo {name}!")
    print(f"Bonjour {name}!")
    print(f"Habari Yako {name}?")

greet_with_name("Phyllis")
        # Hallo Phyllis!
        # Bonjour Phyllis!
        # Habari Yako Phyllis?

# You can also modify this by changing the value of the input. eg.
greet_with_name("Angel")
        # Hallo Angel!
        # Bonjour Angel!
        # Habari Yako Angel?
# Essentially we are creating a variable and its value
something = 123
# In programming, "something" is referred to as the Parameter is the name of the data that is being passed in, 
# and it is used inside the function to refer to it and do things
# while "123" is referred to as the Argument is the actual calue of the data, which is passed off to the function when it is called.

# Position Vs. Keyword Arguments
# Functions with more than 1 inmput
def greet_with(name, location): # this is going to have two parameters, name and location.
    print(f"Hello {name}!")
    print(f"What is it like in {location}?")

greet_with("Phyllis", "Kenya")
        # Hello Phyllis!
        # What is it like in Kenya?

greet_with("Kenya", "Jack Bauer")
        # Hello Kenya!
        # What is it like in Jack Bauer?

# Positional Arguments
        # def my_function(a, b, c):
            # Do this with a
            # then do this with b
            # finally do this with C
        # my_function(1, 2, 3)
# the vars created will be:
a = 1
b = 2
c = 3
# When you switch around the order of the arguments in the function call, eg.my_function(3,1,2), then the parameters will now have different values.
a = 3
b = 1
c = 2
# Positional arguments are simply an ordered list of inputs in a Python function call 
# that correspond to the order of the parameters defined in the function header.
        # >>> def func(num1, num2):
        # ...     print(f"Num 1: {num1}, Num 2: {num2}")
# 
        # >>> func(1, 2)
        # Num 1: 1, Num 2: 2
# 
        # >>> func(2, 1)
        # Num 1: 2, Num 2: 1
# In this example, we have defined a the function func with parameters num1, and num2. When calling the function, the argument order matters. 
# Python uses the position of the arguments to determine the parameter to map each input value to.

# Keyword Arguments
# A keyword argument is supplied with both a parameter name AND its corresponding value.
        # my_function(a=1, b=2, c=3)
#  so now when positions of the arguments are changed around, the parameters and argument will always be the same corresponding values
def greet_with(name, location): # this is going to have two parameters, name and location.
    print(f"Hello {name}!")
    print(f"What is it like in {location}?")

greet_with(name="Phyllis", location="Kenya")
        # Hello Phyllis!
        # What is it like in Kenya?

greet_with(location="Kenya", name="Phyllis")
        # Hello Phyllis!
        # What is it like in Kenya?

# Challenge: Paint Area Calculator
# Instructions
# You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. 
# Given a random height and width of wall, calculate how many cans of paint you'll need to buy.
# number of cans = (wall height x wall width) ÷ coverage per can.
# e.g. Height = 2, Width = 4, Coverage = 5
# number of cans = (2 * 4) / 5
# = 1.6
# But because you can't buy 0.6 of a can of paint, the result should be rounded up to 2 cans.
# IMPORTANT: Notice the name of the function and parameters must match those on line 13 for the code to work.
# Example Input
        # test_h = 3
        # test_w = 9
# Example Output
        # You'll need 6 cans of paint.

# Hint
# 1. To round up a number:
# https://stackoverflow.com/questions/2356501/how-do-you-round-up-a-number-in-python
# 2. Make sure you name your function/parameters the same as when it's called on the last line of code.

#Write your code below this line 👇
def paint_calc(height, width, cover):
    number_of_cans = round(int(height * width) / cover)
    print(f"You'll need {number_of_cans} cans of paint.") # This will be off since it does not take into account the extra can of pain needed 
                                                            # if the remainder is less that 0.5. Hence, need to do the ceiling instead of a simple round off.
            # Height of wall: 3
            # Width of wall: 9
            # You'll need 5 cans of paint.                
#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5

paint_calc(height=test_h, width=test_w, cover=coverage)

#  Alternate Solution:
import math
def paint_calc(height, width, cover):
    area = height * width
    num_of_cans = math.ceil(area / cover)
    print(f"You'll need {num_of_cans} cans of paint.")
# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5

paint_calc(height=test_h, width=test_w, cover=coverage)

        # Height of wall: 3
        # Width of wall: 9
        # You'll need 6 cans of paint.

# Challenge: Prime_number_checker
# Instructions
# Prime numbers are numbers that can only be cleanly divided by themselves and 1.
# https://en.wikipedia.org/wiki/Prime_number
# You need to write a function that checks whether if the number passed into it is a prime number or not.
# e.g. 2 is a prime number because it's only divisible by 1 and 2.
# But 4 is not a prime number because you can divide it by 1, 2 or 4.
# Example Input 1
        # 73
# Example Output 1
        # It's a prime number.
# Example Input 2
        # 75
# Example Output 2
        # It's not a prime number.

# Hint
# Remember the modulus:
# https://stackoverflow.com/questions/4432208/what-is-the-result-of-in-python
# Make sure you name your function/parameters the same as when it's called on the last line of code.
# Use the same wording as the Example Outputs to make sure the tests pass.
# Test Your Code
# Check your code is doing what it is supposed to. When you're happy with your code, click submit to check your solution.

#Write your code below this line 👇
def prime_checker(number):
    is_prime = True
    for r in range(2, number):
        if number % r == 0:
            is_prime = False
    if is_prime:
        print("It is a prime number.")
    else:
        print("It's not a prime number.")
#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
        # Check this number: 1019
        # It is a prime number.

# Caesar Cipher- Encryption
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount 
    # and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 