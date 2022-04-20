

import sys

def main():
    n, a, b, c = map(int, sys.stdin.readline().split())
    ls = [int(sys.stdin.readline()) for i in range(n)]
    ls.sort(reverse=True)
    cost = 0
    if ls[0] >= a:
        ls[0] -= a
        cost += a
    else:
        cost += ls[0]
        ls[0] = 0
    if ls[1] >= b:
        ls[1] -= b
        cost += b
    else:
        cost += ls[1]
        ls[1] = 0
    if ls[2] >= c:
        ls[2] -= c
        cost += c
    else:
        cost += ls[2]
        ls[2] = 0
    ls.sort()
    if ls[1] + ls[2] >= a:
        cost += a
    else:
        cost += ls[1] + ls[2]
    if ls[1] + ls[2] >= b:
        cost += b
    else:
        cost += ls[1] + ls[2]
    if ls[0] + ls[1] >= c:
        cost += c
    else:
        cost += ls[0] + ls[1]
    print(cost)


if __name__ == '__main__':
    main()