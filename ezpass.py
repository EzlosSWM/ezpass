#!/usr/bin/env python3

#Script to generate a random password
"""
It takes arguments:
length as a must have argument
-u (--username) to input username
-t (--title) to input the website name 
-s (--secret) does not give an output on screen but saves to a json file
-o (--output) outputs the results on screen and saves to a json file
"""

import random
import string
import argparse
import json


# Defines the variables for the randomize password
letters = string.ascii_letters
digits = string.digits
punctuation = string.punctuation

# Generates the in line arguments using argparse
parser = argparse.ArgumentParser(description="Simple script to generate passwords")
parser.add_argument('length', type=int, help="length of password")
parser.add_argument('-u', "--username", nargs='*', default=1, help="username attached to password")
parser.add_argument('-t', "--title", nargs='*', default=1, help="title of website")
parser.add_argument('-s', "--silent", help="does not provide an in-line output, but still saves in output file", action="store_true")
parser.add_argument('-o', '--output', help='viewable output and saves in output folder', action="store_true")
args = parser.parse_args()

usr = args.username
pwLength = args.length
title = args.title
show = args.output

# Generates the randomize password
random_user_pw = ''.join([random.choice(letters + digits + punctuation) for n in range(pwLength)])

# Data to be written
listings = {
    "Title" : title,
    "Username" : usr,
    "Password" : random_user_pw
}

json_object = json.dumps(listings, indent = 4)

# Saves the results of the generated file 
def saveFile():
    with open("/home/ezlos/.scripts/output/listings.json", "a") as outfile:
        #outfile.write("\n")
        #outfile.write("\t")
        json.dump(listings, outfile, indent = 4, separators=(',',': '))
        outfile.write("\n")
        
        

saveFile()

# Tests to see if --ouput or --silent was used.
if show:
    print("The generated password for {} is {}.".format(title, random_user_pw))
else: 
    print("You password was generated, it was saved to your output folder.")
