
N = int(input())  # 入力受け取り
A = list(map(int, input().split()))  # 入力受け取り
A.sort()  # ソート
print(A[-1] - A[0])  # 最大値と最小値の差を出力
