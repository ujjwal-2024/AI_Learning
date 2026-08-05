# Python — Complete Fundamentals

## 1. What is Python?

**Python** is a high-level, interpreted, general-purpose programming language known for its simple syntax, readability, and large ecosystem of libraries.

Python is widely used in:

* Web development
* Data Science
* Artificial Intelligence
* Machine Learning
* Automation
* Scientific computing
* Backend development
* Scripting
* Data analysis
* Cybersecurity
* DevOps

Python is particularly important in **AI/ML** because of its extensive ecosystem, including:

* NumPy
* Pandas
* Matplotlib
* Seaborn
* Scikit-learn
* PyTorch
* TensorFlow
* Transformers
* FastAPI

---

# 2. Why Python is Popular for AI/ML

Python is widely used in AI because:

### Simple Syntax

Python code is generally shorter and easier to read than many other programming languages.

```python
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number)
```

### Huge Ecosystem

Python has libraries for almost every part of the AI workflow.

```text
Python
   ↓
NumPy
   ↓
Pandas
   ↓
Matplotlib
   ↓
Scikit-learn
   ↓
PyTorch
   ↓
AI / ML Applications
```

### Community

Python has a very large developer and AI community, which means there are many:

* Libraries
* Tutorials
* Documentation
* Open-source projects
* Research implementations
* Developer tools

---

# 3. Python Characteristics

Important characteristics of Python:

* High-level language
* Interpreted
* Dynamically typed
* Object-oriented
* Supports procedural programming
* Supports functional programming
* Cross-platform
* Open source
* Automatic memory management
* Extensive standard library
* Large third-party ecosystem

---

# 4. Installing and Running Python

Check Python version:

```bash
python --version
```

or:

```bash
python -V
```

Run Python interactively:

```bash
python
```

Then:

```python
print("Hello, Python!")
```

Exit:

```python
exit()
```

Run a Python file:

```bash
python main.py
```

---

# 5. Python Syntax

Python uses indentation to define blocks of code.

Example:

```python
age = 20

if age >= 18:
    print("Adult")
```

The indentation is important.

Incorrect:

```python
if age >= 18:
print("Adult")
```

Correct:

```python
if age >= 18:
    print("Adult")
```

Python commonly uses **4 spaces** for indentation.

---

# 6. Comments

Comments are ignored by Python and are used to explain code.

Single-line comment:

```python
# This is a comment
print("Hello")
```

Multiple lines can be represented using multiple `#` comments:

```python
# This program
# calculates the
# average of numbers
```

---

# 7. Variables

A variable is a name that refers to a value.

```python
name = "Ujjwal"
age = 20
height = 165
```

Python does not require you to explicitly declare the variable's type.

```python
x = 10
```

Later:

```python
x = "Hello"
```

This is possible because Python is **dynamically typed**.

---

# 8. Variable Naming Rules

Valid:

```python
age = 20
student_name = "Alex"
_marks = 90
```

Invalid:

```python
2name = "Alex"
student-name = "Alex"
```

Python is case-sensitive:

```python
age = 20
Age = 30
```

These are two different variables.

### Recommended naming style

Use `snake_case`:

```python
student_name = "Alex"
total_marks = 450
average_score = 90
```

---

# 9. Data Types

Common Python data types:

```text
int
float
complex
bool
str
list
tuple
set
dict
NoneType
```

Check a type:

```python
x = 10

print(type(x))
```

Output:

```text
<class 'int'>
```

---

# 10. Numbers

## Integer

Whole numbers:

```python
age = 20
count = 100
```

## Float

Decimal numbers:

```python
price = 99.99
temperature = 36.5
```

## Complex

```python
z = 2 + 3j
```

Complex numbers are less common in beginner AI programming but are part of Python's numerical capabilities.

---

# 11. Boolean

Boolean values represent:

```text
True
False
```

Example:

```python
is_student = True
is_logged_in = False
```

Booleans are commonly used in conditions.

---

# 12. Strings

A string represents text.

```python
name = "Ujjwal"
```

Strings can use:

```python
"Hello"
'Hello'
```

### String indexing

```python
name = "Python"

print(name[0])
```

Output:

```text
P
```

### Negative indexing

```python
print(name[-1])
```

Output:

```text
n
```

### Slicing

```python
name[0:3]
```

