a = [2, 4, 7, 2, 1, 9, 33, 105, 2, 3, 7, 300, 4, 9]
while len(a) > 1:
    for j, u in enumerate(a):
        if u < a[-1]:
            # Move this item to the end of the list
            a[j], a[-1] = a[-1], a[j]
        # The last item is the minimum, so we discard it
        del a[-1]

# Only 1 item is left, it must be the maximum of the original list
print("greatest number is", a[0])