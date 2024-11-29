def number(num1,num2):
    if num2 == 1:
        return num1
    else:
        return num1 + number(num1,num2-1)
num1=int(input("enter number:"))
num2=int(input("enter number:"))
result=(number(num1,num2))
print("The product of two number:",result)