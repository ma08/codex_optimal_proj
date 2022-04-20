import heapq

N, M = map(int, input().split())  # Input
A = list(map(int, input().split()))  # Input

A.sort()

if N < A[-1]:
    print(-1)
    exit()

h = []

heapq.heappush(h, -A[-1])
heapq.heappush(h, -A[-2])

for i in range(M - 2):
    a = -heapq.heappop(h)

    if a > N:
        print(-1)
        exit()

    heapq.heappush(h, -(a - 1))

a = -heapq.heappop(h)

if a > N:
    print(-1)
    exit()

print(N - (a - 1))
