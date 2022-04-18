import heapq

a, b, k = map(int, input().split())

h = []
for i in range(a, b + 1):
    heapq.heappush(h, i)

for i in range(k):
    print(heapq.heappop(h))

h.reverse()
for i in range(k - 1):
    print(heapq.heappop(h))
print(h[0])
