from collections import defaultdict

n = int(input())
trip = defaultdict(list)

for _ in range(n):
    c, y = input().split()
    trip[c].append(int(y))

q = int(input())

for _ in range(q):
    c, k = input().split()
    print(trip[c][int(k)-1])
