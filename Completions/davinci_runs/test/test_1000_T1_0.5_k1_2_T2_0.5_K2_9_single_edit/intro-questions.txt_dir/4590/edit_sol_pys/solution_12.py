
import heapq

import heapq


def read_books(n, m, k, a, b):
    heapq.heapify(a)
    heapq.heapify(b)
    cnt = 0
    while k > 0:
        if a and b:
            if a[0] < b[0]:
                k -= heapq.heappop(a)
            else:
                k -= heapq.heappop(b)
        elif a:
            k -= heapq.heappop(a)
        elif b:
            k -= heapq.heappop(b)
        else:
            return cnt
        cnt += 1
    return cnt


def main():
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(read_books(n, m, k, a, b))


if __name__ == '__main__':
    main()
