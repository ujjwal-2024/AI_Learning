# variables 

A variable is a named storage location used to hold a value in a program.

In simple terms: it’s like a container that stores data which can change during program execution.

Python uses variables to store data without needing to declare the type explicitly.

ex:
x=10
print(x)
o/t: 10

# Why variables are important

They help programs:

store data
reuse values
perform calculations
handle user input

# Rules for Naming Variables
To use variables correctly, the following naming rules should be followed:

Names can contain letters, digits and underscores (_).
The first character cannot be a digit.
Names are case-sensitive, so myVar and myvar are treated differently.
Keywords such as if, else and for cannot be used as variable names.

# Below listed variable names are valid:

age = 21
_colour = "lilac"
total_score = 90

# Below listed variables names are invalid:

1name = "Error"  # Starts with a digit
class = 10       # class is a reserved keyword
user-name = "Doe"  # Contains a hyphen

# Assigning Values to Variables

1. Basic Assignment: Variables are assigned values using the = operator.

x = 5
y = 3.14
z = "Hi"

2. Dynamic Typing: Python is dynamically typed, so the same variable can store different data types during execution.

x = 10
x = "Now a string"

3. Assigning Same Value: same value can be assigned to multiple variables in a single line.

a = b = c = 100
print(a, b, c)

Output
100 100 100
4. Assigning Different Values: Multiple variables can also be assigned different values in a single line.

x, y, z = 1, 2.5, "Python"
print(x, y, z)

Output
1 2.5 Python

# Deleting a Variable

del keyword is used to delete a variable from memory. After deletion, the variable can no longer be accessed.

x = 10
del x
print(x) 
Output

ERROR!
Traceback (most recent call last):
  File "<main.py>", line 3, in <module>
NameError: name 'x' is not defined

Explanation: del x deletes the variable x. Accessing x after deletion raises a NameError because the variable no longer exists.

