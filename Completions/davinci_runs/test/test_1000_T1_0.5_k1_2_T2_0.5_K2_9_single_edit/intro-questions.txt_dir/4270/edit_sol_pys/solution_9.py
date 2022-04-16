import sys
import heapq

num = int(sys.stdin.readline())  # 입력받은 수
v = list(map(int, sys.stdin.readline().split()))  # 입력받은 수를 정수로 변환
heapq.heapify(v)

for i in range(num-1):
    x = heapq.heappop(v)  # 가장 작은 수를 제거
    y = heapq.heappop(v)
    heapq.heappush(v, (x+y)/2)

print(v[0])
