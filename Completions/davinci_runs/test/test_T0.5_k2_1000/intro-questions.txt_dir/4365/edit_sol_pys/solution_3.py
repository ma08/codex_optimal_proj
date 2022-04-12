

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest 085
# Problem B

if __name__ == '__main__':
    n = int(input())
    d = [int(input()) for _ in range(n)]
    result = 0

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                result += (d[i] + d[j] + d[k])

    print(result)
