'''Author: Bichu Sasi
DescriptionL:Program to check whether the given number is a valid mobile number or not using functions.

Rules:

    1.Every number should contain exactly 10 digits.
    2.The first digit should be 7 or 8 or 9'''


def number(n):
    if len(n) == 10 and n[0] in "789":
        print(f"The mobile number is {n} is valid")
    else:
        print(f"The mobile number is {n} is invalid")
number(input("eneter mobile number:"))