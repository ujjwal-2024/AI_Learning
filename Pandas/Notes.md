# Python Pandas — Complete Notes

> Pandas is a Python library used for **data manipulation, cleaning, analysis, and preprocessing**.
> It is heavily used in **Data Science, Machine Learning, AI, and Data Analytics**.

---

## 1. Installation

```bash
pip install pandas
```

Import:

```python
import pandas as pd
```

Check version:

```python
print(pd.__version__)
```

---

# 2. Pandas Data Structures

Pandas mainly provides two important data structures:

1. **Series** → 1-dimensional
2. **DataFrame** → 2-dimensional

---

## 3. Series

A Series is like a single column of data.

```python
import pandas as pd

s = pd.Series([10, 20, 30, 40])

print(s)
```

Output:

```text
0    10
1    20
2    30
3    40
dtype: int64
```

### Series with custom index

```python
s = pd.Series(
    [90, 85, 95],
    index=["Math", "Physics", "AI"]
)
```

Access:

```python
print(s["Math"])
```

### Series from dictionary

```python
data = {
    "Math": 90,
    "Physics": 85,
    "AI": 95
}

s = pd.Series(data)
```

---

# 4. DataFrame

A DataFrame is a table consisting of rows and columns.

```python
data = {
    "Name": ["Ujjwal", "Rahul", "Aman"],
    "Age": [21, 22, 20],
    "Marks": [85, 90, 78]
}

df = pd.DataFrame(data)

print(df)
```

Output:

```text
     Name  Age  Marks
0  Ujjwal   21     85
1  Rahul   22     90
2    Aman   20     78
```

Think of a DataFrame like an **Excel spreadsheet or SQL table**.

---

# 5. Creating DataFrames

### From dictionary

```python
df = pd.DataFrame({
    "Name": ["A", "B", "C"],
    "Age": [20, 21, 22]
})
```

### From list

```python
data = [
    ["Ujjwal", 21],
    ["Rahul", 22],
    ["Aman", 20]
]

df = pd.DataFrame(data, columns=["Name", "Age"])
```

### Empty DataFrame

```python
df = pd.DataFrame()
```

---

# 6. Reading Data

## CSV

```python
df = pd.read_csv("data.csv")
```

## Excel

```python
df = pd.read_excel("data.xlsx")
```

## JSON

```python
df = pd.read_json("data.json")
```

## SQL

```python
df = pd.read_sql(query, connection)
```

---

# 7. Writing Data

### Save CSV

```python
df.to_csv("output.csv", index=False)
```

### Save Excel

```python
df.to_excel("output.xlsx", index=False)
```

### Save JSON

```python
df.to_json("output.json")
```

---

# 8. Inspecting Data

These functions are extremely important.

### First rows

```python
df.head()
```

```python
df.head(10)
```

### Last rows

```python
df.tail()
```

### Number of rows and columns

```python
df.shape
```

Example:

```text
(1000, 5)
```

Means:

```text
1000 rows
5 columns
```

### Column names

```python
df.columns
```

### Data types

```python
df.dtypes
```

### General information

```python
df.info()
```

### Statistical summary

```python
df.describe()
```

### Unique values

```python
df["Age"].unique()
```

### Number of unique values

```python
df["Age"].nunique()
```

### Value frequency

```python
df["City"].value_counts()
```

---

# 9. Selecting Columns

### Single column

```python
df["Name"]
```

### Multiple columns

```python
df[["Name", "Age"]]
```

---

# 10. Selecting Rows

## `iloc`

`iloc` selects data using **integer positions**.

```python
df.iloc[0]
```

First row.

```python
df.iloc[0:5]
```

First five rows.

```python
df.iloc[0, 1]
```

First row, second column.

```python
df.iloc[:, 0]
```

All rows, first column.

```python
df.iloc[:, 0:3]
```

All rows, first three columns.

---

# 11. `loc`

`loc` selects data using **labels/conditions**.

```python
df.loc[0]
```

Select rows based on index:

```python
df.loc[0:3]
```

Select specific columns:

```python
df.loc[:, ["Name", "Age"]]
```

