def number(num1,num2):
    if num2 == 0:
        return num1
    else:
        return number(num1+1,num2-1)
num1=int(input("enter number:"))
num2=int(input("enter number:"))
sum=(number(num1,num2))
print("sum:",sum)