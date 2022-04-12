

def min_distance(n, p, distances_):
	distances_ = sorted(distances_)
	result = distances_[0]
	for i in range(1, n):
		if distances_[i] - distances_[i-1] > result + p*(i-1):
			result = distances_[i] - p*(i-1)
	return result

n, p = map(int, raw_input().split())
distances_ = map(int, raw_input().split())
print min_distance(n, p, distances_)
