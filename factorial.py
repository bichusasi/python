def factorial (f):
    if f == 0:
        return 1
    else:
        return f * (factorial (f-1))
n=int(input("enter number:"))
f=factorial(n)
print(f"the factorial of given number {n} is {f}")