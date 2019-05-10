a = [2, 4, 7, 2, 1, 9, 33, 105, 2, 3, 7, 300, 4, 9]
maxa = a[0]
for i in a:
    for j in a:
        if i > j and i > maxa:
            maxa = i

print("greatest number is", maxa)