

N, L = map(int, input().split())

apple_flavors = [L + i for i in range(N)]  # リスト内包表記

apple_flavors.remove(max(apple_flavors))  # リストの中で最大値を消す

print(sum(apple_flavors))
