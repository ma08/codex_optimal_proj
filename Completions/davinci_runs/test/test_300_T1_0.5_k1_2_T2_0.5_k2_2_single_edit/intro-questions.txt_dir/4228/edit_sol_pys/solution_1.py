

N, L = map(int, input().split())

apple_flavors = [L + i for i in range(N)]

apple_flavors.remove(max(apple_flavors)) #最大値のリストを削除

print(sum(apple_flavors))