Output:

```text
Pyt
```

---

# 13. String Methods

Common methods:

```python
text = "hello world"
```

Uppercase:

```python
text.upper()
```

Lowercase:

```python
text.lower()
```

Capitalize:

```python
text.capitalize()
```

Replace:

```python
text.replace("world", "Python")
```

Split:

```python
text.split()
```

Strip whitespace:

```python
text.strip()
```

---

# 14. f-Strings

f-strings are a convenient way to insert variables into strings.

```python
name = "Ujjwal"
age = 20

print(f"My name is {name} and I am {age} years old.")
```

This is commonly used in Python applications.

---

# 15. Type Conversion

Convert between data types.

String → integer:

```python
age = int("20")
```

Integer → string:

```python
age = 20
text = str(age)
```

String → float:

```python
price = float("99.5")
```

Integer → float:

```python
x = float(10)
```

Float → integer:

```python
x = int(10.8)
```

The decimal portion is removed.

---

# 16. Operators

## Arithmetic Operators

```text
+    Addition
-    Subtraction
*    Multiplication
/    Division
//   Floor division
%    Modulus
**   Exponentiation
```

Example:

```python
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
```

---

# 17. Comparison Operators

```text
==    Equal
!=    Not equal
>     Greater than
<     Less than
>=    Greater than or equal
<=    Less than or equal
```

Example:

```python
age = 20

print(age >= 18)
```

Output:

```text
True
```

---

# 18. Logical Operators

Python has:

```text
and
or
not
```

Example:

```python
age = 20
has_id = True

if age >= 18 and has_id:
    print("Allowed")
```

---

# 19. Assignment Operators

Basic assignment:

```python
x = 10
```

Other operators:

```text
+=
-=
*=
/=
```

Example:

```python
x = 10

x += 5
```

Now:

```text
x = 15
```

---

# 20. Membership Operators

```text
in
not in
```

Example:

```python
numbers = [1, 2, 3, 4]

print(3 in numbers)
```

Output:

```text
True
```

---

# 21. Identity Operators

```text
is
is not
```

These check whether two references point to the same object.

Example:

```python
a = None

print(a is None)
```

Output:

```text
True
```

---

# 22. Conditional Statements

Python uses:

```text
if
elif
else
```

Example:

```python
marks = 75

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
else:
    grade = "C"

print(grade)
```

---

# 23. Ternary Expression

A short conditional expression:

```python
age = 20

result = "Adult" if age >= 18 else "Minor"
```

---

# 24. Lists

A list stores multiple values and is **mutable**.

```python
numbers = [10, 20, 30, 40]
```

Access:

```python
numbers[0]
```

Modify:

```python
numbers[0] = 100
```

Add:

```python
numbers.append(50)
```

Remove:

```python
numbers.remove(20)
```

Length:

```python
len(numbers)
```

---

# 25. Important List Methods

```python
numbers.append(10)
numbers.extend([20, 30])
numbers.insert(0, 5)
numbers.remove(10)
numbers.pop()
numbers.sort()
numbers.reverse()
numbers.clear()
```

---

# 26. List Slicing

```python
numbers = [10, 20, 30, 40, 50]

numbers[1:4]
```

Output:

```text
[20, 30, 40]
```

---

# 27. Tuples

A tuple is an ordered collection that is **immutable**.

```python
coordinates = (10, 20)
```

Access:

```python
coordinates[0]
```

You cannot normally modify an existing tuple element:

```python
coordinates[0] = 50
```

This produces an error.

Tuples are useful when data should not be changed.

---

# 28. Sets

A set stores unique elements.

```python
numbers = {1, 2, 3, 3, 4}

print(numbers)
```

Duplicate values are removed.

Sets are useful for:

* Removing duplicates
* Membership testing
* Mathematical set operations

Example:

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)
print(a & b)
```

---

# 29. Dictionaries

A dictionary stores data as:

```text
key → value
```

Example:

```python
student = {
    "name": "Ujjwal",
    "age": 20,
    "marks": 85
}
```

Access:

```python
student["name"]
```

Add:

```python
student["city"] = "Delhi"
```

Update:

```python
student["marks"] = 90
```

---

# 30. Dictionary Methods

```python
student.keys()
student.values()
student.items()
student.get("name")
student.pop("age")
```

Loop:

```python
for key, value in student.items():
    print(key, value)
