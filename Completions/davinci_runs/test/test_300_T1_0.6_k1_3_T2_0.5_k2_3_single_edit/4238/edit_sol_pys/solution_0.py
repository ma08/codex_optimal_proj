

# 入力 N
N = int(input())

# 入力 A
A = list(map(int, input().split()))

# 入力 B
B = list(map(int, input().split()))

# 入力 C
C = list(map(int, input().split()))

# 結果
result = 0
before = -1

# ループ
for i in A:
    result += B[i-1]
    if before + 1 == i:
        result += C[before-1]
    before = i

# 出力
print(result)
