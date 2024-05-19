using System;
using System.Linq;

public class KMeans
{
    private Random _rand;

    public KMeans(int seed)
    {
        _rand = new Random(seed);
    }

    public double[][] Cluster(double[][] data, int k, int maxIterations = 1000)
    {
        var centroids = InitializeCentroids(data, k);
        var assignments = new int[data.Length];

        for (int iteration = 0; iteration < maxIterations; iteration++)
        {
            var changed = AssignCentroids(data, centroids, assignments);
            if (!changed) break;
            centroids = UpdateCentroids(data, assignments, k);
        }

        return centroids;
    }

    private double[][] InitializeCentroids(double[][] data, int k)
    {
        var indices = Enumerable.Range(0, data.Length).OrderBy(x => _rand.NextDouble()).Take(k).ToArray();
        return indices.Select(i => data[i].ToArray()).ToArray();
    }

    private bool AssignCentroids(double[][] data, double[][] centroids, int[] assignments)
    {
        var changed = false;
        for (int i = 0; i < data.Length; i++)
        {
            var closestCentroidIndex = GetClosestCentroidIndex(data[i], centroids);
            if (assignments[i] != closestCentroidIndex)
            {
                assignments[i] = closestCentroidIndex;
                changed = true;
            }
        }
        return changed;
    }

    private double[][] UpdateCentroids(double[][] data, int[] assignments, int k)
    {
        var centroids = new double[k][];
        for (int i = 0; i < k; i++)
        {
            var pointsInCluster = data.Where((p, j) => assignments[j] == i).ToArray();
            centroids[i] = pointsInCluster.Any() ? pointsInCluster.Aggregate((a, b) => a.Zip(b, (x, y) => x + y).ToArray()).Select(x => x / pointsInCluster.Length).ToArray() : new double[data[0].Length];
        }
        return centroids;
    }

    private int GetClosestCentroidIndex(double[] point, double[][] centroids)
    {
        var minDistance = double.MaxValue;
        var closestCentroidIndex = -1;
        for (int i = 0; i < centroids.Length; i++)
        {
            var distance = EuclideanDistance(point, centroids[i]);
            if (distance < minDistance)
            {
                minDistance = distance;
                closestCentroidIndex = i;
            }
        }
        return closestCentroidIndex;
    }

    private double EuclideanDistance(double[] a, double[] b)
    {
        return Math.Sqrt(a.Zip(b, (x, y) => Math.Pow(x - y, 2)).Sum());
    }
}

class Program
{
    static void Main()
    {
        var kmeans = new KMeans(1);
        var data = new[]
        {
            new[] { 1.0, 2.0 },
            new[] { 1.0, 4.0 },
            new[] { 1.0, 0.0 },
            new[] { 10.0, 2.0 },
            new[] { 10.0, 4.0 },
            new[] { 10.0, 0.0 },
        };
        var centroids = kmeans.Cluster(data, 2);

        foreach (var centroid in centroids)
        {
            Console.WriteLine(string.Join(", ", centroid));
        }
    }
}