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

## Pycharm SetUp
### Python 3.7

## Python Variables
### What is a Variable
A placeholder to store data.

### Pseudocoding
A translation of your code. 
Makes it easier for you and others to read the code. In particular, non-technical people may need
 
### Types of Variables in Python
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

### Overwriting variables:
If we use the same variable name, it will be rewritten to
reflect the most recent variable name. For example:
```
colour = "Blue"
colour = "Green"
print(colour) # The output will be Green as this was the most recent assignment
```


 