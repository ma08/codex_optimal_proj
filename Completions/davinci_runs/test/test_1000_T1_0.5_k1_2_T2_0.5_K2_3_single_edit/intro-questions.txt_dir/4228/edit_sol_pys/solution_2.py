

N, L = map(int, input().split()) # N: number of apples, L: lowest taste

apple_flavors = [L + i for i in range(N)] # all apples' tastes

apple_flavors.remove(max(apple_flavors))

print(sum(apple_flavors))
