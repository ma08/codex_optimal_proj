# coding: utf-8


from collections import Counter
from collections import defaultdict
from collections import deque
import copy
import math
from heapq import heappop, heappush
import itertools
import bisect
import queue
import random
import re

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    cnt = 0
    for i in range(n):
        if a[i] < b[i]:
            dif = b[i] - a[i]
            if a[i+1] >= dif:
                a[i+1] -= dif
                a[i] += dif
            else:
                a[i] += a[i+1]
                a[i+1] = 0
                cnt += dif - a[i]
                a[i] = b[i]

    print(cnt)


if __name__ == '__main__':
    main()
