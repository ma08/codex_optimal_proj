

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest 086
# Problem A

if __name__ == '__main__':
    a, b = list(map(int, input().split()))
    print('Odd' if (a * b) % 2 == 1 else 'Even')
