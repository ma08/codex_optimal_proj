import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))  # 入力
B = list(map(int, input().split()))  # 入力
C = list(map(int, input().split()))  # 入力

satisfaction = 0  # 合計値

for i in range(N - 1):
    satisfaction += B[A[i] - 1]  # 料理の味を足す
    if A[i] == A[i + 1] - 1:
        satisfaction += C[A[i] - 1]  # 食べる順番が連続していたら、料理の組み合わせのボーナスを足す
satisfaction += B[A[N - 1] - 1]  # 最後の料理の味を足す
print(satisfaction)
