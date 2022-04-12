

n = int(input())  # ユーザーからの整数の入力
a = list(map(int, input().split()))  # ユーザーからの整数のリストの入力

ans = 0
for i in range(n):  # 0からn-1まで繰り返す
    if a[i] != i + 1:  # i + 1 と i番目の要素が等しくない場合
        ans += 1

print(ans)
