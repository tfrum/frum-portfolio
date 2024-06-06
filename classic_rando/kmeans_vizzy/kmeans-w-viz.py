import numpy as np
import matplotlib.pyplot as plt
import random

class KMeans:
    def __init__(self, seed):
        self.rand = random.Random(seed)

    def cluster(self, data, k, max_iterations=1000):
        """
        Generator function that performs K-means clustering on the given data.

        Args:
        data: The input data points.
        k: The number of clusters.
        max_iterations: The maximum number of iterations.

        Yields:
        centroids: The centroids of the clusters.
        assignments: The cluster assignments of the data points.
        """
        centroids = self.initialize_centroids(data, k)
        assignments = [0] * len(data)

        for iteration in range(max_iterations):
            changed = self.assign_centroids(data, centroids, assignments)
            if not changed:
                break
            centroids = self.update_centroids(data, assignments, k)
            yield centroids, assignments

    def initialize_centroids(self, data, k):
        """
        Initializes the centroids by randomly selecting k data points.

        Args:
        data: The input data points.
        k: The number of clusters.

        Returns:
        centroids: The initial centroids.
        """
        indices = self.rand.sample(range(len(data)), k)
        return [data[i] for i in indices]

    def assign_centroids(self, data, centroids, assignments):
        """
        Assigns each data point to the closest centroid.

        Args:
        data: The input data points.
        centroids: The centroids of the clusters.
        assignments: The cluster assignments of the data points.

        Returns:
        changed: Whether any assignments were changed.
        """
        changed = False
        for i, point in enumerate(data):
            closest_centroid_index = self.get_closest_centroid_index(point, centroids)
            if assignments[i] != closest_centroid_index:
                assignments[i] = closest_centroid_index
                changed = True
        return changed

    def update_centroids(self, data, assignments, k):
        """
        Updates the centroids based on the assigned data points.

        Args:
        data: The input data points.
        assignments: The cluster assignments of the data points.
        k: The number of clusters.

        Returns:
        centroids: The updated centroids.
        """
        centroids = []
        for i in range(k):
            points_in_cluster = [point for j, point in enumerate(data) if assignments[j] == i]
            if points_in_cluster:
                centroid = np.mean(points_in_cluster, axis=0)
            else:
                centroid = [0] * len(data[0])
            centroids.append(centroid)
        return centroids

    def get_closest_centroid_index(self, point, centroids):
        """
        Finds the index of the closest centroid to the given point.

        Args:
        point: The input data point.
        centroids: The centroids of the clusters.

        Returns:
        index: The index of the closest centroid.
        """
        min_distance = float('inf')
        closest_centroid_index = -1
        for i, centroid in enumerate(centroids):
            distance = self.euclidean_distance(point, centroid)
            if distance < min_distance:
                min_distance = distance
                closest_centroid_index = i
        return closest_centroid_index

    def euclidean_distance(self, a, b):
        """
        Calculates the Euclidean distance between two points.

        Args:
        a: The first point.
        b: The second point.

        Returns:
        distance: The Euclidean distance between the points.
        """
        return np.linalg.norm(np.array(a) - np.array(b))

def generate_biased_data(num_points):
    np.random.seed(0)
    data = []
    for _ in range(num_points):
        x = np.random.uniform(0, 10)
        y = np.random.uniform(0, 10)
        prob = perlin_noise(x, y)
        if np.random.rand() < prob:
            data.append([x, y])
    return np.array(data)

def perlin_noise(x, y):
    """
    Generates a probability value based on Perlin noise.

    Args:
    x: The x-coordinate.
    y: The y-coordinate.

    Returns:
    prob: The probability value.
    """
    freq = 2
    amp = 0.5
    prob = 0
    for i in range(6):
        prob += amp * np.sin(freq * x + np.sin(freq * y))
        freq *= 2
        amp *= 0.5
    return (prob + 1) / 2

# Generate biased data
data = generate_biased_data(10000)

# Perform K-means clustering
kmeans = KMeans(1)
for centroids, assignments in kmeans.cluster(data, 3):
    plt.scatter(data[:, 0], data[:, 1], c=assignments, alpha=0.1)
    plt.scatter(np.array(centroids)[:, 0], np.array(centroids)[:, 1], c='r', marker='x')
    plt.pause(0.1)
    plt.clf()

plt.show()
