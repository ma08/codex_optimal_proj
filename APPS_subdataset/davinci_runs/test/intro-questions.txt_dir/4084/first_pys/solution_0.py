

# 入力
N, A, B = map(int, input().split())

# 出力
print(N//(A+B)*A+min(N%(A+B), A))