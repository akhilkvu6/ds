# Exercise 1: Introduction to NumPy

# Question 1: Write a NumPy program to convert Fahrenheit degree to centigrade degree. Fahrenheit values are stored in a NumPy array.

import numpy as np

fht = np.array([100, 98.4, 91.50, 99.78, 101.5])

degree = np.array([])

for temp in fht:
    degreeval = (temp - 32) * (5 / 9)
    degree = np.append(degree, degreeval)

print("Fahrenheit values", fht)
print("Centigrade values", degree)


# Question 2: Write a NumPy program to create a random array with 1000 elements and compute the average, variance, standard deviation of the array elements.

arr = np.random.rand(1000)


print("Average =", np.mean(arr))
print("Variance =", np.var(arr))
print("Standard deviation =", np.std(arr))


# Question 3: Write a NumPy program to convert angles from degrees to radians for all elements in a given array.

degrees = np.array([32, 40, 180, 360, 45, 93])

radians = np.deg2rad(degrees)

print("Degrees =", degrees)
print("Radian values =", radians)


# Question 4: Write a NumPy program to calculate the difference between neighbouring elements, element-wise of a given array.

arr = np.array([12, 34, 6, 28, 46, 90, 3])

diffs = np.diff(arr)

print("Array =", arr)
print("Difference =", diffs)


# Question 5: Write a NumPy program to sort a given complex array using the real part first, then the imaginary part.

arr = np.array([
    complex(7, 5),
    complex(4, 3),
    complex(12, 2),
    complex(1, 8),
    complex(1, 9)
])

sorted_arr = np.sort(arr)

print("Array before sorting =", arr)
print("After sorting =", sorted_arr)


# Question 6: Write a NumPy program to create a 1D array with random numbers and print the values greater than 4.

arr = np.random.randint(low=-40, high=40, size=10)

print("Array =", arr)
print("Elements greater than 4 =", arr[arr > 4])


# Question 7: Write a NumPy program to create a 1D array with random numbers and search a particular number given by the user.

arr = np.random.randint(low=-10, high=40, size=10)

print("Array =", arr)

num = int(input("Enter a number: "))

res = np.where(arr == num)

if len(res[0]) == 0:
    print("Number is not present in the array")
else:
    print("Number is present in the array")


# Question 8: Write a NumPy program to save a given array to a text file and load it.

arr = np.array([4., 5., 4., 6., 11., 2235., 56.])

np.savetxt("test.txt", arr)

loaded_array = np.loadtxt("test.txt")

print("Loaded array =", loaded_array)


# Question 9: Write a NumPy program to create an array of all the even integers from 30 to 60.

arr = np.arange(30, 61, 2)

print("Array of all the even integers from 30 to 60:")
print(arr)


# Question 10: Write a NumPy program to compute sum of all elements, sum of each column and sum of each row of a given array.

arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("Array =", arr)

print("Sum of all elements =", np.sum(arr))
print("Sum of each column =", np.sum(arr, axis=0))
print("Sum of each row =", np.sum(arr, axis=1))