```

Dictionaries are extremely common in Python applications and AI systems because they are useful for representing structured information.

---

# 31. Loops

## for Loop

Used to iterate over a sequence.

```python
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number)
```

---

# 32. range()

```python
for i in range(5):
    print(i)
```

Output:

```text
0
1
2
3
4
```

Syntax:

```python
range(start, stop, step)
```

Example:

```python
range(1, 10, 2)
```

---

# 33. while Loop

Runs while a condition is true.

```python
count = 0

while count < 5:
    print(count)
    count += 1
```

---

# 34. break

Stops a loop.

```python
for i in range(10):
    if i == 5:
        break

    print(i)
```

---

# 35. continue

Skips the current iteration.

```python
for i in range(5):
    if i == 2:
        continue

    print(i)
```

---

# 36. Functions

A function is a reusable block of code.

```python
def greet():
    print("Hello")
```

Call it:

```python
greet()
```

---

# 37. Function Parameters

```python
def greet(name):
    print(f"Hello {name}")
```

Call:

```python
greet("Ujjwal")
```

---

# 38. Return

Functions can return values.

```python
def add(a, b):
    return a + b

result = add(10, 20)
```

`return` sends a value back to the caller.

---

# 39. Default Arguments

```python
def greet(name="User"):
    print(f"Hello {name}")
```

Calling:

```python
greet()
```

uses the default value.

---

# 40. `*args`

Allows a function to accept multiple positional arguments.

```python
def add_all(*numbers):
    return sum(numbers)

print(add_all(1, 2, 3, 4))
```

---

# 41. `**kwargs`

Allows multiple keyword arguments.

```python
def show_info(**info):
    print(info)

show_info(name="Ujjwal", age=20)
```

---

# 42. Lambda Functions

A lambda is a small anonymous function.

```python
square = lambda x: x ** 2

print(square(5))
```

Output:

```text
25
```

Lambda functions are commonly encountered with functions such as `map()`, `filter()`, and `sorted()`.

---

# 43. List Comprehension

List comprehensions provide a concise way to create lists.

Normal loop:

```python
squares = []

for x in range(5):
    squares.append(x ** 2)
```

List comprehension:

```python
squares = [x ** 2 for x in range(5)]
```

With condition:

```python
even_numbers = [x for x in range(10) if x % 2 == 0]
```

List comprehensions are common in Python data-processing code.

---

# 44. Exception Handling

Errors can be handled using:

```text
try
except
else
finally
```

Example:

```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
```

---

# 45. Raising Exceptions

You can manually raise an exception:

```python
age = -5

if age < 0:
    raise ValueError("Age cannot be negative")
```

Exception handling is important when building reliable applications.

---

# 46. File Handling

Python can read and write files.

Write:

```python
with open("notes.txt", "w") as file:
    file.write("Hello Python")
```

Read:

```python
with open("notes.txt", "r") as file:
    content = file.read()

print(content)
```

Using `with` automatically handles closing the file.

---

# 47. Modules

A module is a Python file containing reusable code.

Suppose:

```text
math_utils.py
```

contains:

```python
def add(a, b):
    return a + b
```

Another file can import it:

```python
from math_utils import add

print(add(2, 3))
```

---

# 48. Importing Libraries

Import a complete module:

```python
import math
```

Import a specific function:

```python
from math import sqrt
```

Use an alias:

```python
import numpy as np
```

The alias `np` is a standard convention for NumPy.

---

# 49. Packages

A package is a collection of Python modules organized together.

For example:

```text
my_project/
│
├── package/
│   ├── __init__.py
│   ├── module1.py
│   └── module2.py
│
└── main.py
```

Packages help organize larger applications.

---

# 50. pip

`pip` is Python's package installer.

Install a package:

```bash
pip install numpy
```

Upgrade:

```bash
pip install --upgrade numpy
```

Uninstall:

```bash
pip uninstall numpy
```

Show installed packages:

```bash
pip list
```

---

# 51. Virtual Environments

A virtual environment creates an isolated Python environment for a project.

Create:

```bash
python -m venv .venv
```

Activate on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Then install packages:

```bash
pip install numpy pandas scikit-learn
```

Virtual environments are strongly recommended for real projects because different projects may require different package versions.

---

# 52. Object-Oriented Programming

Python supports Object-Oriented Programming (OOP).

Important concepts:

* Class
* Object
* Constructor
* Instance attributes
* Methods
* Inheritance
* Encapsulation
* Polymorphism
* Abstraction

---

# 53. Classes and Objects

A class is a blueprint for creating objects.

```python
class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(self.name, self.marks)
```

Create an object:

```python
student = Student("Ujjwal", 85)

