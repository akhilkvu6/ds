# Exercise 4: Programs using Pandas

import pandas as pd
import numpy as np

# Question 1: Write a Python program to implement List-to-Series Conversion.

listdata = [1, 4, 6, 3]

series = pd.Series(listdata)

print(series)


# Question 2: Write a Python program to generate the series of dates from 1st May, 2021 to 12th May, 2021.

print(pd.date_range("2021-05-01", "2021-05-12"))


# Question 3: Given a dictionary, convert it into corresponding dataframe and display it.

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [24, 30, 28],
    "City": ["Delhi", "Mumbai", "Bangalore"]
}

df = pd.DataFrame(data)

print("Dictionary to DataFrame:")
print(df)


# Question 4: Given a 2D List, convert it into corresponding dataframe and display it.

listdata = [
    [1, "Alice", 10],
    [2, "Bob", 15],
    [3, "Don", 25]
]

df = pd.DataFrame(listdata, columns=["ID", "Name", "Score"])

print(df)


# Question 5: Given a CSV file, read it into a dataframe and display it.

df = pd.read_csv("medal.csv")

print(df)


# Question 6: Given a dataframe, sort it by multiple columns.

listdata = [
    [1, "Alice", 15],
    [2, "Bob", 15],
    [3, "Don", 45]
]

df = pd.DataFrame(listdata, columns=["ID", "Name", "Score"])

print("Data frame")
print(df)

sorted_df = df.sort_values(
    by=["Score", "Name"],
    ascending=[False, True]
)

print("Sorted Dataframe")
print(sorted_df)


# Question 7: Given a dataframe with custom indexing, convert it to default indexing and display it.

data = [
    ["Alice", 25, "New York"],
    ["Bob", 30, "Paris"],
    ["Charlie", 35, "London"]
]

df = pd.DataFrame(
    data,
    columns=["Name", "Age", "City"],
    index=["p1", "p2", "p3"]
)

print(df)

df = df.reset_index(drop=True)

print(df)


# Question 8: Given a dataframe, select first 2 rows and output them.

data = [
    ["Alice", 25, "New York"],
    ["Bob", 30, "Paris"],
    ["Charlie", 35, "London"]
]

df = pd.DataFrame(
    data,
    columns=["Name", "Age", "City"]
)

print(df.iloc[0:2, :])


# Question 9: Given is a dataframe showing name, occupation, salary of people. Find the average salary per occupation.

data = [
    ["Alice", "Teacher", 25000],
    ["Bob", "Doctor", 55000],
    ["Charlie", "Teacher", 20000],
    ["Dylan", "Doctor", 35000],
    ["Emma", "Engineer", 65000]
]

df = pd.DataFrame(
    data,
    columns=["Name", "Job", "Salary"]
)

print(df)

avg_by_job = df.groupby("Job")["Salary"].mean()

print(avg_by_job)


# Question 10: Given a dataframe with NaN Values, fill the NaN values with 0.

data = {
    "A": [1, 2, np.nan, 4],
    "B": [np.nan, 2, 3, 4]
}

df = pd.DataFrame.from_dict(data, orient="index")

print(df)

df = df.fillna(0)

print(df)


# Question 11: Given is a dataframe showing Company Names and Profits. Convert positive profits to True and the rest to False.

data = {
    "cname": ["A", "B", "C"],
    "profit": [1000, -500, 0]
}

df = pd.DataFrame(data)

df["profit"] = df["profit"] > 0

print("Profit Column Converted to Boolean:")
print(df)


# Question 12: Given are 2 dataframes containing Employee ID, Employee Name, Stipend and Position. Merge them using Employee ID.

data1 = [
    [101, "John", 30000],
    [102, "Amith", 35000],
    [103, "Sona", 20000]
]

df1 = pd.DataFrame(
    data1,
    columns=["ID", "Name", "Stipend"]
)

data2 = [
    [101, "Developer"],
    [102, "Developer"],
    [103, "Tester"]
]

df2 = pd.DataFrame(
    data2,
    columns=["ID", "Position"]
)

df3 = pd.merge(
    df1,
    df2,
    how="inner",
    on="ID"
)

print(df3)