'''Author : Bichu sasi
Description : Write a Python function to check whether a number falls within a given range. '''

def text (num):
    list = []
    for i in range (0,9+1):
        list.append(i)
    if num in list:
        print("Number is present")
    else:
        print("Number is not present")
num = int(input("Enter number : "))
text (num)