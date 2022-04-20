import sys
input = sys.stdin.readline


N = int(input()) # 入力

if N%4 == 0 or N%7 == 0 or N%11 == 0:
    print("Yes")
else:
    print("No")
