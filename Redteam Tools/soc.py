#!/bin/python3

#we use socket to connect nodes

from os import putenv
import socket

HOST = '127.0.0.1'
PORT = 7777

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

#on cli type
# $ nc -nvlp 7777 #to establish a listening port and listen on 7777
#then on another cli run # $ python3 soc.py

#output

#On terminal 1
#nc -nvlp 7777

#On terminal 2
# python3 soc.py

#Output on terminal 1 after terminal 2 was ran
#└─$ nc -nvlp 7777
#listening on [any] 7777 ...
#connect to [127.0.0.1] from (UNKNOWN) [127.0.0.1] 34688
# connection terminatered because we didnot tell it to do anything
