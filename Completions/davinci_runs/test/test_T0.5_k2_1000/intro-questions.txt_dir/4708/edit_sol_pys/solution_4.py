#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
X = int(sys.stdin.readline())
Y = int(sys.stdin.readline())

if N <= K:
    print(N * X)  # N回買う
elif N > K:
    print(K * X + (N - K) * Y)  # K回買って、残りをY円で買う
