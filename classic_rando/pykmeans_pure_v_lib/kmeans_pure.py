def init_centroids(data, n_clusters):
  """Randomly initializes cluster centers."""
  centroids = []
  for _ in range(n_clusters):
    index = random.randint(0, len(data) - 1)
    centroids.append(data[index].copy())  # Ensure separate copy
  return centroids

def closest_centroid(x, centroids):
  """Calculates the closest centroid for a data point using distance squared."""
  min_distance_squared = float('inf')  # Positive infinity
  closest_index = None
  for i, centroid in enumerate(centroids):
    distance_squared = sum((x_i - c_i) ** 2 for x_i, c_i in zip(x, centroid))
    if distance_squared < min_distance_squared:
      min_distance_squared = distance_squared
      closest_index = i
  return closest_index

def update_centroids(data, labels, n_clusters):
  """Recalculates centroids as the mean of points in their cluster."""
  centroids = [[0] * len(data[0]) for _ in range(n_clusters)]  # Initialize
  for i in range(n_clusters):
    cluster_members = [data[j] for j in range(len(data)) if labels[j] == i]
    if cluster_members:
      for dim in range(len(data[0])):
        centroids[i][dim] = sum(point[dim] for point in cluster_members) / len(cluster_members)
  return centroids

def predict(data, centroids):
  """Assigns data points to the closest centroid."""
  labels = []
  for x in data:
    labels.append(closest_centroid(x, centroids))
  return labels

def fit(data, n_clusters, max_iter=300):
  """Iteratively refines centroids and assignments until convergence."""
  centroids = init_centroids(data, n_clusters)
  for _ in range(max_iter):
    old_centroids = centroids.copy()
    labels = predict(data, centroids)
    centroids = update_centroids(data, labels, n_clusters)
    if old_centroids == centroids:  # Check for convergence
      break
  return labels

# Sample Usage 
data = [[1, 2], [1.5, 1.8], [5, 8], [8, 8], [1, 0.6], [9, 11]]
labels = fit(data, 2)
print(labels)