'''Auhor : Bichu Sasi
Description : Program to define a module to find Fibonacci Numbers and import the module to another program.'''
def fibonacci (n):
    list = []
    a,b = 0,1
    while a <= n:
        list.append(a)
        a,b=b,a+b
    return list


