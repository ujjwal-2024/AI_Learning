import pandas as pd

df = pd.read_csv(r"C:\AI Engineering\AI_Learning\Pandas\practice\data.csv")

# =========================
# 1. BASIC INFORMATION
# =========================

print(df.head())
# Shows the first 5 rows

print(df.shape)
# Shows (rows, columns)

print(df.columns)
# Shows all column names

print(df.dtypes)
# Shows the data type of each column

df.info()
# Shows column information and missing values

print(df.describe())
# Gives statistics like mean, min, max, etc.


# =========================
# 2. SELECT COLUMNS
# =========================

print(df["Pulse"])
# Selects only the Pulse column

print(df[["Pulse", "Calories"]])
# Selects Pulse and Calories columns


# =========================
# 3. SELECT ROWS
# =========================

print(df.loc[0])
# Selects row with index 0

print(df.loc[0, "Pulse"])
# Gets Pulse value from row 0

print(df.iloc[0])
# Selects first row by position

print(df.iloc[0, 2])
# Gets value from first row, third column


# =========================
# 4. FILTERING
# =========================

print(df[df["Pulse"] > 120])
# Shows workouts where Pulse is above 120

print(df[df["Calories"] > 400])
# Shows workouts burning more than 400 calories

print(df[df["Duration"] == 60])
# Shows workouts lasting exactly 60 minutes

print(df[(df["Pulse"] > 100) & (df["Calories"] > 300)])
# Pulse > 100 AND Calories > 300


# =========================
# 5. STATISTICS
# =========================

print(df["Pulse"].mean())
# Average Pulse

print(df["Pulse"].median())
# Middle Pulse value

print(df["Pulse"].min())
# Lowest Pulse

print(df["Pulse"].max())
# Highest Pulse

print(df["Calories"].mean())
# Average Calories

print(df["Calories"].max())
# Highest Calories


# =========================
# 6. MISSING VALUES
# =========================

print(df.isnull().sum())
# Counts missing values in every column

print(df["Calories"].isnull().sum())
# Counts missing Calories

print(df[df["Calories"].isnull()])
# Shows rows where Calories is missing

print(df[df["Date"].isnull()])
# Shows rows where Date is missing


# =========================
# 7. DUPLICATES
# =========================

print(df.duplicated().sum())
# Counts duplicate rows

print(df[df.duplicated()])
# Shows duplicate rows


# =========================
# 8. UNIQUE VALUES
# =========================

print(df["Duration"].unique())
# Shows different Duration values

print(df["Duration"].nunique())
# Counts different Duration values

print(df["Duration"].value_counts())
# Counts how many times each Duration occurs


# =========================
# 9. SORTING
# =========================

print(df.sort_values("Pulse"))
# Sorts by Pulse from low to high

print(df.sort_values("Pulse", ascending=False))
# Sorts Pulse from high to low

print(df.sort_values("Calories", ascending=False))
# Highest Calories first


# =========================
# 10. GROUPBY
# =========================

print(df.groupby("Duration")["Calories"].mean())
# Average Calories for each Duration

print(df.groupby("Duration")["Pulse"].mean())
# Average Pulse for each Duration

print(df.groupby("Duration")["Calories"].max())
# Maximum Calories for each Duration


# =========================
# 11. CREATE NEW COLUMN
# =========================

df["CaloriesPerMinute"] = df["Calories"] / df["Duration"]
# Calculates calories burned per minute

print(df[["Duration", "Calories", "CaloriesPerMinute"]])


# =========================
# 12. FIND THE OUTLIER
# =========================

print(df[df["Duration"] > 100])
# Finds unusually large Duration values

# Your dataset contains a Duration of 450,
# which looks suspicious compared with most values.



