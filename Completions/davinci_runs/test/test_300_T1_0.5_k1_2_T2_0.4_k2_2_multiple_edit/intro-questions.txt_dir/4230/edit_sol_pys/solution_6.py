#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
Задача: найти ближайшее число из массива к заданному числу
"""

def main():
    x = int(input())
    n = int(input())
    p = list(map(int, input().split()))

    p.sort()

    if x < p[0]:
        print(p[0] - x)
    elif x > p[n - 1]:
        print(x - p[n - 1])
    else:
        for i in range(1, n):
            if p[i - 1] < x and x < p[i]:
                if abs(p[i - 1] - x) < abs(p[i] - x):
                    print(p[i - 1] - x)
                else:
                    print(p[i] - x)
                break

if __name__ == '__main__':
    main()
