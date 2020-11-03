# Collections in python - Practice
# Lists
shopping_list = ["apple", "milk", "bread"]
print(shopping_list)  # We can print the list
print(type(shopping_list))   # How can we be sure this is a list? Use type()

# Indexing in lists
print(shopping_list[1])  # This returns milk
print(shopping_list[2])  # This returns bread
print(shopping_list[-1])  # this returns bread
print(shopping_list[1:])  # We can use : to go from a specified index to the end. This also works in reverse:
print(shopping_list[:1])  # This prints apple


# Task:Create a mixed data type list of 7 items
# Display type of data
# Add, delete, replace, pop
# Use indexing to print list in reverse order

mix_list=[1,3.14,"raspberry","pi",True,42,False]
print(mix_list)
print(type(mix_list))
print(type(mix_list[0]),type(mix_list[1]),type(mix_list[2]), type(mix_list[3]), type(mix_list[4]), type(mix_list[5]), type(mix_list[6]))

# Add an item
mix_list.append("pie")
print(mix_list)
# Remove an item
mix_list.remove(False)
print(mix_list)
# Replace an item
mix_list[5]=72
print(mix_list)
# Use pop to remove the last item
mix_list.pop()
print(mix_list)
# Print in reverse
print(mix_list[-1], mix_list[-2], mix_list[-3], mix_list[-4], mix_list[-5], mix_list[-6])
print(mix_list[::-1])

# Tuples
short_list=("paracetemol", "eggs", "milk","supermalt")
print(type(short_list)) # Returns tuple
short_list[1]="fruits" # This will give us a type error as it is not possible to change tuples.
print(short_list[1]) # Returns eggs


