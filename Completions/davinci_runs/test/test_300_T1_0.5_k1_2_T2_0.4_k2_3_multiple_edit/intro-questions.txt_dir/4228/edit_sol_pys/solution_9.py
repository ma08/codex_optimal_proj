

N, L = map(int, input().split())

apple_flavors = [L + i for i in range(N)]  # リンゴの味を格納するリスト

apple_flavors.remove(min(apple_flavors))  # リンゴの味の中で一番苦い味を削除

print(sum(apple_flavors))  # リンゴの味の合計値を出力
