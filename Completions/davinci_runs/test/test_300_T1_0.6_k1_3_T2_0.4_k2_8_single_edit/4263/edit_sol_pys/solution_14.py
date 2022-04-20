

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest 047
# Problem A

if __name__ == '__main__':
    a, b, c = list(map(int, input().split()))

    if a + b == c or a + c == b or b + c == a:
        print('Yes')
    else:
        print('No')
