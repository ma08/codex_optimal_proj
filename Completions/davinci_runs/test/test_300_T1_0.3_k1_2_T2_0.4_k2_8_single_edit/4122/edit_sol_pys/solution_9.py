# -*- coding: utf-8 -*-


# AtCoder Beginner Contest

if __name__ == '__main__':
    H, n = map(int, input().split())
    d = list(map(int, input().split()))

    for i in range(n):
        H += d[i]
        if H <= 0:
            print(i + 1)
            break
    else:
        print(-1)
