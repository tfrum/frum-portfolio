import random
import math

class KMeans:
    def __init__(self, n_clusters, max_iter=300, random_state=0):
        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.random_state = random_state
        self.centroids = None

    def _init_centroids(self, X):
        random.seed(self.random_state)
        self.centroids = random.sample(list(X), self.n_clusters)

    def _closest_centroid(self, x):
        distances = [math.sqrt(sum((x_i - c_i) ** 2 for x_i, c_i in zip(x, centroid)))
                     for centroid in self.centroids]
        return distances.index(min(distances))

    def _update_centroids(self, X, labels):
        for i in range(self.n_clusters):
            new_centroid = [0] * len(X[0])  # Assuming consistent dimensionality
            cluster_members = [X[j] for j in range(len(X)) if labels[j] == i]
            if cluster_members:
                new_centroid = [sum(x) / len(cluster_members) for x in zip(*cluster_members)]
            self.centroids[i] = new_centroid

    def predict(self, X):
        labels = [self._closest_centroid(x) for x in X]
        return labels

    def fit(self, X):
        self._init_centroids(X)

        for _ in range(self.max_iter):
            old_centroids = self.centroids
            labels = self.predict(X)
            self._update_centroids(X, labels)
            if old_centroids == self.centroids:  # Check for convergence
                break

data = [[1, 2], [1.5, 1.8], [5, 8], [8, 8], [1, 0.6], [9, 11]]
kmeans = KMeans(n_clusters=2) 
kmeans.fit(data)
print(kmeans.predict(data))