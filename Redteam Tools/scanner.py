#!/bin/python3

from os import scandir
import sys
import socket
from datetime import datetime

#Define our target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #Translate hostname to IPv4
else:
    print("invalide amount of arguments.")
    print("syntax; python3 scanner.py <ip>")

#Add a pretty banner (print 50 dashes)
print ("-" * 50)
print("scanning target "+target)
print("Time started: "+str(datetime.now()))
print ("-" * 50)

#Try statement
try:
    #for port in rang(1,65535):
    for port in range(50,85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #AF_INET is our IPv4 address #SOCK_STREAM is our port
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port)) #return an error indicator
        if result == 0:
            print("Port {} is open".format(port))
        s.close()

#to interprute the scan

#ctl + C we want to exit the program
except KeyboardInterrupt: 
    print("\nExiting program.")
    sys.exit()

#exit the progeram if there's no name resolution
except socket.gaierror: 
    print("Hostname could not be resolved.")
    sys.exit()

#if we can't connect to the ip address we want to exit the program
except socket.error:
    print("Couldn't connect to server.")
    sys.exit()

#python3 scanner.py <ip>