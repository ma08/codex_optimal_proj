

N, L = map(int, input().split())  # 入力

apple_flavors = [L + i for i in range(N)]  # リスト作成

apple_flavors.remove(max(apple_flavors))

print(sum(apple_flavors))
