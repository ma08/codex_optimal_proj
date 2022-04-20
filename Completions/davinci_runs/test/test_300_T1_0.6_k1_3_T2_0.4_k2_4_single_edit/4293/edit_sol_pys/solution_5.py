
import sys

# 引数を読み込む
argvs = sys.argv
p = int(argvs[1])
q = int(argvs[2])
r = int(argvs[3])

# 出力
print(min(p + q, p + r, q + r))
