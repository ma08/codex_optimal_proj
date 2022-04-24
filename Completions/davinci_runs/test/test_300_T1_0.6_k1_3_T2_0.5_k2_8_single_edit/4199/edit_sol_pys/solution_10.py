N, K = map(int, input().split())
h = [int(x) for x in input().split()]


print(len([x for x in h if x >= K]))  # リスト内包表記
