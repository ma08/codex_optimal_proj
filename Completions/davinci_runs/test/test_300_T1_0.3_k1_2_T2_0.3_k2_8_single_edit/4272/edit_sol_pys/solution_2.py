import sys
input = sys.stdin.readline


N = int(input()) # 文字列の長さ
S = input() # 文字列

count = 0

for i in range(N-2):
    if S[i] == 'A' and S[i+1] == 'B' and S[i+2] == 'C':
        count += 1

print(count)
