# printing, commenting, debugging, string manipulation and variables
#DataType: string

# print() echoes back the string or characters in between the ""
print("something")
    #--> something

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
# concatenate with space in between- Options: space after Hello, space before phyllis and an empty " " between the two words:
print("hello " + "phyllis")
    # --> hello phyllis
print("hello" + " phyllis")
    #--> hello phyllis
print("hello" + " " + "phyllis")
    # --> hello phyllis


# Instructions
# When you run your program, it should print the following:

        # Day 1 - String Manipulation
        # String Concatenation is done with the "+" sign.
        # e.g. print("Hello " + "world")
        # New lines can be created with a backslash and n.

print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")


# Input:
# input() will wait for the user to add the input before proceeding:
# eg:
input("what is your name? ")
    # --> phyllis

print("Hello " + input("what is your name? ") + "!")
    # --> what is your name? phyllis
    # --> Hello phyllis!


#len() prints the length of the characters in the string
print(len(input("what is your name? ")))
    # --> what is your name? phyllis
    # --> 7


#variables()
# varibales have to be one word and in python you can use an underscore, eg. user_name, or you can use a digit but it cannot be the at the beginning 
# of the variable. you can have "length1" but not "1length"

# you should use the special words like "print" or "input" as a variables as these are functions

# any mistype/variation from the original variable will cause python not to pick up the variable later in the code, 
# eg. "name" needs to remain as exactly that for the rest of the code. Any errors like "name" or "nime"... will result in an error of "variable not previously defined."

name = input("what is your name? ")
length= len(name)
print(length)
    # --> what is your name? phyllis
    # --> 7

# Instructions
#Write a program that switches the values stored in the variables a and b.
#Your program should work for different inputs. e.g. any value of a and b.
a = input("a: ")
b = input("b: ")
#solution: Think about it like switching liquids in two cups, you get a third cup to make this possible
c=a
a=b
b=c

#test:
print("a: " + a)
print("b: " + b)
    # a: 6
    # b: 8
    # a: 8
    # b: 6


# band name generator:
print("Hello! Welcome to the band generator.")
city = input("what is the name of the city you grew up in?\n ")
pet = input("what is the name of your first pet?\n ")
print("the name of your band could be: " + city + " " + pet )
    # what is the name of the city you grew up in? Nairobi 
    # what is the name of your first pet? Chips
    # the name of your band could be: Nairobi Chips