# -*- coding: utf-8 -*-
# @Author: wangchao
# @Time: 19-8-9 下午5:13
import sys
 
N = int(sys.stdin.readline().rstrip())
d = list(map(int, sys.stdin.readline().rstrip().split()))
 
print(N)
print(d)
 
count = 0
for i in range(1, N):
    if sum(d[:i]) == sum(d[i:]):
        count += 1
 
print(count)
