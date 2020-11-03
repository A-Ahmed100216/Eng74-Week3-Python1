# Concatenation and Casting - Practice
# Get user data, display message.

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




