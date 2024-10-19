'''Author:Bichu Sasi
Date:19-10-2024
Discription:Access and print a sub-string that consists of the last name only. Use string slicing to extract the sub-string.
'''

first_name = input("Enter your first name:")
last_name = input("Enter last name:")
name = first_name+" "+last_name
print(name)
first_name_length = len(first_name)
print(first_name_length)
extract_first_name = name[:first_name_length]
print(extract_first_name)
