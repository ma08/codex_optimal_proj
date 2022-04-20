
import heapq

# Input the number of assignments and the number of days
M, N = map(int, input().split())

# Input the number of assignments on each day
A = list(map(int, input().split()))[::-1]

# Initialize a heap
h = A

# Repeat N times
for i in range(N):
    # Pop the largest element in the heap
    a = heapq.heappop(h)

    # If a is greater than N, Takahashi cannot finish all of the assignments
    if a > M:
        print(-1)
        exit()

    heapq.heappush(h, a-1)

# Print the number of assignments that Takahashi can finish
print(M)
