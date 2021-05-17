#!/bin/python3

#run the command bello on cli
# $gedit script.py&
	
#variables and Methods

quote = "All is fair in  love and war."
print (quote)

#run the command bello on cli
# $python3 script.py

#methods
print(quote.upper()) #uppercase
print(quote.lower()) #lowercase
print(quote.title()) #title case

#Length of the string
print(len(quote))

#variables and math
name = "Heath" #string
age = 30 #int int(30) means only integer
gpa = 3.7 #float float(3.7)

print(int(age))
print(int(30.1))
print(int(30.9))

print ("My name is " + name + " and I am " + age + "years old.") #this will out put error

#Converting int to string
print ("My name is " + name + " and I am " + str(age) + "years old.")

#to increment out age
age += 1
print(age)

age -= 1
print(age)

birthday=1
age += birthday
print(age)


#Functions 

print('\n')
#functions
print("Here is an emaple function:")

#defining a funtion
def who_am_i():
	name = "Heath"
	age = 30
	print ("My name is " + name + " and I am " + str(age) + "years old.")

#to call a function
who_am_i()

#adding paramenters
def add_one_hundred(num):
	print(num + 100)

#to call the function
add_one_hundred(100)

#Multiple parameters
def add(x,y):
	print(x+y)

add(7,7)

def multiply(x,y):
	return x * y

multiply (7,7) #this will not print it will just return and it can be called leter
print(multiply(7,7)) #this will print 

def squre_root(x):
	print(x ** .5)

def new_line():
	print('\n')

def nl(): #this is still same as above just short
	print('\n')

nl()
#Boolean experessions (True or False)
print ("Boolean expressions:")

bool1 = True
bool2 = 3*3 == 9
bool3 = False
bool4 = 3*3 != 9

print (bool1, bool2, bool3, bool4)
print(type(bool1))

nl()
#Relational and Boolean operators

greater_than = 7 > 5
less_than = 5 < 7
greater_than_equal_to = 7 >= 7
less_than_equal_to = 7 <= 7

test_and = (7 > 5) and (5 < 7) #True
test_and2 = (7 > 5) and (5 > 7) #False
test_or = (7 > 5) or (5 < 7) #True
test_or2 = (7 > 5) or (5 > 7) #True

test_not = not True #False

	#and both or all has to be true to = true
	#or at lest one has to be true to = true

nl()
#Conditional Statements
def drink(money):
	if money >= 2:
		return " You've got yourself a drink!"
	else:
		return "NO drink for you!"

	print(drink(3))
	print(drink(1))

def alcohol(age,money):
	if (age >= 21) and (money >=5):
		return "We're geting a drink!"
	elif (age >= 21) and (money < 5):
		return "Come back with more money."
	elif (age < 21) and (money >= 5):
		return"Nice try, kid!"
	else:
		return "you're too poor and too young"

print(alcohol(21,5))
print(alcohol(21,4))
print(alcohol(20,4))

nl()
#list
#List are data structure and they are changable we can re-order then
#everything inside a list is an item
#list have brackets [] around them
#list items starts with zero
#list are mutable

movies = ["When Harry met Sally", "The Hangover", "The Perks of Being a Wallflower", "The Exorcist"]

print(movies[1]) #this will returnt the second item
print(movies[0]) #returns the first items in the list
print(movies[1:3]) #first number starts and the second number is the stop
print(movies[1:]) #returns the second item till the last
print(movies[:1]) #return everything before the first item
print(movies[:2])
print(movies[-1]) #returns the last item on the list

print(len(movies))
movies.append("Jaws") #when we append we append to the end of the list
print(movies)

movies.pop() #when we pop we pop from the end of the list
print(movies)

movies.pop(0)
print(movies)

nl()
#Tuples
#tuples are in-mutable they do not change
#tuples use perenthesis ()

grades = ("a", "b", "c", "f")
print (grades[1])

nl()
#looping

#For loops -start to finish of an iterate
vegetables = ["cucumber", "spinach", "cabbage"]
for x in vegetables:
	print (x)

#While loops - Execute as long as it's true

i = 1

while i < 10:
	print(i)
	i += 1