---

# 12. Filtering Data

Suppose:

```python
df = pd.DataFrame({
    "Name": ["A", "B", "C", "D"],
    "Age": [20, 25, 18, 30],
    "Marks": [80, 90, 65, 95]
})
```

### Age greater than 20

```python
df[df["Age"] > 20]
```

### Marks greater than 80

```python
df[df["Marks"] > 80]
```

### Multiple conditions

```python
df[(df["Age"] > 20) & (df["Marks"] > 80)]
```

### OR

```python
df[(df["Age"] > 25) | (df["Marks"] > 90)]
```

### NOT

```python
df[~(df["Age"] > 20)]
```

Use:

* `&` → AND
* `|` → OR
* `~` → NOT

---

# 13. `isin()`

Check whether values belong to a list.

```python
df[df["City"].isin(["Delhi", "Mumbai"])]
```

---

# 14. `between()`

```python
df[df["Age"].between(18, 25)]
```

---

# 15. Sorting

### Sort ascending

```python
df.sort_values("Marks")
```

### Sort descending

```python
df.sort_values("Marks", ascending=False)
```

### Sort by multiple columns

```python
df.sort_values(
    ["Age", "Marks"],
    ascending=[True, False]
)
```

---

# 16. Adding Columns

```python
df["Passed"] = df["Marks"] >= 40
```

Create calculated column:

```python
df["Bonus"] = df["Marks"] + 5
```

---

# 17. Updating Columns

```python
df["Marks"] = df["Marks"] + 10
```

Rename:

```python
df["Marks"] = df["Marks"].astype(float)
```

---

# 18. Rename Columns

```python
df.rename(
    columns={
        "Name": "Student_Name",
        "Marks": "Score"
    },
    inplace=True
)
```

---

# 19. Drop Columns

```python
df.drop("Age", axis=1)
```

Multiple columns:

```python
df.drop(
    ["Age", "Marks"],
    axis=1
)
```

Using `columns` is often clearer:

```python
df.drop(columns=["Age", "Marks"])
```

---

# 20. Drop Rows

```python
df.drop(index=0)
```

Multiple rows:

```python
df.drop(index=[0, 1, 2])
```

---

# 21. Missing Values

Missing values are usually represented by `NaN`.

```python
df.isna()
```

or:

```python
df.isnull()
```

Both are commonly used.

---

## Count missing values

```python
df.isnull().sum()
```

Percentage:

```python
df.isnull().mean() * 100
```

---

# 22. Removing Missing Values

Remove rows containing missing values:

```python
df.dropna()
```

Remove columns:

```python
df.dropna(axis=1)
```

Only remove rows where all values are missing:

```python
df.dropna(how="all")
```

---

# 23. Filling Missing Values

Fill with a fixed value:

```python
df["Age"] = df["Age"].fillna(0)
```

Fill with mean:

```python
df["Age"] = df["Age"].fillna(
    df["Age"].mean()
)
```

Fill with median:

```python
df["Age"] = df["Age"].fillna(
    df["Age"].median()
)
```

Fill with mode:

```python
df["City"] = df["City"].fillna(
    df["City"].mode()[0]
)
```

### Important

For ML preprocessing:

* Mean → useful when data is roughly symmetric
* Median → useful when outliers exist
* Mode → commonly used for categorical data

---

# 24. Duplicate Data

Check duplicates:

```python
df.duplicated()
```

Count:

```python
df.duplicated().sum()
```

Remove duplicates:

```python
df.drop_duplicates()
```

Based on specific columns:

```python
df.drop_duplicates(
    subset=["Name"]
)
```

---

# 25. Data Types

Check:

```python
df.dtypes
```

Convert:

```python
df["Age"] = df["Age"].astype(int)
```

Convert to float:

```python
df["Marks"] = df["Marks"].astype(float)
```

Convert to string:

```python
df["Name"] = df["Name"].astype(str)
```

---

# 26. Numeric Conversion

Useful when a column contains invalid numeric values.

```python
df["Price"] = pd.to_numeric(
    df["Price"],
    errors="coerce"
)
```

