# Data Types (Booleans) and Operators - Practice
# Booleans give a True or False outcome.
a = True
b = False
print(a==b) # Returns False, True is not equal to False.
print(a!=b) # Returns True as True is not equal to False.
print(a<b) # In boolean, True = 1, False =0, 1>0

# Boolean methods
greetings = 'Hello World!'

print(greetings.islower())  # checks if all the values in the greeting variable are in lower case.
print(greetings.isalpha())  # Checks if all values in the greeting variable are alphabetical i.e not numbers.
print((greetings.startswith("H")))  # Checks if greeting variable starts with specified character(s), in this case "H"
print(greetings.endswith("d"))   # Checks if variable ends with specified character(s), in this case "d"

# None
print(bool(None)) # Returns False as None = False