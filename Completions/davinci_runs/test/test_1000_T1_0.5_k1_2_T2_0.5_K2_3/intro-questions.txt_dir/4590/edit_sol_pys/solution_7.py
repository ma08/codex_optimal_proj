
import heapq


def read_books(n, m, k, a, b, c):
    heapq.heapify(a)
    heapq.heapify(b)
    c = 0
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
            return c
        c += 1
    return c


def main():
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(read_books(n, m, k, a, b))


if __name__ == '__main__':
    main()
