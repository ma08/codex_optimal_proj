# 文字列を入力
S, T = input().split()
A, B = map(int, input().split())
U = input()
if S == U:
    print(A-1, B)
else:
    print(A, B-1)
