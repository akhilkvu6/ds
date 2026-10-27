# Exercise 9: Linear Regression

# Aim: Program to implement Linear Regression Algorithm using any standard dataset available in the public domain.

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

# 1. Load the diabetes dataset
diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True)

# 2. Use only one feature (BMI is feature index 2)
diabetes_X = diabetes_X[:, np.newaxis, 2]

# 3. Split the features and targets into training and testing sets (last 20 samples for testing)
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]

diabetes_y_train = diabetes_y[:-20]
diabetes_y_test = diabetes_y[-20:]

# 4. Create and train linear regression model
regr = linear_model.LinearRegression()
regr.fit(diabetes_X_train, diabetes_y_train)

# 5. Make predictions using the test set
diabetes_y_pred = regr.predict(diabetes_X_test)

# 6. Print evaluation metrics
print("Coefficients: ", regr.coef_)
print("Intercept: ", regr.intercept_)
print("Mean squared error: %.2f" % mean_squared_error(diabetes_y_test, diabetes_y_pred))
print("R^2 score: %.2f" % r2_score(diabetes_y_test, diabetes_y_pred))

# 7. Plot test data points and the fitted regression line
plt.scatter(diabetes_X_test, diabetes_y_test, color="black")

sorted_idx = np.argsort(diabetes_X_test[:, 0])
plt.plot(diabetes_X_test[sorted_idx], diabetes_y_pred[sorted_idx], color="blue", linewidth=3)

plt.xlabel("BMI")
plt.ylabel("Diabetes progression")
plt.title("Linear Regression: BMI vs Diabetes Progression")
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.show()
