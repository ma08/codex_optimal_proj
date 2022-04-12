
import sys, heapq

n = int(sys.stdin.readline())
v = list(map(int, sys.stdin.readline().split())) # 값을 입력받아서 리스트로 만든다.
heapq.heapify(v) # 최소힙으로 만든다.

for i in range(n-1):
    x = heapq.heappop(v) # 가장 작은 값을 빼낸다.
    y = heapq.heappop(v) # 가장 작은 값을 빼낸다.
    heapq.heappush(v, (x+y)/2) # 평균을 넣는다.

print(v[0]) # 가장 작은 값을 출력한다.
