"""1.Write a Python program to multiples all the items in a list."""


list_item = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Initialize an empty list to store the doubled items
doubled_list = []

# Iterate through each item in the list and double it
for item in list_item:
    doubled_item = item * 2
    doubled_list.append(doubled_item)

# Print the result as a list
print(doubled_list)
