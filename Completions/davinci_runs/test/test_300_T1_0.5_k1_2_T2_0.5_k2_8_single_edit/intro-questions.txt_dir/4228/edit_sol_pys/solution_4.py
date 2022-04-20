
N, L = map(int, input().split())  # N: number of apples, L: first apple's flavor

apple_flavors = [L + i for i in range(N)]

apple_flavors.remove(max(apple_flavors))  # remove the apple with the most sour flavor

print(sum(apple_flavors))
