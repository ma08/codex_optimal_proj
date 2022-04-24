
# coding=utf-8

n, m = map(int, raw_input().split())

if (n + m) % 2 == 0:
    print(2 ** (n + m) - 2 ** ((n + m) / 2))
else:
    print(2 ** (n + m))
