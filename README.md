# Introduction to Python
Python was developed by Guido Van Rossum
in 1991. It is one of the most used and 
fastest growing programming languages. 

## Why Python?
* Supports multiple system and platforms; 
* Object Oriented Programming  driven;
* Helps to improve programmers productivity; 
* Allows you to scale even the most complex applications with ease;
* Extensive support libraries;
* Predominantly used in Machine Learning and Data Analysis.

## Pseudocoding
A translation of your code. 
Makes it easier for you and others to read the code. In particular, non-technical people may need comments to understand what the code does.
## Python Variables
### What is a Variable
A placeholder to store data.

### Types of Variables in Python
Data types are forms which data can take
1. Strings - Characters encased in " " or ' '. Consistency is key, pick one type of quote and stick to this.   
```name="Aminah"```
2. Integer - A whole number   
```age = 23```
3. Float - A number with a decimal   
```travel_allowance = 2.4```
4. Boolean - A True or False variable   
```1 = True```

### How can we take user data?
We can use a method called input() to get data from user:
```
username = input('Please enter your name: ') # Getting user data using the input method. This value is then assigned as a variable called name.
print(username)
```
### How can we find out the type of variable?
We can use the type() method which gives us the data type.
```
print(type(name)) ## This should output string
print(type(age)) ## This should ouput integer
print(type(travel_allowance)) ## This should output float
```

### Overwriting variables
If we use the same variable name, it will be rewritten to
reflect the most recent variable name. For example:
```
colour = "Blue"
colour = "Green"
print(colour) # The output will be Green as this was the most recent assignment
```


# Booleans
Booleans are a type of variable which return a True or False. 
```
a = True
b = False
print(a==b) # Returns False, True is not equal to False.
print(a!=b) # Returns True as True is not equal to False.
print(a<b) # In boolean, True = 1, False =0, 1>0
```

## Boolean methods
The following methods are examples of Boolean Methods:
```
greetings = 'Hello World!'

print(greetings.islower())  # checks if all the values in the greeting variable are in lower case.
print(greetings.isalpha())  # Checks if all values in the greeting variable are alphabetical i.e not numbers.
print((greetings.startswith("H")))  # Checks if greeting variable starts with specified character(s), in this case "H"
print(greetings.endswith("d"))   # Checks if variable ends with specified character(s), in this case "d"
```


# What is concatenation?
Combining strings together to make the output more readable.
Typically we would print each variable separately as shown below:
```python
first_name = 'James'
middle_name= 'Bond'
last_name =int('007')
age = 35

print(first_name) 
print(middle_name)
print(last_name)
```
This method is not very user friendly so we can use concatenation. 
This can be achieved using the  plus sign:
 

## This method is not very user friendly so we can use concatenation...
## We can use the plus operator
print(first_name+middle_name+str(last_name))
# But this is missing spaces which makes it difficult to read so...
print(first_name + " " + middle_name + " " + str(last_name) + " " + str(age))
# Alternatively, using commas, we automatically get spaces
print(first_name,middle_name,last_name)





 