import sys
input = sys.stdin.readline


N = int(input()) #人数
A = [int(x) for x in input().split()] #第i人が参加するグループ
B = [int(x) for x in input().split()] #グループごとのポイント
C = [int(x) for x in input().split()] #グループごとのボーナスポイント

points = 0
for i in range(N-1):
    if A[i+1] - A[i] == 1: #隣り合うグループが連続している場合
        points += (B[A[i]-1] + C[A[i]-1]) #ポイントを足す
    else:
        points += B[A[i]-1] #連続していない場合はポイントのみ
points += B[A[N-1]-1] #最後のグループのポイントを足す
print(points)