`errors="coerce"` converts invalid values into `NaN`.

---

# 27. String Operations

Pandas provides `.str` for string operations.

```python
df["Name"].str.lower()
```

```python
df["Name"].str.upper()
```

```python
df["Name"].str.title()
```

Remove spaces:

```python
df["Name"].str.strip()
```

Contains:

```python
df[df["Name"].str.contains("ujjwal", case=False)]
```

Replace:

```python
df["Name"].str.replace("old", "new")
```

Get string length:

```python
df["Name"].str.len()
```

---

# 28. Date and Time

Convert to datetime:

```python
df["Date"] = pd.to_datetime(df["Date"])
```

Extract year:

```python
df["Date"].dt.year
```

Month:

```python
df["Date"].dt.month
```

Day:

```python
df["Date"].dt.day
```

Day of week:

```python
df["Date"].dt.day_name()
```

---

# 29. Index

Set a column as index:

```python
df.set_index("Name")
```

Reset index:

```python
df.reset_index()
```

Change index permanently:

```python
df.set_index("Name", inplace=True)
```

---

# 30. `apply()`

`apply()` allows you to apply a function to data.

```python
df["Marks"].apply(lambda x: x + 5)
```

Example:

```python
def grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    else:
        return "C"

df["Grade"] = df["Marks"].apply(grade)
```

---

# 31. `map()`

Usually used with Series.

```python
df["Gender"] = df["Gender"].map({
    "Male": 1,
    "Female": 0
})
```

---

# 32. `replace()`

```python
df["City"] = df["City"].replace({
    "Delhi": "New Delhi"
})
```

---

# 33. `groupby()`

One of the most important Pandas operations.

Suppose:

```python
df.groupby("Department")["Salary"].mean()
```

Calculate sum:

```python
df.groupby("Department")["Salary"].sum()
```

Count:

```python
df.groupby("Department")["Salary"].count()
```

Multiple aggregations:

```python
df.groupby("Department")["Salary"].agg(
    ["mean", "min", "max", "sum"]
)
```

Group by multiple columns:

```python
df.groupby(
    ["Department", "Gender"]
)["Salary"].mean()
```

---

# 34. Aggregation

Common functions:

```python
df["Marks"].mean()
df["Marks"].median()
df["Marks"].mode()
df["Marks"].sum()
df["Marks"].min()
df["Marks"].max()
df["Marks"].std()
df["Marks"].var()
df["Marks"].count()
```

---

# 35. `agg()`

```python
df["Marks"].agg(
    ["mean", "median", "min", "max"]
)
```

Different operations for different columns:

```python
df.agg({
    "Age": "mean",
    "Marks": ["mean", "max"]
})
```

---

# 36. Combining DataFrames

## `concat()`

Combine DataFrames vertically:

```python
result = pd.concat(
    [df1, df2],
    ignore_index=True
)
```

Horizontal:

```python
result = pd.concat(
    [df1, df2],
    axis=1
)
```

---

# 37. Merge

Similar to SQL JOIN.

```python
result = pd.merge(
    df1,
    df2,
    on="id"
)
```

### Inner Join

```python
pd.merge(
    df1,
    df2,
    on="id",
    how="inner"
)
```

### Left Join

```python
pd.merge(
    df1,
    df2,
    on="id",
    how="left"
)
```

### Right Join

```python
pd.merge(
    df1,
    df2,
    on="id",
    how="right"
)
```

### Outer Join

```python
pd.merge(
    df1,
    df2,
    on="id",
    how="outer"
)
```

---

# 38. Join

```python
df1.join(df2)
```

Useful when joining based on indexes.

---

# 39. Pivot Tables

Useful for summarizing data.

```python
pd.pivot_table(
    df,
    values="Salary",
    index="Department",
    aggfunc="mean"
)
```

Multiple dimensions:

```python
pd.pivot_table(
    df,
    values="Salary",
    index="Department",
    columns="Gender",
    aggfunc="mean"
)
```

---

# 40. Crosstab

Used to create frequency tables.

