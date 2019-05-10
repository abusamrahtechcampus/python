


try:
	number = int(input("Enter Number: "))
	res = number  /2
	print(res)

	fo_opject = open("t.txt","r")
	data = fo_opject.read()
	print(data)
	fo_opject.close()

except TypeError:
	print("Enter Numbers Only")
except FileNotFoundError:
	print("File Not Found")


except Exception as e:
	print(e)
else:
     print(10*10)	