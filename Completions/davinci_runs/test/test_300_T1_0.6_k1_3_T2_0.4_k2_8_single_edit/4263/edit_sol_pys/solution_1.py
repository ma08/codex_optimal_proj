

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest 094
# Problem A

if __name__ == '__main__':
    A, B, X = list(map(int, input().split()))

    if A <= X <= A + B:
        print('YES')
    else:
        print('NO')
