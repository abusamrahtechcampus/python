amount = float(input("Please Enter The Amount: "))

discount = 0
final_amount = 0 

if amount >0:
     if amount <1000 :
     	discount = amount  *(5/100)
     	final_amount = amount - discount
     elif  amount >= 1000  and amount <= 5000:
     	 discount = amount * (10/100)
     	 final_amount = amount - discount
     
     elif amount> 5000:
     	discount = amount * (15/100)
     	final_amount = amount - discount
     else :
     	print("Please Enter Correct number")
else :
     	print("Please Enter Correct number")

print("the discount amount " , discount)
print("The final amount ", final_amount)