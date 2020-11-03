# # Collection in python
# # Lists?
# # A collection of data. In everyday life we commnly wirte shopping lists which contain everything we wish to purchase. In python, a list is simply a collection of data.
# # Python lists are enclosed in square brackets list = ["item1","item2","item3"]
# # Lists are mutable i.e we can add, remove, change an item.
# # Indexing starts with 0 and represents an item in the list
# # Lets create a list
# shopping_list = ["apple", "milk", "bread"]
# # Now we can print the list
# # print(shopping_list)
# # # How can we be sure this is a list? Use type()
# # print(type(shopping_list))
# #
# # # Looking at indexing in lists
# # print(shopping_list[1]) # This returns milk
# # print(shopping_list[2]) # This returns bread
# # print(shopping_list[-1]) # this returns bread
# # print(shopping_list[1:]) # We can use : to go from a specified index to the end. This also works in reverse:
# # print(shopping_list[:1]) # This prints apple
#
#
# ## Managing Lists - Mutablity Features
# # We can add items to the end of the list using append
# shopping_list.append("eggs")
# print(shopping_list)
#
# # We can also remove items using the remove method
# shopping_list.remove("apple")
# print(shopping_list)
#
# # The pop method can be used to remove the last item from the list
# shopping_list.pop()
# print(shopping_list)
#
# # Replacing items in a list - we put the index we wsh to chnage in square brackets and set it to a new value.
# shopping_list[1]="fruits"
# print(shopping_list)

# ## Can we have mixed data types? YES
# mixed_shopping_list=[1, 2, 3, "apple","milk","bread"]
# print(mixed_shopping_list)

#Task: Create a mixed data type list of 7 items
# dispaly type of data
# add, delete, replace, pop
# Use indexing to print list in reverse order

# mix_list=[1,3.14,"raspberry","pi",True,42,False]
# print(mix_list)
# print(type(mix_list))
# print(type(mix_list[0]),type(mix_list[1]),type(mix_list[2]), type(mix_list[3]), type(mix_list[4]), type(mix_list[5]), type(mix_list[6]))
#
# # Add an item
# mix_list.append("pie")
# print(mix_list)
# # Remove an item
# mix_list.remove(False)
# print(mix_list)
# # Replace an item
# mix_list[5]=72
# print(mix_list)
# # Use pop to remove the last item
# mix_list.pop()
# print(mix_list)
#
# # Print in reverse
# print(mix_list[-1], mix_list[-2], mix_list[-3], mix_list[-4], mix_list[-5], mix_list[-6])
# print(mix_list[::-1])


# Tuples
## Tuples are immutable lists - cannot be changed
# Use cases - NI number, DOB, place of birth, ethnicity - these are things we cannot change
# We use ()to declare a tuple
short_list=("paracetemol", "eggs", "milk","supermalt")
#print(type(short_list))
#short_list[1]="fruits" # This will give us a type error as it is not possible to change tuples.
print(short_list[1])


