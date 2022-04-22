
import heapq
N=int(input())
A=list(map(int,input().split()))
A.sort()
A.reverse()
h=[]
for k in range(N):
    heapq.heappush(h,A[k])
for k in range(1,N):
    v=heapq.heappop(h)
    v=v/2
    heapq.heappush(h,v)
print(sum(h))
