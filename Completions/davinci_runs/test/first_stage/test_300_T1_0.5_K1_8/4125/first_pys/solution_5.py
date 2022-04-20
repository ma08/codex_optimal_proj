

"""
-----Sample Input 1-----
3 3
1 7 11

-----Sample Output 1-----
2

-----Sample Input 2-----
5 11
10 12 19 20 21

-----Sample Output 2-----
6

-----Sample Input 3-----
3 5
3 4 6

-----Sample Output 3-----
1

-----Sample Input 4-----
8 7
1 2 4 6 10 13 14 20

-----Sample Output 4-----
2
"""

N, X = map(int, input().split())
x = list(map(int, input().split()))

# 各点からの距離を計算
distance = []
for i in range(0, N):
    distance.append(abs(X-x[i]))

# 各点の距離の最大値を取得
max_distance = max(distance)

# 各点の距離の最大値が距離Dである場合、
# その距離Dを移動できる場合のみ、Dを返す
if max_distance <= X:
    print(max_distance)

# 各点の距離の最大値が距離Dである場合、
# その距離Dを移動できない場合、D-1を返す
else:
    print(X-1)