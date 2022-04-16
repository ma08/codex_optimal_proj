
import sys
import heapq

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    l = []
    for i in range(m):
        l.append(a[i] * 2)
        a[i] = a[i] // 2
    heapq.heapify(a)
    for i in range(m):
        now = heapq.heappop(a)
        now += l[i]
        heapq.heappush(a, now)
    print(sum(a))



if __name__ == "__main__":
    main()