```python
pd.crosstab(
    df["Gender"],
    df["Department"]
)
```

---

# 41. `query()`

Instead of:

```python
df[df["Age"] > 20]
```

You can write:

```python
df.query("Age > 20")
```

Multiple conditions:

```python
df.query("Age > 20 and Marks > 80")
```

---

# 42. Random Sampling

Random rows:

```python
df.sample(5)
```

Random fraction:

```python
df.sample(frac=0.1)
```

10% of the dataset.

---

# 43. Reset and Reorder Columns

Reorder:

```python
df = df[
    ["Name", "Age", "Marks"]
]
```

---

# 44. Transpose

```python
df.T
```

Rows become columns and columns become rows.

---

# 45. Copy

Create an independent copy:

```python
df2 = df.copy()
```

Prefer `copy()` when modifying a DataFrame derived from another DataFrame.

---

# 46. Combining Conditions

Example:

```python
result = df[
    (df["Age"] >= 18) &
    (df["Marks"] >= 60) &
    (df["City"] == "Delhi")
]
```

Always put each condition inside parentheses when using `&` or `|`.

---

# 47. Handling Outliers

Pandas can help identify outliers.

Example using IQR:

```python
Q1 = df["Salary"].quantile(0.25)
Q3 = df["Salary"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = df[
    (df["Salary"] < lower) |
    (df["Salary"] > upper)
]
```

---

# 48. Correlation

```python
df.corr(numeric_only=True)
```

Correlation measures relationships between numerical variables.

Example:

```text
1.0  → strong positive relationship
0.0  → little/no linear relationship
-1.0 → strong negative relationship
```

---

# 49. Basic Data Analysis Workflow

A common workflow:

```python
import pandas as pd

# Load data
df = pd.read_csv("data.csv")

# Inspect
print(df.head())
print(df.shape)
print(df.info())
print(df.describe())

# Check missing values
print(df.isnull().sum())

# Check duplicates
print(df.duplicated().sum())

# Clean data
df = df.drop_duplicates()

# Fill missing values
df["Age"] = df["Age"].fillna(
    df["Age"].median()
)

# Analyze
print(df.groupby("Department")["Salary"].mean())

# Save cleaned data
df.to_csv("cleaned_data.csv", index=False)
```

---

# 50. Pandas for Machine Learning

Pandas is commonly used before feeding data into ML algorithms.

Typical pipeline:

```text
Raw Dataset
     ↓
Load with Pandas
     ↓
Inspect Data
     ↓
Clean Data
     ↓
Handle Missing Values
     ↓
Remove Duplicates
     ↓
Handle Outliers
     ↓
Convert Data Types
     ↓
Encode Categorical Data
     ↓
Feature Engineering
     ↓
Train/Test Split
     ↓
ML Model
```

Example:

```python
df = pd.read_csv("dataset.csv")

# Inspect
print(df.info())

# Missing values
print(df.isnull().sum())

# Remove duplicates
df = df.drop_duplicates()

# Fill missing numerical values
df["Age"] = df["Age"].fillna(
    df["Age"].median()
)

# Convert categorical values
df["Gender"] = df["Gender"].map({
    "Male": 1,
    "Female": 0
})
```

---

# 51. Pandas vs NumPy

| Pandas                | NumPy                    |
| --------------------- | ------------------------ |
| Data manipulation     | Numerical computing      |
| DataFrame             | ndarray                  |
| Series                | Array                    |
| Handles tabular data  | Handles numerical arrays |
| Labels/indexes        | Mostly position-based    |
| Missing data handling | More limited             |
| CSV/Excel data        | Mathematical operations  |

They are often used together:

```python
import numpy as np
import pandas as pd
```

---

# 52. Pandas vs SQL

Many Pandas operations have SQL equivalents.

| SQL      | Pandas            |
| -------- | ----------------- |
| SELECT   | `df[columns]`     |
| WHERE    | Boolean filtering |
| GROUP BY | `groupby()`       |
| ORDER BY | `sort_values()`   |
| JOIN     | `merge()`         |
| COUNT    | `count()`         |
| AVG      | `mean()`          |
| DISTINCT | `unique()`        |
| LIMIT    | `head()`          |

