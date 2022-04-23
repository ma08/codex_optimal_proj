

n, m = map(int, input().split())

graph = [[] for i in range(n+1)]
visited = [False]*(n+1)

s = set()
for i in range(n):
	if total_sum - a[i] == a[i]:
		s.add(i+1)

print(len(s))
print(*s)
