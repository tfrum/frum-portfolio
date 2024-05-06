from sklearn.cluster import KMeans

# Sample usage (same data)
kmeans_sklearn = KMeans(n_clusters=2)
kmeans_sklearn.fit(data)
print(kmeans_sklearn.predict(data))