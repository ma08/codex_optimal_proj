import sys, heapq

def main():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().rstrip().split()))
    a = list(map(lambda x: x * (-1), a))
    heapq.heapify(a)
    for _ in range(n):
        print(heapq.heappop(a) * (-1))

if __name__ == '__main__':
    main()
