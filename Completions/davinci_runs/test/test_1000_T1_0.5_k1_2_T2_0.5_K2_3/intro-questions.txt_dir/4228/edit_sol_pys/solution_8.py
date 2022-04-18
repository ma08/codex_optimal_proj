

N, L = map(int, input().split()) # N, Lをスペース区切りで入力し、int型に変換してリスト化

apple_flavors = [L + i for i in range(N)] #リスト内包表記

apple_flavors.remove(max(apple_flavors))

print(sum(apple_flavors))
