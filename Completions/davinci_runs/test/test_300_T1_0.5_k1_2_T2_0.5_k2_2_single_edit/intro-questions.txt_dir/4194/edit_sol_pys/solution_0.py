# import heapq
#
# # Input
# N, M = map(int, input().split())
# A = list(map(int, input().split()))
#
# # Sort A in ascending order
# A.sort()
#
# # If N is smaller than A[-1], Takahashi cannot finish all of the assignments
# if N < A[-1]:
#     print(-1)
#     exit()
#
# # Initialize a heap
# h = []
#
# # Put the last element of A into the heap
# heapq.heappush(h, -A[-1])
#
# # Put the second-last element of A into the heap
# heapq.heappush(h, -A[-2])
#
# # Repeat M-2 times
# for i in range(M-2):
#     # Pop the largest element in the heap
#     a = -heapq.heappop(h)
#
#     # If a is greater than N, Takahashi cannot finish all of the assignments
#     if a > N:
#         print(-1)
#         exit()
#
#     # Push a-1 into the heap
#     heapq.heappush(h, -(a-1))
#
# # Pop the largest element in the heap
# a = -heapq.heappop(h)
#
# # If a is greater than N, Takahashi cannot finish all of the assignments
# if a > N:
#     print(-1)
#     exit()
#
# # Print N-(a-1)
# print(N-(a-1))
import heapq

n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
if n < a[-1]:
    print(-1)
    exit()
h = []
heapq.heappush(h, -a[-1])
heapq.heappush(h, -a[-2])
for i in range(m-2):
    a = -heapq.heappop(h)
    if a > n:
        print(-1)
        exit()
    heapq.heappush(h, -(a-1))

a = -heapq.heappop(h)
if a > n:
    print(-1)
    exit()

print(n-(a-1))
