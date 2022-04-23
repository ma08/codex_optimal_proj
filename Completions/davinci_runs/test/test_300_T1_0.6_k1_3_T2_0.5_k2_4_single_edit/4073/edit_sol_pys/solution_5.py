#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Read input
n = int(input())
a = list(map(int, input().split()))

# Compute and print answer
print(sum(a) - n)
