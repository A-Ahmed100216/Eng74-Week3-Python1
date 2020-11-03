# Dictionaries
# Known as arrays in other languages
# Another way of managing date but more dynamically
# Consist of key value pairs used to stora and manage data.
#  Syntax: We use {} brackets to store dictionaries
#  Dict{"key":"value"}
#  Any type of data can be stored in a dictionary i.e string, integers, lists, tuples etc.
# Dictionaries are ordered by keys
# Let's create a dictionary
devops_students={
    "key":"value",
    "name":"Aminah",
    "stream":"tech",
    "lessons_completed":4,
    "completed_lesson_name": ["Variables","Data Types", "Operators"]
}
print(type(devops_students))
# we can use the key as an index to access values.
print(devops_students['name']) #returns the value of name i.e Aminah
print(devops_students["lessons_completed"])
print(devops_students.keys()) # only returns the keys
print(devops_students.values()) # Only returns the values
#  the variable completed lesson name is a list. Returning this gives the entire list.
print(devops_students["completed_lesson_name"])
# What is we want an item from the list? We can use indexes
print(devops_students["completed_lesson_name"][1])