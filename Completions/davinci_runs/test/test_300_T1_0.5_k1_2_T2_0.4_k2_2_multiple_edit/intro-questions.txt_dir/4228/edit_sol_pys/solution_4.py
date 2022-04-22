

N, L = map(int, input().split())

apple_flavours = [L + i for i in range(N)] # リスト内包表記を使う

apple_flavours.remove(max(apple_flavours))

print(sum(apple_flavours))
