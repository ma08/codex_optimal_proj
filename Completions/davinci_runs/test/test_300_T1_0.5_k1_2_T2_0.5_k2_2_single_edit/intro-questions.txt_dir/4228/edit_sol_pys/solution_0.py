

N, L = map(int, input().split())

apple_flavors = [L + i for i in range(N)]

apple_flavors.remove(min(apple_flavors))

print(sum(apple_flavors))
