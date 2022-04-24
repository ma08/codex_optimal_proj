import sys
import heapq

num = int(sys.stdin.readline())
v = list(map(int, sys.stdin.readline().split()))
heapq.heapify(v)  # heapify()는 리스트를 힙 형태로 바꿔줌

for i in range(num-1):
    x = heapq.heappop(v)  # heappop()은 가장 작은 값을 빼줌
    y = heapq.heappop(v)
    heapq.heappush(v, (x+y)/2)  # heappush()는 값을 넣어줌

print(v[0])
