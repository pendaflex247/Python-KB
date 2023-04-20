#[Exercise Description](read://http_inventwithpython.com/?url=http%3A%2F%2Finventwithpython.com%2Fpythongently%2Fexercise1%2F)

#Write a program that, when run, greets the user by printing “Hello, world!” on the screen. 
#Then it prints a message on the screen asking the user to enter their name. 
#The program greets the user by name by printing the “Hello,” followed by the user’s name.

#Let’s use “Alice” as the example name. Your program’s output should look like this:

#Hello, world!

#What is your name?

#Alice

#Hello, Alice

#Solution Design (SD)

# Define a greeting message
greeting = "Hello, World!\n"

# Print the greeting
print(greeting)

# Prompt the user for their name
username = input ("What is your name?\n") 

# Print a personalized greeting
print ("Hello, " + username + "!")
