

n = int(input())  # 入力
heights = list(map(int, input().split()))  # 入力

for i in range(1, n):  # i = 1, 2, ..., n-1
    if heights[i] < heights[i - 1]:  # 前の要素と比較
        heights[i] = heights[i - 1]  # 前の要素と同じにする

print('Yes')  # 出力
