#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

def get_input(n, k):
    a = np.array([[int(x) for x in input().split()] for i in range(n)])
    return a

def get_answer(a):
    return np.linalg.det(a)

def main(n, k):
    a = get_input(n, k)
    print(get_answer(a))

if __name__ == '__main__':
    n, k = map(int, input().split())
    main(n, k)
