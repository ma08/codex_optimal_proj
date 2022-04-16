import math

def area_of_triangle(a, b, c):
    """
    Calculates the area of a triangle given the three sides.
    """
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

def distance_from_center(a, b, c, area):
    """
    Calculates the distance from the centroid to any vertex of the triangle.
    """
    return 2 * area / (a + b + c)

def solve(triangles):
    """
    Uses Heron's formula to find the area of each triangle,
    then uses the centroid to find the required distance from the vertex.
    """
    max_dist = 0
    for a, b, c in triangles: # Find the largest distance
        area = area_of_triangle(a, b, c)
        dist = distance_from_center(a, b, c, area)
        max_dist = max(max_dist, dist)
    return max_dist

def main():
    """
    Reads the number of triangles, then reads each triangle's side lengths,
    then prints the required distance.
    """
    n = int(input())
    triangles = []
    for _ in range(n):
        a, b, c = map(int, input().split())
        triangles.append((a, b, c))
    result = solve(triangles)
    print(result)

if __name__ == "__main__":
    main()
