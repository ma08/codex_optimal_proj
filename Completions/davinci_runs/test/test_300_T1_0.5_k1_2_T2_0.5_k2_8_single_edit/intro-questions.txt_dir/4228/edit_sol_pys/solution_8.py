

N, L = map(int, input().split())

apple_flavors = [L + i for i in range(N)] # apple_flavors = [L, L+1, L+2, ..., L+N]

apple_flavors.remove(max(apple_flavors))

print(sum(apple_flavors))
