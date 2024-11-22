row = int(input("enter range:"))
print("increasing triangle")
for i in range (1,row+1):
    for j in range(i):
        print("*",end="\t")
    print()

row = int(input("enter range:"))
print("Decreasing triangle")
for i in range(row,0,-1):
    for j in range(i):
        print("*", end="\t")
    print()

row = int(input("enter range:"))
print("Hill pattern")
for i in range (1,row+1):
    for j in range(row-i):
        print(" ",end="\t")
    for k in range(2*i-1):
        print("*",end="\t")
    print()

row = int(input("enter range:"))
print("reverse pattern")
for i in range(row,0,-1):
    for j in range(row - i):
        print(" ", end="\t")
    for k in range(2 * i - 1):
        print("*", end="\t")
    print()
