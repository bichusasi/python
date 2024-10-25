'''
Author:Bichu Sasi
Date:25/10/2024
Description:Write a Python program to convert temperature values back and forth between Celsius and Fahrenheit. The user should be able to input a temperature in Celsius or Fahrenheit, and the program should convert it to the other unit using the formula:
'''

temp=int(input("Enter the tempreture:"))
unit=input("Is this in (C)elsius or (F)ahrenheit?:")
if unit=='C':
    f = ((9 / 5) * temp) + 32
    print(temp, " celsius is ",f,"Fahrenhiet")
else:
    c = 5 / 9 * (temp - 32)
    print(temp, " fahrenhiet is ",c,"Celsius")