

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest 086
# Problem A

if __name__ == '__main__':
    a, b = list(map(int, input().split()))

    if (a * b) % 2 == 0:
        print('Even')
    else:
        print('Odd')
