
N, L = map(int, input().split())

apple_flavours = [L + i for i in range(N)]

apple_flavours.remove(max(apple_flavours))

print(sum(apple_flavours))
