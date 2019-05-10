dollar_list =[]
ryal_list = []

for item in range(1,11):
	dollar_list.append(item)

converted_rate = float(input("Enter The converted rate: "))
# x= True
#while == True:
if converted_rate>0 and converted_rate <10:
   for item in dollar_list:
       ryal_value = item *converted_rate
       ryal_list.append(ryal_value)
print("The ryal list is \n","\n",ryal_list,"Ryals")
      
        #x = False   


