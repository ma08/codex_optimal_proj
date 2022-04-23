
N, L = map(int, input().split())

apple_flavors = [L + i for i in range(N)]  # list of apple flavors

apple_flavors.remove(max(apple_flavors))  # remove the apple with the worst flavor

print(sum(apple_flavors))
