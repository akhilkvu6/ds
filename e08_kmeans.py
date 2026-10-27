# Exercise 8: K-Means Clustering

# Aim: Program to implement K-means Clustering Algorithm using any standard dataset available in the public domain.

from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score, normalized_mutual_info_score

# 1. Load Iris dataset and select first 2 features (Sepal length and Sepal width)
iris = datasets.load_iris()
X = iris.data[:, :2]
y = iris.target

# 2. Initialize and fit KMeans clustering model
kmeans = KMeans(n_clusters=3, random_state=21)
kmeans.fit(X)
labels = kmeans.labels_

# 3. Visualize Actual vs Predicted clusters
plt.subplot(1, 2, 1)
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='prism', edgecolor='k')
plt.title('Actual')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')

plt.subplot(1, 2, 2)
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='jet', edgecolor='k')
plt.title('Predicted')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')

plt.tight_layout()
plt.show()

# 4. Evaluate clustering performance using ARI and NMI
ari = adjusted_rand_score(y, labels)
nmi = normalized_mutual_info_score(y, labels)

print(f"Adjusted Rand Index (ARI): {ari:.3f}")
print(f"Normalized Mutual Information (NMI): {nmi:.3f}")
