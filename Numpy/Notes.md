# NumPy — Numerical Python

## 1. What is NumPy? 

**NumPy (Numerical Python)** is a fundamental Python library used for **numerical computing and scientific computing**.

It provides a powerful data structure called the **NumPy array (`ndarray`)**, which allows us to store and manipulate large amounts of numerical data efficiently.

NumPy is especially important in **Data Science, Machine Learning, Deep Learning, Computer Vision, and AI** because most AI algorithms involve mathematical operations on vectors, matrices, and multidimensional data.

```python
import numpy as np
```

Here, `np` is the commonly used alias for NumPy.

---

# 2. Why Do We Need NumPy?

Python already has lists, so why use NumPy?

Python lists are general-purpose containers and can store different types of objects. NumPy arrays are specifically optimized for numerical operations.

### Python List

```python
numbers = [1, 2, 3, 4, 5]

result = [x * 2 for x in numbers]
```

### NumPy Array

```python
import numpy as np

numbers = np.array([1, 2, 3, 4, 5])

result = numbers * 2

print(result)
```

Output:

```text
[ 2  4  6  8 10]
```

NumPy allows us to perform operations on the entire array without explicitly writing a loop.

This is called **vectorized computation**.

---

# 3. Important Features of NumPy

NumPy provides:

* Fast numerical computation
* Multidimensional arrays
* Vectorized operations
* Broadcasting
* Mathematical functions
* Statistical functions
* Linear algebra operations
* Random number generation
* Array manipulation
* Efficient memory usage
* Foundation for many other Python libraries

Libraries such as **Pandas, SciPy, scikit-learn, and parts of the scientific Python ecosystem** rely heavily on NumPy concepts and arrays.

---

# 4. NumPy Array

The main object in NumPy is the:

```text
ndarray
```

which means **N-dimensional array**.

An array can have:

* 1 dimension → vector
* 2 dimensions → matrix
* 3 or more dimensions → multidimensional array/tensor-like structure

Example:

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)
```

Output:

```text
[1 2 3 4 5]
```

---

# 5. Creating NumPy Arrays

## From a Python List

```python
arr = np.array([1, 2, 3, 4])
```

## 2D Array

```python
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
```

## 3D Array

```python
arr = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])
```

---

# 6. Important Array Properties

Consider:

```python
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
```

## ndim

Returns the number of dimensions.

```python
arr.ndim
```

Output:

```text
2
```

## shape

Returns the size of each dimension.

```python
arr.shape
```

Output:

```text
(2, 3)
```

This means:

```text
2 rows
3 columns
```

## size

Returns the total number of elements.

```python
arr.size
```

Output:

```text
6
```

## dtype

Returns the data type of the elements.

```python
arr.dtype
```

For example:

```text
int64
```

---

# 7. Creating Special Arrays

## Zeros

```python
np.zeros(5)
```

Output:

```text
[0. 0. 0. 0. 0.]
```

2D:

```python
np.zeros((2, 3))
```

---

## Ones

```python
np.ones(5)
```

2D:

```python
np.ones((2, 3))
```

---

## Full

Creates an array filled with a specific value.

```python
np.full((2, 3), 7)
```

---

## Identity Matrix

```python
np.eye(3)
```

Output:

```text
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
```

Identity matrices are important in linear algebra.

---

## arange()

Similar to Python's `range()`.

```python
np.arange(0, 10, 2)
```

Output:

```text
[0 2 4 6 8]
```

Syntax:

```python
np.arange(start, stop, step)
```

---

## linspace()

Creates evenly spaced numbers between two values.

```python
np.linspace(0, 1, 5)
```

Output:

```text
[0.   0.25 0.5  0.75 1.  ]
```

This is commonly useful in numerical and mathematical computations.

---

# 8. Indexing

NumPy indexing is similar to Python list indexing.

```python
arr = np.array([10, 20, 30, 40, 50])

print(arr[0])
```

Output:

```text
10
```

Negative indexing:

```python
arr[-1]
```

Output:

```text
50
```

---

# 9. Slicing

Syntax:

```python
array[start:stop:step]
```

Example:

```python
arr = np.array([10, 20, 30, 40, 50])

