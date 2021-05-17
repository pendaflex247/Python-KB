#!/bin/python3

#Importing modules

#sys has to do with anything with system and parameters
import sys #sys is a system function and parameters

print(sys.version)

#sys.exit exit python cleanly 

import sys
from datetime import datetime
print (datetime.now())

import sys
from datetime import datetime as dt #import with alias
print (dt.now())

my_name ="Heath"
print(my_name[0])
print(my_name[-1])

sentence = "This is a sentence."
print(sentence[:4])

print(sentence.split())

sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split)
print(sentence_join)

quote = "He said, \"give me all your money\""
print(quote)

too_much_space= "          hello            "
print(too_much_space.strip())

print("a" in "Apple")

#to find the word a in Apple if well don't know what the word is 
letter = "A"
word = "Apple"
print(letter.lower() in word.lower()) #Imporved

movie = "The Hangover"
print("myfavorite movie is {}.".format(movie))

