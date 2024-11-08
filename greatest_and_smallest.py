'''
limit = int(input("limit:"))
number = int(input("eneter numbers:"))
small = number
big = number
while limit > 1:
    number = int(input("eneter numbers:"))
    if number > big:
        big=number
    elif number < small:
        small=number
    limit -= 1
print(f"big={big}")
print(f"small={small}")'''
