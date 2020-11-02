# What is concatenation?
# Combining strings together

first_name = 'James'
middle_name= 'Bond'
last_name =int('007')
age = 35
print(first_name)
print(middle_name)
print(last_name)
## This method is not very user friendly so we can use concatenation...
## We can use the plus operator
print(first_name+middle_name+str(last_name))
# But this is missing spaces which makes it difficult to read so...
print(first_name + " " + middle_name + " " + str(last_name) + " " + str(age))
# Alternatively, using commas, we automatically get spaces
print(first_name,middle_name,last_name)

# # Casting is used to integer to string or in reverse.
# # We can use str() to convert to string.
# # Likewise, using int() converts to an integer.
# #print(int(last_name))


## Get user data, display message your age is

# name =input("Please enter your name: ")
# DOB = input("Please enter your DOB: ")
# age = input("Please enter your age: ")
# house_number = input("Please enter your house number: ")
# street = input("Please enter your street name: ")
# postcode = input("Please enter your postcode: ")
# address = str(house_number + " " + street + ", " + postcode)
#
#
# print("Hello" +" " + name)
# print("You are " + str(age) +" years old.")
# print("You live at " + address)
# print ("You were born on " + str(DOB))

# ##Decalring strings with quotes
# # we can use \ as an escape character if our string has an apostrophe
# single_quotes = 'single quote\'s'
# double_quotes = "double quote's"
# print(single_quotes)
# print(double_quotes)

# ## String slicing
# # Why ? if we receive user data but only want certain aspects
# # Indexing - accessing a certain charcaters, start at 0
# greet= "Hello World!"
# print(greet[0]) # Prints the charaacer at index 0 i.e H
# print(greet[0:5])# Prints the range of charcaters from index 0 up to but not including index 5.
# print(greet[-1]) # Can also work in reverse to get the last letter
#
# ## len can be used to get the length of a string
# print(len(greet))

#
# white_space =" Lot's of space at the end             "
# print(len(white_space)) ## the spaces will be counted in the length
# print(len(white_space.strip())) ## this method deletes all the spaces at the end of the greet string
# Count method - count() it counts the number of times anyword or character is present in the string.
sample_text ="Lots of text with Some text and more text"
print(sample_text.count("text"))
print(sample_text.replace("text","chocolate")) ## Replaces text with chocolate
print(sample_text.capitalize()) ## Capitalises the sentence.
print(sample_text.upper()) ## makes the entire string upper case
print(sample_text.lower()) ## makes the entire string lower case