student.display()
```

---

# 54. `self`

`self` refers to the current object.

```python
class Student:

    def __init__(self, name):
        self.name = name
```

`self.name` is an attribute belonging to the object.

---

# 55. Inheritance

A class can inherit functionality from another class.

```python
class Animal:

    def speak(self):
        print("Animal speaks")


class Dog(Animal):

    def bark(self):
        print("Dog barks")
```

Now:

```python
dog = Dog()

dog.speak()
dog.bark()
```

---

# 56. `super()`

`super()` is used to access functionality from a parent class.

```python
class Animal:

    def __init__(self, name):
        self.name = name


class Dog(Animal):

    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
```

Here:

```python
super().__init__(name)
```

calls the constructor of the parent class.

OOP becomes more useful as you build larger applications and AI systems, especially when working with frameworks and designing reusable components.

---

# 57. Iterators

An iterator is an object that allows you to iterate through values one at a time.

Important functions:

```python
iter()
next()
```

Example:

```python
numbers = [1, 2, 3]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
```

---

# 58. Generators

Generators produce values lazily using `yield`.

```python
def numbers():
    for i in range(5):
        yield i
```

Use:

```python
for number in numbers():
    print(number)
```

Generators are useful when working with large datasets because values can be processed one at a time instead of loading everything into memory.

This concept becomes particularly useful in **data pipelines and AI applications**.

---

# 59. Decorators

A decorator modifies or extends the behavior of a function.

Basic example:

```python
def decorator(func):

    def wrapper():
        print("Before function")
        func()
        print("After function")

    return wrapper
```

Usage:

```python
@decorator
def hello():
    print("Hello")
```

Decorators are commonly used in frameworks such as FastAPI and Flask.

---

# 60. Type Hints

Python allows optional type hints.

```python
def add(a: int, b: int) -> int:
    return a + b
```

Type hints improve readability and tooling.

You can also use:

```python
name: str = "Ujjwal"
age: int = 20
```

Type hints don't usually enforce types at runtime by themselves.

---

# 61. Dataclasses

For classes primarily used to store structured data, Python provides `dataclass`.

```python
from dataclasses import dataclass

@dataclass
class Student:
    name: str
    marks: float
```

Then:

```python
student = Student("Ujjwal", 85)
```

Dataclasses reduce boilerplate code.

---

# 62. Python Memory Management

Python manages memory automatically.

Important concepts include:

* Objects
* References
* Garbage collection
* Reference counting

Example:

```python
a = [1, 2, 3]
b = a
```

Both variables refer to the same list object.

Therefore:

```python
b.append(4)
```

also changes what `a` refers to.

Understanding references becomes useful when working with large numerical datasets and performance-sensitive applications.

---

# 63. Mutable vs Immutable Objects

### Mutable

Can be changed after creation.

Examples:

```text
list
dict
set
```

### Immutable

Cannot be changed after creation.

Examples:

```text
int
float
str
tuple
bool
```

Example:

```python
numbers = [1, 2, 3]
numbers.append(4)
```

The list is modified.

---

# 64. Shallow Copy vs Deep Copy

Copying objects can sometimes cause unexpected behavior.

```python
import copy

a = [[1, 2], [3, 4]]

b = copy.copy(a)
c = copy.deepcopy(a)
```

A shallow copy copies the outer object while nested objects may still be shared.

A deep copy recursively copies nested objects.

This becomes important when working with nested data structures.

---

# 65. Scope

Python has different variable scopes.

Common scopes:

```text
Local
Enclosing
Global
Built-in
```

This is often remembered as **LEGB**.

Example:

```python
x = 10

def test():
    x = 20
    print(x)

test()
print(x)
```

Output:

```text
20
10
```

The local variable does not change the global variable.

---

# 66. `if __name__ == "__main__"`

Common Python pattern:

```python
def main():
    print("Program started")


