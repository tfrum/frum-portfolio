import kmeans

def main():
    # Create an instance of KMeans with 3 clusters
    km = kmeans.KMeans(n_clusters=3)

    # Adding some points
    km.add_point(1.0, 2.0)
    km.add_point(2.0, 1.0)
    km.add_point(4.0, 2.0)
    km.add_point(5.0, 3.0)
    km.add_point(3.0, 6.0)
    km.add_point(2.0, 3.0)
    km.add_point(5.0, 7.0)
    
    # Compute the centroids
    km.compute()

    print("Clustering complete. Centroids:")
    for i, centroid in enumerate(km.centroids, 1):
        print(f"Centroid {i}: ({centroid[0]}, {centroid[1]})")

if __name__ == "__main__":
    main()
