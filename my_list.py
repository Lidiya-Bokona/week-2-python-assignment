# Create an empty list
my_list = []

# Add numbers
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Insert 15 in the second position
my_list.insert(1, 15)

# Add more numbers
my_list.extend([50, 60, 70])

# Remove the last number
my_list.pop()

# Sort the numbers
my_list.sort()

# Find and print the position of 30
index_of_30 = my_list.index(30)
print(index_of_30)  # This will show where 30 is in the list
