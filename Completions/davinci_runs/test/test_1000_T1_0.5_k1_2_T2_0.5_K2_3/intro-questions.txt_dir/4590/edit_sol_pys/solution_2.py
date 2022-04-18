

import heapq


def read_books(n, m, k, a, b):
    heapq.heapify(a)
    heapq.heapify(b)
    cnt = 0
    while n > 0 and m > 0 and k > 0:
        if a and b:
            if a[0] < b[0]:
                n -= heapq.heappop(a)
            else:
                m -= heapq.heappop(b)
        elif a:
            n -= heapq.heappop(a)
        elif b:
            m -= heapq.heappop(b)
        else:
            return cnt, n, m
        cnt += 1
    return cnt, n, m


def main():
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    cnt, n, m = read_books(n, m, k, a, b)
    print(cnt)


if __name__ == '__main__':
    main()
