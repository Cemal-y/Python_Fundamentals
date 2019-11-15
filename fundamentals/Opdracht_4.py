# Op: 4a
group_of_people = ["Alex", "Eliot", "Veronica", "Lucy", "Wouter", "Bart"]

first_chars = [letter[0] for letter in group_of_people]

numbers = list(range(100))

sum = 0

[sum := sum + number for number in numbers]

print(first_chars)
print(sum)

# Op: 4b
# List comprehensions are used to create new lists from other iterables.
# They are useful, because we they reduce the amount of the code comparing to using a normal for loop.

# The code below calculates the squares of each number in the list and returns a new list with those values.
list_of_numbers = [1, 2, 3, 4, 5]
list_of_squares1 = [number**2 for number in list_of_numbers]
print(list_of_squares1)

# In order to do the same we need to do more with a for loop
list_of_squares2 = []
for element in list_of_numbers:
    square = element*element
    list_of_squares2.append(square)
print(list_of_squares2)


# Op: 4c
number_list = range(10)
number_matrix = [[j for j in number_list] for i in number_list]
print(number_matrix)
