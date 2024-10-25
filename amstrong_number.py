'''
Author:Bichu Sasi
Date:25/10/2024
Description:python program to find given number is amstrong number non amstrong number.
'''

number=int(input("Enter a number:"))
orginal_number = number
sum=0
while number>0:
    remainder = number%10
    sum += remainder**3
    number = number//10
if sum == orginal_number:
    print("given number is amstrong number")
else:
    print("given number is non amstrong")