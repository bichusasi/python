Author: Bichu Sasi
description:A program that accepts the lengths of three sides of a triangle as inputs. The program should output whether or not the triangle is a right triangle (Recall from the Pythagorean Theorem that in a right triangle, the square of one side equals the sum of the squares of the other two sides). Implement using functions.



def sides (first,second,third):
    list = [first,second,third]
    list.sort()
    if list[2]**2 == list[0]**2 + list[1]**2:
        print("This is a right triangle.")
    else:
        print("this is not a right angle")
a=int(input("enter the first:"))
b=int(input("enter the second:"))
c=int(input("enter the third:"))
sides(a,b,c)
