try:
	mfile = open("exa_file.txt","r")
	data = mfile.read()
	print(data)
	mfile.close()
except FileNotFoundError:
	print("Sorry, This File Doesn't Exist")
else:
	print(10*10)