arr[1:4]
```

Output:

```text
[20 30 40]
```

Every second element:

```python
arr[::2]
```

Output:

```text
[10 30 50]
```

---

# 10. 2D Array Indexing

```python
arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
```

Access row 1, column 2:

```python
arr[0, 1]
```

Output:

```text
20
```

Access second row:

```python
arr[1]
```

Access second column:

```python
arr[:, 1]
```

Output:

```text
[20 50]
```

---

# 11. Reshaping

`reshape()` changes the shape of an array without changing its data.

```python
arr = np.array([1, 2, 3, 4, 5, 6])

new_arr = arr.reshape(2, 3)
```

Result:

```text
[[1 2 3]
 [4 5 6]]
```

The total number of elements must remain the same.

For example:

```text
6 elements → 2 × 3
```

is valid.

But:

```text
6 elements → 4 × 4
```

is invalid.

---

# 12. Flattening

`flatten()` converts a multidimensional array into a 1D array.

```python
arr = np.array([
    [1, 2],
    [3, 4]
])

arr.flatten()
```

Output:

```text
[1 2 3 4]
```

---

# 13. Array Arithmetic

NumPy allows element-wise arithmetic.

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
```

Addition:

```python
a + b
```

Output:

```text
[5 7 9]
```

Subtraction:

```python
a - b
```

Multiplication:

```python
a * b
```

Division:

```python
a / b
```

Power:

```python
a ** 2
```

These operations are performed element by element.

---

# 14. Scalar Operations

A scalar is a single number.

```python
arr = np.array([1, 2, 3, 4])

arr + 10
```

Output:

```text
[11 12 13 14]
```

Similarly:

```python
arr * 5
```

Output:

```text
[ 5 10 15 20]
```

This is one example of **broadcasting**.

---

# 15. Broadcasting

Broadcasting allows NumPy to perform operations between arrays with compatible shapes.

Example:

```python
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

arr + 10
```

NumPy effectively applies `10` to every element.

Another example:

```python
a = np.array([1, 2, 3])

b = np.array([
    [10],
    [20],
    [30]
])

a + b
```

NumPy automatically expands the arrays to compatible shapes.

Broadcasting is extremely important in **machine learning and deep learning**, where operations are frequently performed on matrices and batches of data.

---

# 16. Aggregation Functions

NumPy provides functions for summarizing numerical data.

```python
arr = np.array([10, 20, 30, 40, 50])
```

Sum:

```python
np.sum(arr)
```

Mean:

```python
np.mean(arr)
```

Minimum:

```python
np.min(arr)
```

Maximum:

```python
np.max(arr)
```

Standard deviation:

```python
np.std(arr)
```

Variance:

```python
np.var(arr)
```

---

# 17. Axis

`axis` is extremely important when working with multidimensional arrays.

Consider:

```python
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
```

### Sum of all elements

```python
np.sum(arr)
```

### Sum across rows

```python
np.sum(arr, axis=1)
```

Output:

```text
[6 15]
```

### Sum across columns

```python
np.sum(arr, axis=0)
```

Output:

```text
[5 7 9]
```

Understanding `axis` is essential for working with datasets.

---

# 18. Boolean Masking

Boolean masking allows us to filter data based on conditions.

```python
arr = np.array([10, 25, 30, 5, 40])

arr > 20
```

Output:

```text
[False  True  True False  True]
```

We can use this condition to filter the array:

```python
arr[arr > 20]
```

Output:

```text
[25 30 40]
```

This is very useful for data preprocessing.

---

# 19. Vectorization

Vectorization means performing operations on entire arrays instead of explicitly writing Python loops.

Without vectorization:

```python
result = []

for x in arr:
    result.append(x * 2)
```

With NumPy:

```python
result = arr * 2
```

Vectorized operations are generally faster and produce cleaner numerical code.

This is one of the major reasons NumPy is widely used for numerical computing.

---

# 20. Mathematical Functions

NumPy provides many mathematical functions.

Examples:

```python
np.sqrt(arr)
np.square(arr)
np.abs(arr)
np.exp(arr)
np.log(arr)
np.sin(arr)
np.cos(arr)
```

Example:

```python
arr = np.array([1, 4, 9])

np.sqrt(arr)
```

Output:

```text
[1. 2. 3.]
```

---

# 21. Random Numbers

NumPy provides tools for generating random data.

Modern NumPy code commonly uses:

```python
rng = np.random.default_rng()
```

Then:

```python
rng.random(5)
```

Generate random integers:

```python
rng.integers(1, 10, size=5)
```

Set a seed for reproducibility:

