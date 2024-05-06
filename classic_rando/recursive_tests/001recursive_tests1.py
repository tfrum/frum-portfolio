import math

def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0  # Collinear
    elif val > 0:
        return 1  # Clockwise
    else:
        return 2  # Counterclockwise

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def graham_scan(points):
    n = len(points)
    if n < 3:
        raise ValueError("Convex hull not possible")

    # Find the leftmost point
    min_x = min(points, key=lambda x: x[0])
    points.remove(min_x)
    hull = [min_x]

    while points:
        p = hull[-1]
        q = None
        for r in points:
            if q is None or orientation(p, q, r) == 2:
                q = r
        hull.append(q)
        points.remove(q)

    return hull

points = [(0, 3), (1, 1), (2, 2), (4, 4), (0, 0), (1, 2), (3, 1), (3, 3)]
hull = graham_scan(points)
print(hull)