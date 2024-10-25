'''
Author:BIchu Sasi
Date:25/10/2024
Discription: Write a Python program to find the largest of two numbers. The program should take three numbers as input from the user and determine which one is the largest. Use conditional statements to compare the numbers.
'''

number1=int(input("Enter the first number:"))
number2=int(input("Enter the second number:"))
if (number1>number2):
    print(number1,"is greatrer than",number2)
else:
    print(number2,"is grater than",number1)