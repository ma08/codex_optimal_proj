# -*- coding: utf-8 -*-


s = raw_input()
t = raw_input()

sticky = []

for i in range(len(s)):
    if s[i] != t[i]:
        sticky.append(s[i])

print("".join(sticky))
