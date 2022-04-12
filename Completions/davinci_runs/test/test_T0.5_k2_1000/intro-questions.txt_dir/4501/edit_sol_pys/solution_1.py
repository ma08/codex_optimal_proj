
import itertools # itertoolsモジュールのインポート

n, a = map(int, input().split()) # 整数の入力
x = list(map(int, input().split())) # 整数のリストの入力

ans = 0 # 初期化
for i in range(1, n+1):
    for j in itertools.combinations(x, i):
        if sum(j) / i == a:
            ans += 1
print(ans)
