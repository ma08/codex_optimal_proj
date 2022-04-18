
import heapq


def read_books(n, m, k, a, b):
    heapq.heapify(a)  # 小根堆
    heapq.heapify(b)  # 小根堆
    cnt = 0
    while k > 0:
        if a and b:
            if a[0] < b[0]:  # 取最小值
                k -= heapq.heappop(a)
            else:
                k -= heapq.heappop(b)
        elif a:  # 只有a
            k -= heapq.heappop(a)
        elif b:  # 只有b
            k -= heapq.heappop(b)
        else:  # 无法再读
            return cnt
        cnt += 1  # 读完一本书
    return cnt


def main():
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(read_books(n, m, k, a, b))


if __name__ == '__main__':
    main()
