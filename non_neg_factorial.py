
'''Author : Bichu sasi
Description :  Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument. '''
def factorial (num):
    fact = 1
    for i in range (1,num+1):
        fact *= i
    print(f"factorial of given number :{fact}")
num = int(input("enter the number : "))
if num > 0:
    factorial (num)
else:
    print("Enter only positive numbers!")


