"""3.Write a Python program to count the number of strings where the string length is 2 or more.
	Sample List : ['abc', 'xyz', 'aba', '1']
	Expected Result : 3  """


my_list = ['abc', 'xyz', 'aba', '1', 'a', 'bca']
# Initialize a variable to store the count of strings with length 2 or more
result = 0
# Iterate through each string in the list
for i in my_list:
    # Check if the length of the current string is greater than or equal to 2
    if len(i) >= 2:
        result += 1 # If true, increment the result count

print(result)