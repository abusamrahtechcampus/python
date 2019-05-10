print("  Admin Sign in ")

name = input("  Enter Your Name: ")

password = int(input("  Enter Your Password: "))

while True:
	if name == "admin" and password == 123:

		print(" Welcom Admin")
		break

	else:
		print("  Name or Password Is Wrong")

	name = input("  Enter Your Name: ")
	password = int(input("  Enter Your Password: "))