"""2.Write a Python program to remove duplicates from a list."""


my_list = [1, 2, 3, 1, 2, 3, 5, 4 ,6, 2]
print("Orginal List:", my_list)
temp_list = []  # Create an empty list to store unique elements

for i in my_list:
    # Check if the element is not already in the temporary list
    if i not in temp_list: 
    # If not present, append the element to the temporary list
        temp_list.append(i)

print("List After removing duplicates ", temp_list)