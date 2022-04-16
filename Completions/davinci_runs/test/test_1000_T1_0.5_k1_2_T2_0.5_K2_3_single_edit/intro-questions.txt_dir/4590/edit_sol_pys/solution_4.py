import sys

import heapq
input = sys.stdin.readline



def read_books(n, m, k, a, b):
    a = [x * -1 for x in a]
    b = [x * -1 for x in b]
    heapq.heapify(a), heapq.heapify(b)
    cnt = 0
    while k > 0:
        if a and b and a[0] < b[0]:
            if k >= 0:
                k -= heapq.heappop(a)
        elif a and b and a[0] >= b[0]:
            k -= heapq.heappop(b)
        elif a:
            k -= heapq.heappop(a)
        elif b:
            if k >= 0:
                k -= heapq.heappop(b)
        else:
            return cnt
        cnt += 1
    return cnt


def main():
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(read_books(n, m, k, a, b) - 1)


if __name__ == '__main__':
    main()
