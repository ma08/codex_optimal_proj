
N, L = map(int, input().split())

apple_flavors = [L + i for i in range(N)] # list comprehension

apple_flavors.remove(max(apple_flavors)) # remove max

print(sum(apple_flavors))
