

def min_distance(n, p, distances, i=0):
    distances = sorted(distances)
    result = distances[0]
    for i in range(1, n-1):
        if distances[i] - distances[i-1] > result + p*(i-1):
            result = distances[i] - p*(i-1)
    return result

n, p = map(int, raw_input().split())
distances = map(int, raw_input().split())
print min_distance(n, p, distances)
