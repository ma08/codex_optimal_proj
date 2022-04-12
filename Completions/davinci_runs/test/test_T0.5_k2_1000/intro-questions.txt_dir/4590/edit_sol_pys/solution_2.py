

import heapq


def read_books(n, m, k, a, b):
    heapq.heapify(a)
    heapq.heapify(b)
    cnt = 0
    while n > 0 and m > 0 and k > 0:
        if a and b:
            if a[0] < b[0]:
                n -= 1
            else:
                m -= 1
        elif a:
            n -= 1
        elif b:
            m -= 1
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
