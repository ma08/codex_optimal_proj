def min_distance(n, p, distances, result):
    distances = sorted(distances)
    for i in range(1, n):
        if distances[i] - distances[i-1] > result + p * i:
            result = distances[i] - p * i
    return result
 
n, p = map(int, input().split())
distances = map(int, input().split())
result = distances[0]
print(min_distance(n, p, distances, result))
