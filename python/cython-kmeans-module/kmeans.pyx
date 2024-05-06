from libc.stdlib cimport malloc, free, realloc, calloc
from libc.string cimport memset

cdef extern from *:
    """
    #include <stdlib.h>
    #include <string.h>
    #include <math.h>

    typedef struct Point {
        double x, y;
    } Point;

    void update_centroids(Point *points, int n_points, int n_clusters, Point *centroids) {
        double *sum_x = (double *) calloc(n_clusters, sizeof(double));
        double *sum_y = (double *) calloc(n_clusters, sizeof(double));
        int *count = (int *) calloc(n_clusters, sizeof(int));

        for (int i = 0; i < n_points; i++) {
            int cluster_id = i % n_clusters;
            sum_x[cluster_id] += points[i].x;
            sum_y[cluster_id] += points[i].y;
            count[cluster_id]++;
        }

        for (int i = 0; i < n_clusters; i++) {
            if (count[i] > 0) {
                centroids[i].x = sum_x[i] / count[i];
                centroids[i].y = sum_y[i] / count[i];
            }
        }

        free(sum_x);
        free(sum_y);
        free(count);
    }
    """
    ctypedef struct Point:
        double x, y
    void update_centroids(Point *points, int n_points, int n_clusters, Point *centroids)

cdef class KMeans:
    cdef int _n_clusters
    cdef Point *_centroids
    cdef Point *_points
    cdef int _n_points

    def __cinit__(self, int n_clusters):
        self._n_clusters = n_clusters
        self._points = <Point*>calloc(n_clusters, sizeof(Point))  # Use calloc to initialize to zero
        self._centroids = <Point*>calloc(n_clusters, sizeof(Point))
        if not self._points or not self._centroids:
            raise MemoryError("Cannot allocate memory.")
        memset(self._centroids, 0, n_clusters * sizeof(Point))

    def add_point(self, double x, double y):
        self._points = <Point*>realloc(self._points, (self._n_points + 1) * sizeof(Point))
        if not self._points:
            raise MemoryError("Cannot allocate memory.")
        self._points[self._n_points].x = x
        self._points[self._n_points].y = y
        self._n_points += 1

    def compute(self):
        update_centroids(self._points, self._n_points, self._n_clusters, self._centroids)

    def __dealloc__(self):
        if self._points:
            free(self._points)
        if self._centroids:
            free(self._centroids)

    # Exposing properties to Python
    property n_clusters:
        def __get__(self):
            return self._n_clusters

    property centroids:
        def __get__(self):
            result = []
            for i in range(self._n_clusters):
                result.append((self._centroids[i].x, self._centroids[i].y))
            return result