```python
rng = np.random.default_rng(42)
```

Random number generation is frequently used when creating datasets, simulations, experiments, and ML workflows.

---

# 22. Linear Algebra

NumPy provides important linear algebra operations.

Matrix multiplication:

```python
A @ B
```

or:

```python
np.matmul(A, B)
```

Dot product:

```python
np.dot(a, b)
```

Transpose:

```python
A.T
```

Other linear algebra functionality is available through:

```python
np.linalg
```

For example:

```python
np.linalg.inv(A)
np.linalg.det(A)
np.linalg.eig(A)
```

Linear algebra is fundamental to machine learning because many ML algorithms involve vectors and matrices.

---

# 23. NumPy and Machine Learning

NumPy is important for understanding what happens underneath many ML algorithms.

For example, a dataset can be represented as:

```python
X = np.array([
    [1200, 3],
    [1500, 4],
    [1800, 4],
    [2000, 5]
])
```

Here:

```text
Rows    → observations/examples
Columns → features
```

A target variable could be:

```python
y = np.array([50, 65, 75, 90])
```

Many ML operations involve:

* matrix multiplication
* normalization
* statistical calculations
* vector operations
* transformations
* distance calculations
* optimization calculations

Therefore, understanding NumPy makes it easier to understand what ML libraries are doing internally.

---

# 24. NumPy in the AI/ML Stack

A simplified AI/ML workflow can look like:

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
PyTorch / TensorFlow
   ↓
Machine Learning / Deep Learning
```

NumPy is not the only library used in AI, but its array concepts are foundational.

---

# 25. Important NumPy Concepts to Master

For AI/ML, prioritize these topics:

### Must Know

* `ndarray`
* `shape`
* `ndim`
* `size`
* `dtype`
* indexing
* slicing
* reshaping
* axis
* aggregation
* boolean masking
* vectorization
* broadcasting
* array arithmetic

### Important for ML

* normalization
* random number generation
* matrix multiplication
* dot product
* transpose
* linear algebra
* handling multidimensional arrays

### Useful but Don't Overfocus Initially

* advanced memory layout
* obscure NumPy functions
* highly specialized APIs

You don't need to memorize the entire NumPy API.

The goal is to understand the **array model and numerical operations** and know how to look up functions when needed.

---

# 26. Simple Practice Example

```python
import numpy as np

marks = np.array([
    [70, 80, 90],
    [60, 75, 85],
    [90, 95, 88]
])

print("Shape:", marks.shape)
print("Average:", marks.mean())
print("Subject averages:", marks.mean(axis=0))
print("Student averages:", marks.mean(axis=1))
print("Highest:", marks.max())
print("Lowest:", marks.min())

print("Students with average > 75:")
print(marks[marks.mean(axis=1) > 75])
```

This single example combines:

* arrays
* shape
* aggregation
* axis
* mean
* boolean masking

---

# 27. NumPy Learning Goal

The goal is **not** to memorize every NumPy function.

The goal is to become comfortable with:

```text
Data
 ↓
Array
 ↓
Shape
 ↓
Indexing / Slicing
 ↓
Transformation
 ↓
Vectorized Operations
 ↓
Broadcasting
 ↓
Statistics
 ↓
Linear Algebra
 ↓
ML
```

Once these concepts are comfortable, moving to **Pandas and scikit-learn** becomes much easier.

---

# Quick Revision

```python
import numpy as np

# Create
arr = np.array([1, 2, 3])

# Properties
arr.shape
arr.ndim
arr.size
arr.dtype

# Create special arrays
np.zeros((2, 3))
np.ones((2, 3))
np.eye(3)
np.arange(10)
np.linspace(0, 1, 5)

# Manipulation
arr.reshape(...)
arr.flatten()

# Statistics
np.mean(arr)
np.sum(arr)
np.min(arr)
np.max(arr)
np.std(arr)

# Filtering
arr[arr > 2]

# Mathematical operations
np.sqrt(arr)
np.exp(arr)
np.log(arr)

# Linear algebra
A @ B
A.T
np.dot(A, B)
np.linalg

# Random
rng = np.random.default_rng(42)
rng.random(5)
rng.integers(1, 10, size=5)
```

**Key idea:** NumPy gives Python an efficient way to work with **vectors, matrices, and multidimensional numerical data**, which makes it one of the foundational tools for AI and machine learning.
