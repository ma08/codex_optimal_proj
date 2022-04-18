

# テストケース
# N = 3, L = 5
# apple_flavors = [3, 4, 5]
# sum(apple_flavors) = 12

N, L = map(int, input().split())

apple_flavors = [L + i for i in range(N)]

apple_flavors.remove(max(apple_flavors))

print(sum(apple_flavors))
