

N, L = map(int, input().split())

apple_flavors = [L + i for i in range(N)] #リスト生成

apple_flavors.remove(max(apple_flavors)) #一番苦いリンゴを除外する

print(sum(apple_flavors))
