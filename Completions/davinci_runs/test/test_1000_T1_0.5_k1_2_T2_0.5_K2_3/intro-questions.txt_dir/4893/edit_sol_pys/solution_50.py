

def min_distance(n, p, distances, result=0):
	distances = sorted(distances)
	for i in range(n):
		if distances[i] - p*i > result:
			result = distances[i] - p*i
	return result

n, p = map(int, raw_input().split())
distances = map(int, raw_input().split())


print min_distance(n, p, distances)
