N, K = map(int, input().split())
fruit = list(map(int, input().split()))


fruit.sort() # リストの要素を小さい順に並べ替える
print(sum(fruit[:K])) # 小さい順に並べ替えたリストの上位K個を合計する
