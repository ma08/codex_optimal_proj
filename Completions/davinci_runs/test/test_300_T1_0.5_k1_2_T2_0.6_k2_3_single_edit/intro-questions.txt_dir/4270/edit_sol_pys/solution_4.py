import sys


def main():
    num = int(sys.stdin.readline())
    v = list(map(int, sys.stdin.readline().split()))

    for i in range(num-1):
        v.sort()
        x = v.pop(0)
        y = v.pop(0)
        v.append((x+y)/2)

for i in range(num-1):
    x = heapq.heappop(v)
    y = heapq.heappop(v)
    heapq.heappush(v, (x+y)/2)

print(v[0])
