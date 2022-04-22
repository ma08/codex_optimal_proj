# -*- coding: utf-8 -*-

s = input()
t = input()

print(len(s) + len(t) - 2 * len(set(s) & set(t)))
