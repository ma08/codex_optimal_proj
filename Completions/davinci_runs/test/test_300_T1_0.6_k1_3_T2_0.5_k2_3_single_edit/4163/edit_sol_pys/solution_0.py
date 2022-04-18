#!/usr/bin/env python
# -*- coding: utf-8 -*-

n = int(input())
doubles = []

for i in range(n):
    dice1, dice2 = map(int, input().split())
    doubles.append(dice1 == dice2)

for i in range(len(doubles) - 2):
    if doubles[i] and doubles[i+1] and doubles[i+2]:
        print("Yes")
        exit()

print("No")
