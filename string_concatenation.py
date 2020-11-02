# What is concatenation?
# Combining strings together

# first_name = 'James'
# middle_name= 'Bond'
# last_name =int('007')
# age = 35
# print(first_name)
# print(middle_name)
# print(last_name)
# ## This method is not very user friendly so we can use concatenation
# ## We can use the plus operator
# print(first_name+middle_name+str(last_name))
# # But this is missing spaces which makes it difficult to read so...
# print(first_name + " " + middle_name + " " + str(last_name) + " " + str(age))
# # Alternatively, using commas, we automatically get spaces
# print(first_name,middle_name,last_name)
#
# # Casting is used to integer to string or in reverse.
# # We can use str() to convert to string.
# # Likewise, using int() converts to an integer.
# #print(int(last_name))


## Get user data, display message your age is
name =input("Please enter your name: ")
DOB = input("Please enter your DOB: ")
age = input("Please enter your age: ")
house_number = input("Please enter your house number: ")
street = input("Please enter your street name: ")
postcode = input("Please enter your postcode: ")
address = str(house_number + " " + street + ", " + postcode)


print("Hello" +" " + name)
print("You are " + str(age) +" years old.")
print("You live at " + address)
print ("You were born on " + str(DOB))