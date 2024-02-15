"""1.Write a Python program to multiples all the items in a list."""


def multiply_list_items(list):
    result = 1
    for item in list:
        result *= item
    return result

my_list = [2, 3, 4, 5]
result = multiply_list_items(my_list)
print(f"The result of multiplying all items in the list is: {result}")
