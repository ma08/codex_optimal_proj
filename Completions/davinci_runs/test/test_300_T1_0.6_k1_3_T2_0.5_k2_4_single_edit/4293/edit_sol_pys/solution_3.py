
import sys

# 引数読み込み
args = sys.argv
p = int(args[1])
q = int(args[2])
r = int(args[3])

# 出力
print(min(p + q, p + r, q + r))
