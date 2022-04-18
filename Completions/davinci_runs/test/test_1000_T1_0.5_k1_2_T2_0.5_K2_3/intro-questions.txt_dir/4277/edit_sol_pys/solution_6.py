#!/usr/bin/env python3

import math
import itertools
from collections import Counter
from collections import defaultdict
from collections import deque
import bisect
from heapq import heappush, heappop


def main():
    n, a, b = map(int, input().split())

    print(min(n*a, b))


if __name__ == '__main__':
    main()
