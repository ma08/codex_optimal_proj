from collections import deque
from math import ceil



if __name__ == "__main__":
    n, s = map(int, input().split())
    a = list(map(int, input().split()))

    if s == sum(a):
        print(n)
        exit()

    if s < sum(a):
        print(-1)
        exit()

    a.sort()
    a.reverse()

    t = s // a[0]
    i = 0
    while i < t:
        if s % a[i] == 0:
            print(i + 1)
            exit()
        i += 1

    print(ceil(s / a[0]))
