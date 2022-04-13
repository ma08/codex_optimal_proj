#!/usr/bin/env python3

L = int(input())
max_volume = 0

for a in range(1, L + 1):
    for b in range(1, L + 1):
        for c in range(1, L + 1):
            if a + b + c == L:
                volume = a * b * c
                if volume > max_volume:
                    max_volume = volume

print(max_volume)
