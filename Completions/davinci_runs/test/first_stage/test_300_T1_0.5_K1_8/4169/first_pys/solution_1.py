

import heapq

def main():
    n, m = map(int, input().split())
    heap = []
    for i in range(n):
        a, b = map(int, input().split())
        heapq.heappush(heap, (a, b))

    ans = 0
    while m > 0:
        a, b = heapq.heappop(heap)
        if m > b:
            ans += a * b
            m -= b
        else:
            ans += a * m
            break

    print(ans)

if __name__ == "__main__":
    main()