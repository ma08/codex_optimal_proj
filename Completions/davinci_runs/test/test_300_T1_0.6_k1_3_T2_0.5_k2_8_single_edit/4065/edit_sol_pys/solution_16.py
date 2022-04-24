

# n = int(input())
# a = list(map(int, input().split()))
#
# q = [a[0]]
# for i in range(1, n):
#     if a[i] <= 2 * q[-1]:
#         q[-1] = a[i]
#     else:
#         q.append(a[i])
#
# print(len(q))

import sys


def input():
    return sys.stdin.readline().strip()


def main():
    n = int(input())
    a = list(map(int, input().split()))

    q = [a[0]]
    for i in range(1, n):
        if a[i] <= 2 * q[-1]:
            q[-1] = a[i]
        else:
            q.append(a[i])

    print(len(q))


if __name__ == '__main__':
    main()
