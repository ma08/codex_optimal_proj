# -*- coding: utf-8 -*-
# @Author: chenweizhi
# @Date:   2017-12-04 19:53:35
# @Last Modified by:   chenweizhi
# @Last Modified time: 2017-12-04 19:53:35

import sys

a, b, c = map(int, sys.stdin.readline().split())

if a == b and b == c:
    print("YES")
else:
    print("NO")
