list_1 = [34,12,25,2,56,7,6]
list_2 = [98,76,45,34,12]
list_3 = list_1 + list_2
even_list = []
odd_list = []
for i in list_3:
    if i % 2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)
print("evenm list:",even_list)
print("odd list",odd_list)
print(even_list + odd_list)
