import heapq


def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    print(a)



def main2():
    n = int(input())
    a = list(map(int, input().split()))
    heapq.heapify(a)
    print(a)


if __name__ == '__main__':
    main()
