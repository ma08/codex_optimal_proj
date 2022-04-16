#!/usr/bin/env python3


def median(s, t, k):
    if k == 0:
        return ""
    if s[0] == t[0]:
        return s[0] + median(s[1:], t[1:], k - 1)
    if len(s) == 1:
        return t[0] + median(s[1:], t[1:], k - 1)
    if len(t) == 1:
        return s[0] + median(s[1:], t[1:], k - 1)
    if k == 1:
        return min(s[0], t[0])
    if s[0] < t[0]:
        return s[0] + median(s[1:], t, k - 1)
    return t[0] + median(s, t[1:], k - 1)

k = int(input())
s = input()
t = input()

print(median(s, t, k))
