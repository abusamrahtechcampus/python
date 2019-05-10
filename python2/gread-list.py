pass_grade = ['A','B','C','D']
failed_grade = 'F'

grade = input("Please Enter Your Grade: ")

if grade.upper() in pass_grade or grade.lower() in pass_grade:
	print("Congratultion You Pass")
elif grade.upper() == failed_grade or grade.lower() == failed_grade:
	print("good Luck Next Year")

else:
	print("Please Enter Correct your Grade")
