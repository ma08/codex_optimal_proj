

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest 061-A
# Problem A

if __name__ == '__main__':
    a, b, c = list(map(int, input().split()))

    if c >= a and c <= b:
        print('Yes')
    else:
        print('No')
