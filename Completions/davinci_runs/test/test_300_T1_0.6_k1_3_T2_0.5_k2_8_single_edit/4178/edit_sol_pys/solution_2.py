
n = int(input())
heights = list(map(int, input().split()))  # 1行目を数値に変換してリストに格納

for i in range(1, n):
    if heights[i] < heights[i - 1]:
        heights[i] = heights[i - 1]

print('Yes')
