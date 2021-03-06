# Dictionary - Practice
# Let's create a dictionary
devops_students={
    "key":"value",
    "name":"Mina",
    "stream":"tech",
    "lessons_completed":4,
    "completed_lesson_name": ["Variables","Data Types", "Operators"],
    "hobbies":["hiking","baking","reading"]
}
print(type(devops_students))  # Returns Dictionary

# we can use the key as an index to access values.
print(devops_students['name']) #returns the value of name i.e Mina
print(devops_students["lessons_completed"]) #returns the value of lessons completed i.e 4
print(devops_students.keys()) # only returns the keys
print(devops_students.values()) # Only returns the values
#  the variable completed lesson name is a list. Returning this gives the entire list.
print(devops_students["completed_lesson_name"])
# What is we want an item from the list? We can use indexes
print(devops_students["completed_lesson_name"][1])
# How can we change values
devops_students["lessons_completed"]=3
print(devops_students["lessons_completed"])

# How do we get key value pairs?
print(devops_students.items())
print(type(devops_students.items()))

#Task
# Create a dictionary to store user details
# all the details that you utilise in the last task
# create a list of hobbies of at least 3 items.
# name, dob, address, course, grades,
# explore dictionary methods: remove, add, replace

# Create the dictionary
my_details={
    "Full Name":"Jane Doe",
    "DOB":" 00-00-0000",
    "Address":"100 Generic Lane, NO9 W34",
    "Course":"DevOps",
    "Grades":66,
    "Hobbies":["Hiking","Murder Mystery","Baking"]
}
# Prints out the original list
print(my_details)

# Type of item
print(type(my_details["Grades"]))
print(type(my_details["Hobbies"]))

# Adding an item
my_details["Age"]=100
print(my_details)

#  Removing items
my_details.pop("Age")
print(my_details)

# Replacing items
my_details["Course"]="Technology"
print(my_details["Course"])
my_details["Hobbies"][2]="Biking"
print(my_details["Hobbies"])

# Reversing Hobbies
print(my_details["Hobbies"][::-1])

# Appending lists within a dictionary
devops_students["hobbies"].append("zumba")
print(devops_students)
# Likewise we can remove within a list
devops_students["hobbies"].remove("baking")
print(devops_students)
