
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/5/7 20:20
# @Author  : 一叶知秋
# @File    : file
# @Software: PyCharm

H, n = map(int, input().split())
d = list(map(int, input().split()))

for i in range(n):
    H += d[i]
    if H <= 0:
        print(i + 1)
        break
else:
    print(-1)
