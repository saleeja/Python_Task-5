"""6.Using list comprehension, construct a list from the squares of each element in the list, if the square is greater than 50.
	lst1=[2, 4, 6, 8, 10, 12, 14]
"""


list_items = [2, 4, 6, 8, 10, 12, 14, 5, 20]
# Using list comprehension to create a new list containing squares greater than 50
squares_greater_than_50 = [x**2 for x in list_items if x**2 > 50]

print("Squares greater than 50:", squares_greater_than_50)
