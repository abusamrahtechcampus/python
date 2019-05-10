
import datetime

name = input("Please Enter Your Name: ")

input("p any key to continue .......")

year = int(input("Please Enter Your Year: "))

month = int(input("Please Enter Your Month: "))

day = int(input(" Please Enter Your Day: "))


today_date = datetime.datetime.now()


dop = datetime.datetime(year,month,day)

age = today_date - dop
#print(age)

age_1 = age.days / 365

print("Mr:",name," Your Age Is",int(age_1) ,"year")

input("Press Enter To Exit........")
