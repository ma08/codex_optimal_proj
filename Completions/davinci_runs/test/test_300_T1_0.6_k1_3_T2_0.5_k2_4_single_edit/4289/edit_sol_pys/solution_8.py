
n = int(input())
t, a = map(int, input().split())
h = list(map(int, input().split()))

index = 0
diff = 10000

for i in range(n):
    if abs(a - (t - h[i] * 0.006)) < diff:  # 誤差の絶対値が最小のとき
        diff = abs(a - (t - h[i] * 0.006))  # 差分を更新
        index = i + 1

print(index)
