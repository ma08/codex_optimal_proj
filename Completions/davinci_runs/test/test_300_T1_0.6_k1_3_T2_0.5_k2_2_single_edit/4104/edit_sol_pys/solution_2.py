#!/usr/bin/env python3
s = input().split('-')
for i in range(len(s)):
    s[i] = s[i].split('+')
sum = 0
if len(s) == 1:
    s = s[0]
    s = s.split('+')
    for i in range(len(s)):
        sum += int(s[i])
    print(sum)
    exit(0)
for i in range(len(s)):
    for j in range(len(s[i])):
        sum -= int(s[i][j])
print(sum)
