#!/usr/bin/env python
# -*- coding: utf-8 -*-


N, W, H = map(int, input().split())  # N lines, W width, H height

for _ in range(N):
    match = int(input())  # line length
    if match <= (W**2 + H**2)**0.5:  # Pythagorean theorem
        print("DA") 
    else:
        print("NE")
