

# -*- coding: utf-8 -*-
# @Date    : 2018-09-06 15:11:49
# @Author  : raj lath (oorja.halt@gmail.com)
# @Link    : link
# @Version : 1.0.0

import os
from sys import stdin

max_val=int(10e12)
min_val=int(-10e12)

def read_int()     : return int(stdin.readline())
def read_ints()    : return [int(x) for x in stdin.readline().split()]
def read_str()     : return input()
def read_strs()    : return [x for x in stdin.readline().split()]

nb_chips = read_int()
chips    = read_ints()
chips.sort()
mid = chips[nb_chips//2]
ans = 0
for i in chips:
    ans += abs(mid-i)
print(ans)