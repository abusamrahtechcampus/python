amount = float(input("Please Enter The Amount: "))

discount = 0
final_amount = 0

if amount > 0 and amount < 1000:
    discount = amount * (5 / 100)
    final_amount = amount - discount
    print("\n","Your discountt 5%")
elif amount >= 1000 and amount <= 5000:
    discount = amount * (10 / 100)
    final_amount = amount - discount
    print("\n","Your discount 10%")

elif amount >5000:
    discount = amount * (15 / 100)
    final_amount = amount - discount
    print("\n","Your discountt 15% ")
else:
    print("Please Enter Correct number ")

print("\n","the discount amount ", discount)
print("\n","The final amount ", final_amount)
