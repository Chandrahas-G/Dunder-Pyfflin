# For List
my_list = [1, 3, 2, 1, 2, 3, 2, 3, 4]
new_list = dict.fromkeys(my_list)

print(new_list.keys())                       # printing keys of Dict


# With String
my_list = "chandrahas"
new_list = list(dict.fromkeys(my_list))      # Extracts unique keys into List

print(new_list)
