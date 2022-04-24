

import sys, os

# 引数読み込み(第1引数: ファイルパス)
argvs = sys.argv[1]

# 出力
print(min(p + q, p + r, q + r))
