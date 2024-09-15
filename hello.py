# Initial string
my_string = "Hello"

# Print the memory address of the initial string
print("Original string:", my_string)
print("Memory address of original string:", id(my_string))

# Modify the string by creating a new one
new_string = 'h' + my_string[1:]

# Print the memory address of the new string
print("New string:", new_string)
print("Memory address of new string:", id(new_string))
