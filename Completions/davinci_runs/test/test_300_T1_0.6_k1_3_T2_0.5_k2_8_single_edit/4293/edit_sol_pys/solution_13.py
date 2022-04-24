

import sys

# 引数読み込み
argvs = sys.argv
p = int(argvs[1])  # pをint型に変換して代入
q = int(argvs[2])  # qをint型に変換して代入
r = int(argvs[3])  # rをint型に変換して代入

# 出力
print(min(p + q, p + r, q + r))