---

# 53. Important Pandas Methods

### Inspection

```python
head()
tail()
shape
info()
describe()
dtypes
columns
```

### Selection

```python
loc[]
iloc[]
```

### Cleaning

```python
dropna()
fillna()
drop_duplicates()
replace()
astype()
```

### Transformation

```python
apply()
map()
rename()
```

### Analysis

```python
groupby()
agg()
value_counts()
mean()
median()
sum()
min()
max()
std()
```

### Combining

```python
concat()
merge()
join()
```

### Sorting

```python
sort_values()
sort_index()
```

---

# 54. Common Mistakes

### Mistake 1 — Using `and` instead of `&`

Wrong:

```python
df[(df["Age"] > 20) and (df["Marks"] > 80)]
```

Correct:

```python
df[(df["Age"] > 20) & (df["Marks"] > 80)]
```

---

### Mistake 2 — Forgetting parentheses

Wrong:

```python
df[df["Age"] > 20 & df["Marks"] > 80]
```

Correct:

```python
df[
    (df["Age"] > 20) &
    (df["Marks"] > 80)
]
```

---

### Mistake 3 — Accidentally modifying original data

Prefer:

```python
new_df = df.copy()
```

when creating a DataFrame you intend to modify separately.

---

# 55. Important Concepts to Master for AI/ML

For an AI/ML engineer, prioritize these Pandas concepts:

### Must Know

* DataFrame
* Series
* `read_csv()`
* `head()`
* `tail()`
* `shape`
* `info()`
* `describe()`
* `loc`
* `iloc`
* Boolean filtering
* `isna()`
* `fillna()`
* `dropna()`
* `drop_duplicates()`
* `astype()`
* `groupby()`
* `agg()`
* `sort_values()`
* `value_counts()`
* `apply()`
* `map()`
* `merge()`
* `concat()`
* `to_datetime()`
* `to_csv()`

### Learn Later

* MultiIndex
* Advanced reshaping
* Advanced window functions
* Performance optimization
* Chunk processing
* Categorical data
* Advanced time-series operations

---

# 56. Pandas Cheat Sheet

```python
import pandas as pd

# Load
df = pd.read_csv("data.csv")

# Inspect
df.head()
df.tail()
df.shape
df.info()
df.describe()
df.columns
df.dtypes

# Select
df["Name"]
df[["Name", "Age"]]
df.loc[0]
df.iloc[0]

# Filter
df[df["Age"] > 20]

# Missing values
df.isna().sum()
df.dropna()
df.fillna(0)

# Duplicates
df.duplicated().sum()
df.drop_duplicates()

# Sort
df.sort_values("Age")
df.sort_values("Age", ascending=False)

# Modify
df["New"] = df["Age"] * 2

# Rename
df.rename(columns={"Age": "Student_Age"})

# Group
df.groupby("City")["Age"].mean()

# Aggregate
df["Age"].mean()
df["Age"].median()
df["Age"].sum()
df["Age"].min()
df["Age"].max()

# Combine
pd.concat([df1, df2])
pd.merge(df1, df2, on="id")

# Date
df["Date"] = pd.to_datetime(df["Date"])

# Save
df.to_csv("output.csv", index=False)
```

---

# 57. Practical Pandas Learning Order

```text
1. Series
2. DataFrame
3. Reading CSV
4. Data inspection
5. Selecting columns/rows
6. Filtering
7. Sorting
8. Missing values
9. Duplicates
10. Data type conversion
11. String operations
12. DateTime
13. apply/map
14. groupby
15. aggregation
16. merge/join/concat
17. Pivot tables
18. Feature engineering
19. Data cleaning
20. ML preprocessing
```

---

# 58. Key Takeaway

Pandas is not just a library for reading CSV files.

For AI/ML, Pandas is primarily used for:

```text
Data Loading
     ↓
Data Exploration
     ↓
Data Cleaning
     ↓
Data Transformation
     ↓
Feature Engineering
     ↓
Data Preparation
     ↓
Machine Learning
```


