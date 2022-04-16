from collections import deque

import heapq
    a = deque(a)
    b = deque(b)


    print(a)
    print(b)
def read_books(n, m, k, a, b):
    heapq.heapify(a)
    heapq.heapify(b)
    cnt = 0
    while k > 0:
        if a and b and a[0] < b[0]:
            if k - a[0] >= 0:
                k -= a[0]
                heapq.heappop(a)
            else:
                return cnt
        elif b and k - b[0] >= 0:
            k -= b[0]
            heapq.heappop(b)
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
