

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem A

if __name__ == '__main__':
    N = int(input())
    a = list(map(int, input().split()))

    a.sort()
    print(a[N - 1] - a[0])
