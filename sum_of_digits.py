

number=int(input("Enter a number:"))
sum_of_number = 0
while number>0:
    remainder = number%10
    sum_of_number += remainder
    number = number//10
print("Sum of digits of the given number:",sum_of_number)