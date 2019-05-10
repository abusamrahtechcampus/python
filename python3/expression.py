import re

pattern = "^[a-zA-Z]*$"

name = input("Enter your Name letters only: ")

if re.match(pattern,name):
	print("text Matched")
else:
	print("text not Matched")


pattern1 = "^[0-9]*$"

name1 = input("Enter your Name numbers only: ")

if re.match(pattern1,name1):
	print("text Matched")
else:
	print("text not Matched")
