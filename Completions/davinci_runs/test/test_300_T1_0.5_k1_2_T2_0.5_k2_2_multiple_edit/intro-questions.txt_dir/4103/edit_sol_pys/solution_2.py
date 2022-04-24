#!/usr/bin/env python3

n, b, a = map(int, input().split())
s = list(map(int, input().split()))

max_segment = 0
current_battery = b
current_accumulate = a
for i in range(n):
    if current_accumulate >= 1:
        current_accumulate -= 1
    else:
        current_battery -= 1
    if s[i] == 1:
        if current_battery < b:
            current_battery += 1
        else:
            current_accumulate += 1
    max_segment += 1
    if current_battery == 0 and current_accumulate == 0:
        break

print(max_segment)
