# printing, commenting, debugging, string manipulation and variables

# print() echoes back the string or characters in between the ""
print("something")
    #--> something


#Concatenate: join
print("Hello" + "Phyllis")
    # --> HelloPhyllis

#Line Break:
print("Hello Phyllis\nHello phyllis\nhello phyllis")
    #  Hello Phyllis
    #  Hello phyllis
    #  hello phyllis 

#concatenate with space in between- Options: space after Hello, space before phyllis and an empty " " between the two words:
print("hello " + "phyllis")
    # --> hello phyllis
print("hello" + " phyllis")
    #--> hello phyllis
print("hello" + " " + "phyllis")
    # --> hello phyllis


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
name = input("what is your name? ")
length= len(name)
print(length)
    # --> what is your name? phyllis
    # --> 7

# write a program that will reverse the inputs "a" and "b"
a = input("a: ")
b = input("b: ")
c=a
a=b
b=c
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