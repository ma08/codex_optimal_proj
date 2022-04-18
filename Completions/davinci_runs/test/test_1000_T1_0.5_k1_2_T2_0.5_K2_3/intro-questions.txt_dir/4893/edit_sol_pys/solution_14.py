

def min_distance(n, p, distances):
    distances = sorted(distances)
    result = 0
    for i in range(n):
        if distances[i] - p*i > result:
            result = distances[i] - p*i 
    return result

n, p = map(int, raw_input().split())
distances = map(int, raw_input().split())



print min_distance(n, p, distances)
