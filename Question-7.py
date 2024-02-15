"""7. Write a Python program to find the repeated items of a tuple."""


def repeated_items(sample_tuple):
    repeated_set = {item for item in sample_tuple if sample_tuple.count(item) > 1}
    return tuple(repeated_set)


sample_tuple = (1, 2, 4, 1, 2, 4, 5, 6, 2)

# Get the repeated items in the tuple as a tuple
result = repeated_items(sample_tuple)

print("Repeated items:", result)