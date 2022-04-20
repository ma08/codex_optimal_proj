#!/usr/bin/env python3

import sys

# 引数読み込み(1,2,3番目)
argvs = sys.argv
p = int(argvs[1])
q = int(argvs[2])
r = int(argvs[3])

# 出力(最小値を出力)
print(min(p + q, p + r, q + r))
