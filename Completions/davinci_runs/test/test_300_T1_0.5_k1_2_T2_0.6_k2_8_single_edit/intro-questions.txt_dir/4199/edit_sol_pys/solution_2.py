

n, k = map(int, input().split())
h = [int(input()) for _ in range(n)]  # リスト内包表記で受け取る
print(sum(1 if i >= k else 0 for i in h))  # リスト内包表記で解答を出力する
