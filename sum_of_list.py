'''Author : Bichu sasi
Description : Write a Python function to sum all the numbers in a list.
Sample List : (8, 2, 3, 0, 7)
Expected Output : 20 '''

def sum_of_list(list):
    sum = 0
    for i in list:
        sum += i
    print(sum)
list = []
n = int(input("Enter the number of elements : ))
for i in range (n):
    b = int(input("enter the elements : "))
    list.append(b)
sum_of_list(list)