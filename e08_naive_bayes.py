# Exercise 8: Naive Bayes

# Question 1: Program to implement Naive Bayes Algorithm using Iris dataset and find the accuracy.

from sklearn import datasets
from sklearn import naive_bayes
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

iris = datasets.load_iris()

x, y = iris.data, iris.target

classifier = naive_bayes.GaussianNB()

x_train, x_test, y_train, y_test = train_test_split(
    x, y, train_size=0.8
)

classifier.fit(x_train, y_train)

result = classifier.predict(x_test)

accuracy = accuracy_score(y_test, result) * 100

print(f"Accuracy is {accuracy}")

features = [
    [int(i) for i in input(
        f"Enter {iris.feature_names}"
    ).split()]
]

result = classifier.predict(features)

print(iris["target_names"][result])