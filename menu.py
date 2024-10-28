'''
Author:Bichu Sasi
Date:28/10/2024
Description:Write a menu-driven Python program that allows users to convert temperatures between Celsius and Fahrenheit. The program should repeatedly display a menu with three options:
'''

while True:
    print("1./tConvert Celsius to Fahrenheit")
    print("2./tConvert Fahrenheit to Celsius")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        cel = int(input("Enter tempreture:"))
        fah =  (cel * 9/5) + 32
        print(f"{cel} celsius in {fah} fahrenheit")
    elif choice == 2:
        fah = int(input("Enter tempreture:"))
        cel =  (fah - 32) * 5/9
        print(f"{fah} fahrenheit in {cel} fahrenheit")
    elif choice == 3:
        break
    else:
        print("Invalid choice!")
