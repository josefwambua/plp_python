# Creating an empty list called my_list
my_list = []

# Append 10, 20, 30, 40 elements to the list: 
my_list.extend([10, 20, 30, 40])

# Insert the value 15 at the second position in the list
my_list.insert(1, 15)

# Extend the list with another list: [50, 60, 70]
my_list.extend([50, 60, 70])

# Remove the last element from the list
my_list.pop()

# Sort the list in ascending order
my_list.sort()

# Find and print the index of the value 30 in list
index_30 = my_list.index(30)
print("Index of 30 in my_list:", index_30)
