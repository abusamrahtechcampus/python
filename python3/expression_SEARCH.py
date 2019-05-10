import re

pattern = ["java","python","javascript"]

text = "i love python"
for item in pattern:
	if re.search(item,text):
		print("item found")
	else:
	     print("item not found")	