

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem C

if __name__ == '__main__':
    a, b, c = list(map(int, input().split()))
    total = a + b + c
    count = 0

    if a == b:
        count += 1
    if b == c:
        count += 1
    if c == a:
        count += 1

    if count == 1:
        print('Yes')
    else:
        print('No')
