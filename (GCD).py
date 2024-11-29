'''Author: Bichu Sasi
Description:Recursive function to find the greatest common divisor of two positive numbers.

Euclidean Algorithm for Greatest Common Divisor (GCD)'''

def GCD(num1,num2):
        if num1 % num2 == 0:
            return num2
        else:
            return GCD(num2,num1%num2)
num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
print("the greatest common divisor of",num1,",",num2,"is",GCD(num1,num2))
