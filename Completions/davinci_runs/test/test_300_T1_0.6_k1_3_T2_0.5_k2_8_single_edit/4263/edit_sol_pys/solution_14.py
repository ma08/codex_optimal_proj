

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem C

if __name__ == '__main__':
    from collections import Counter

    n = int(input())
    a = list(map(int, input().split()))
    result = 0

    for i in range(n):
        if a.count(i) == 1:
            result = a.index(i)
            break

    print(result + 1)
