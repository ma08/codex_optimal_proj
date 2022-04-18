

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest 001
# Problem B

if __name__ == '__main__':
    m = int(input())

    if m >= 3500:
        print(int(m * 1.05))
    elif m >= 2500:
        print(int(m * 1.1))
    elif m >= 1500:
        print(int(m * 1.15))
    else:
        print(int(m * 1.2))


