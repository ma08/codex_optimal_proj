
N, L = map(int, input().split())

apple_flavor = [L + i for i in range(N)]

apple_flavor.remove(max(apple_flavor))

print(sum(apple_flavor))
