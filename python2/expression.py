import re

pattern = "^[a-zA-Z]*$"

name = input("Enter your Name: ")

if re.match(pattern,name):
	print("text Matched")
else:
	print("text not Matched")