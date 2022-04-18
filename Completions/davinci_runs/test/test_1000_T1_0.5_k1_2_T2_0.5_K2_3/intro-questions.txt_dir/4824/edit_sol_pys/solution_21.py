
C, P = map(int, input().split())  # 購入種類、購入商品数
heights = list(map(int, input().split()))  # 商品の購入数

# 価格
prices = [7, 5, 3, 1, 3, 4, 3, 2, 5, 7]

# 合計金額
total = 0
for i in range(P):
    total += prices[i] * heights[i]

print(total)
