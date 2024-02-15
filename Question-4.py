"""4.Write a Python program to print the numbers of a specified list after removing even numbers from it
	list = [24,34,53,65,78,93,23,42]
"""

list_items = [24, 34, 53, 65, 78, 93, 23, 42]

# Create an empty list to store the result
filtered_list = []

# Iterate through the original list and add odd numbers to the filtered list
for x in list_items:
    if x % 2 != 0:
        filtered_list.append(x)

print("List after removing even numbers:", filtered_list)
