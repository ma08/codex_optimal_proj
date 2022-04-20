# -*- coding: utf-8 -*-

from collections import Counter

s = input()
t = input()

s_counter = Counter(s)
t_counter = Counter(t)

if s_counter == t_counter:
    print("Yes")
else:
    print("No")
