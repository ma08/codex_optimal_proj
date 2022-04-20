

import sys

# N = int(input())
N = int(sys.stdin.readline())

# 出力変数
ans = 0

# 6のべき乗
six = 36
while six <= N:
    # 9のべき乗
    nine = 81
    while nine <= N:
        # 6のべき乗 + 9のべき乗
        if six + nine == N:
            ans += 1
            break
        # 9のべき乗を増やす
        nine *= 9
    # 6のべき乗を増やす
    six *= 6

# Nが6のべき乗でない場合
if N % 6 != 0:
    ans += 1

# 出力
print(ans)