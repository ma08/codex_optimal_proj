
n = int(input()) # 入力された数値をint型にしてnに代入
x = list(map(int, input().split())) # スペース区切りで数値を入力し、int型にしてリストに代入

# x = [1, 2, 3]
# n = 3

x.sort() # リストをソート

min_cost = float('inf') # 無限大の定数
for i in range(n): # リストの要素数分ループ
    cost = 0 # 絶対値の合計
    for j in range(n): # リストの要素数分ループ
        cost += abs(x[j] - x[i]) # リストの各要素の差の絶対値を合計
    min_cost = min(min_cost, cost) # 今までの最小値と比較

print(min_cost)