if __name__ == "__main__":
    main()
```

This ensures `main()` runs when the file is executed directly but not automatically when the file is imported as a module.

This pattern is useful for organizing Python projects.

---

# 67. PEP 8

**PEP 8** is Python's main style guide.

Important practices include:

* 4 spaces for indentation
* Clear variable names
* `snake_case` for functions and variables
* `PascalCase` for classes
* Reasonable line lengths
* Spaces around operators
* Organized imports

Example:

```python
student_name = "Ujjwal"
total_marks = 450
```

instead of:

```python
x="Ujjwal"
y=450
```

when descriptive names are appropriate.

---

# 68. Python for Data Science

Python provides a powerful data-science ecosystem.

Typical workflow:

```text
Raw Data
   ↓
Python
   ↓
NumPy
   ↓
Pandas
   ↓
Data Cleaning
   ↓
Visualization
   ↓
Scikit-learn
   ↓
Machine Learning
```

---

# 69. Python for AI Engineering

For AI engineering, Python is used for much more than training models.

A typical AI application may involve:

```text
Python
│
├── Data Processing
│   ├── NumPy
│   └── Pandas
│
├── Machine Learning
│   └── Scikit-learn
│
├── Deep Learning
│   └── PyTorch
│
├── LLMs
│   ├── Transformers
│   └── LLM APIs
│
├── Backend
│   └── FastAPI
│
├── Databases
│   └── SQL
│
└── Deployment
    ├── Docker
    └── Cloud
```

Therefore, strong Python fundamentals are extremely valuable for an AI engineer.

---

# 70. Python Concepts to Prioritize for AI/ML

You do NOT need to master every advanced Python feature before starting AI.

Prioritize:

### Tier 1 — Must Know

* Variables
* Data types
* Strings
* Lists
* Tuples
* Sets
* Dictionaries
* Conditions
* Loops
* Functions
* List comprehensions
* Exceptions
* File handling
* Modules
* Imports
* pip
* Virtual environments

### Tier 2 — Important

* OOP
* `*args`
* `**kwargs`
* Lambda
* Iterators
* Generators
* Decorators
* Type hints
* Context managers
* Mutable vs immutable objects
* Scope
* Package structure

### Tier 3 — Learn as Needed

* Advanced metaprogramming
* Descriptors
* Custom protocols
* Advanced decorators
* Python internals
* Advanced concurrency
* C extensions

Don't spend months trying to master every Python feature before moving into AI.

---

# 71. Python + NumPy

Python lists:

```python
numbers = [1, 2, 3, 4]
```

NumPy arrays:

```python
import numpy as np

numbers = np.array([1, 2, 3, 4])
```

With NumPy:

```python
numbers * 2
```

produces:

```text
[2 4 6 8]
```

NumPy is designed for efficient numerical operations, which makes it much more suitable for numerical computing than relying exclusively on Python lists.

---

# 72. Python Learning Roadmap

A practical order for learning Python:

```text
1. Syntax
   ↓
2. Variables & Data Types
   ↓
3. Operators
   ↓
4. Conditions
   ↓
5. Lists / Tuples / Sets / Dictionaries
   ↓
6. Loops
   ↓
7. Functions
   ↓
8. Comprehensions
   ↓
9. Modules & Packages
   ↓
10. File Handling
   ↓
11. Exceptions
   ↓
12. OOP
   ↓
13. Iterators & Generators
   ↓
14. Decorators
   ↓
15. Type Hints
   ↓
16. Virtual Environments
   ↓
17. NumPy
   ↓
18. Pandas
   ↓
19. Scikit-learn
   ↓
20. PyTorch
```

---

# 73. Key Takeaway

Python is not just a programming language for AI—it is the **primary language used across a large part of the modern AI/ML ecosystem**.

For an AI engineer, the goal is not to memorize Python syntax.

The goal is to be able to:

* Write clean Python
* Structure programs properly
* Work with data
* Debug errors
* Use external libraries
* Build reusable components
* Understand OOP
* Handle files and APIs
* Manage environments and dependencies
* Write efficient numerical code
* Understand enough Python internals to diagnose problems

Once the fundamentals are strong, libraries such as **NumPy, Pandas, scikit-learn, PyTorch, and FastAPI** become much easier to learn.
