'''Author : Bichu sasi
Description :  Write a Python function to find the maximum of three numbers.'''

def number(list):
    list.sort()
    print(f"the maximum value is : {list[2]}")
num1 = int(input("enetr first number : "))
num2 = int(input("enetr second number : "))
num3 = int(input("enetr third number : "))
list = [num1,num2,num3]
number(list)