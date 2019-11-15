# first list with different data types
my_data = ["Cemal", 29, 73.5, True]

# second list with even numbers
numbers = list(range(2, 1001, 2))

new_line = "\n"

print(f"{my_data}{new_line}{numbers}")

# Bonus

# Creating Empty List and adding elements with append method
sample_list = []
sample_list.append(1)
sample_list.append(2)
print(sample_list)

# Cloning a list
sample_lis2 = my_data[::]
print(sample_lis2)

# Copying a list
sample_list3 = sample_list.copy()
print(sample_list3)

# Converting a tuple,array, set...
sample_tuple = (1, 2, 3, 4)
sample_list4 = list(sample_tuple)
print(sample_list4)

# Using extend method
sample_list5 = []
sample_list5.extend(my_data)
print(sample_list5)

# Using list comprehension
list_of_numbers = [1, 2, 3, 4, 5]
list_of_squares1 = [number**2 for number in list_of_numbers]
print(list_of_squares1)
