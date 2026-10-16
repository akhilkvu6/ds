# Exercise 3: Programs using Matplotlib

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# Question 1: Draw a line from position (1,3) and (2,10)
# then to (6,12) and finally to (18,20).
# Mark each point with green color and set line colour to red
# and line style to dotted.

x = np.array([1, 2, 6, 18])
y = np.array([3, 10, 12, 20])

plt.plot(
    x, y,
    color="red",
    linestyle=":",
    marker=".",
    markersize=10,
    markerfacecolor="green",
    markeredgecolor="green"
)

plt.show()


# Question 2: Draw a plot for the following data:
# Temperature in degree and Sales.

x = np.array([12, 14, 16, 18, 20, 22, 24])
y = np.array([100, 200, 250, 400, 300, 450, 500])

plt.xlabel("Temperature")
plt.ylabel("Sales")

plt.plot(x, y, color="green", marker="*")

plt.show()


# Question 3: Draw a line using given axis values
# taken from a text file.

file = open("exercise3.3.txt")

x = np.array(list(map(int, file.readline().strip().split(","))))
y = np.array(list(map(int, file.readline().strip().split(","))))

file.close()

plt.title("Temperature Information")
plt.xlabel("Day")
plt.ylabel("Temperature")

plt.plot(x, y, marker="*")

plt.show()


# Question 4: Plot two or more lines on same plot
# with suitable legends.

x = np.array([1, 2, 3, 4, 5])

y1 = np.array([30, 32, 31, 32, 33])
y2 = np.array([27, 26, 29, 28, 29])

plt.plot(
    x, y1,
    color="red",
    marker=".",
    label="Highest Temperature"
)

plt.plot(
    x, y2,
    color="blue",
    marker=".",
    label="Lowest Temperature"
)

plt.xlabel("Day")
plt.title("Temperature Difference")
plt.legend()

plt.show()


# Question 5: Create multiple plots.

x = np.array([1, 2, 3, 4, 5])

y1 = np.array([30, 32, 31, 32, 33])
y2 = np.array([27, 26, 29, 28, 29])

plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)

plt.plot(x, y1, color="red", marker=".")

plt.xlabel("Day")
plt.ylabel("Temperature (°C)")
plt.title("Highs")


plt.subplot(1, 2, 2)

plt.plot(x, y2, color="blue", marker=".")

plt.xlabel("Day")
plt.ylabel("Temperature (°C)")
plt.title("Lows")

plt.suptitle("Temperature Difference Over 5 Days")

plt.show()


# Question 6: Programming language and popularity.
# i. Bar chart
# ii. Horizontal bar chart
# iii. Bar chart with different colors.

languages = ["Java", "Python", "PHP", "JavaScript", "C#", "C++"]
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]


# i. Bar chart

plt.bar(languages, popularity)

plt.xlabel("Programming Languages")
plt.ylabel("Popularity")

plt.show()


# ii. Horizontal bar chart

plt.barh(languages, popularity, color="red")

plt.xlabel("Popularity")
plt.ylabel("Programming Languages")
plt.title("Programming Languages Popularity")

plt.show()


# iii. Different colors for each bar

colors = [
    "red",
    "green",
    "blue",
    "orange",
    "purple",
    "yellow"
]

plt.bar(languages, popularity, color=colors)

plt.xlabel("Programming Languages")
plt.ylabel("Popularity")

plt.show()


# Question 7: Create bar plots of scores by group and gender.
# Use multiple x values on the same chart for men and women.

x = np.arange(1, 6) * 3

men = np.array([22, 30, 35, 35, 26])
women = np.array([25, 22, 30, 35, 29])

width = 0.4

plt.bar(
    x - width,
    men,
    width=width,
    label="Men"
)

plt.bar(
    x + width,
    women,
    width=width,
    label="Women"
)

plt.xlabel("Group")
plt.ylabel("Score")
plt.title("Scores by Group and Gender")
plt.legend()

plt.show()


# Question 8: Create a pie chart on the popularity
# of programming languages.

languages = [
    "Java",
    "Python",
    "PHP",
    "JavaScript",
    "C#",
    "C++"
]

popularity = [30, 40, 10, 10, 5, 5]

plt.pie(
    popularity,
    labels=languages,
    autopct="%1.1f%%"
)

plt.title("Programming Languages Popularity")

plt.show()


# Question 9: Create a pie chart of gold medal achievements
# of five most successful countries in 2016 Summer Olympics.
# Read the data from a CSV file.

df = pd.read_csv("medal.csv")

countries = df["Country"].to_numpy()
medals = df["Gold_Medal"].to_numpy()

plt.pie(
    medals,
    labels=countries,
    autopct="%1.1f%%"
)

plt.title("Gold Medals - 2016 Summer Olympics")

plt.show()


# Question 10: Draw a scatter plot comparing
# Mathematics and Science marks of 10 students.

math_marks = np.array([
    88, 92, 80, 89, 100,
    80, 60, 100, 80, 34
])

science_marks = np.array([
    35, 79, 79, 48, 100,
    88, 32, 45, 20, 30
])

students = np.arange(1, 11)

plt.scatter(
    students,
    math_marks,
    color="red",
    label="Mathematics"
)

plt.scatter(
    students,
    science_marks,
    color="green",
    label="Science"
)

plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Mathematics vs Science Marks")
plt.legend()

plt.show()