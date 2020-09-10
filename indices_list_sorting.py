# Task: Finding all indices of a certain item in a multidimensional list
# Input: list to search, value/item to search for
# Output: list of indices i.e. returning indices of the item found in the list
# Method: Using a function to find the indices

def list_indices_item(my_list, my_item):
    indices_list = list()   # Initializing an empty list to store the indices
    for i in range(len(my_list)):
        if my_list[i] == my_item:  # Checks first, if the list has the item
            indices_list.append([i])    # If yes, then the indices are appended
        elif isinstance(my_list[i], list): # Checking if the next index is a list
            for index in list_indices_item(my_list[i], my_item): # Using Recursion to call the defined function in itself and repeating the procedure Note: the my_list now has changed
                    indices_list.append([i] + index) # Using concatenation to store the indices
    return indices_list


oma_list = [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]
oma_item = 2
x = list_indices_item(oma_list, oma_item)
print(x)

