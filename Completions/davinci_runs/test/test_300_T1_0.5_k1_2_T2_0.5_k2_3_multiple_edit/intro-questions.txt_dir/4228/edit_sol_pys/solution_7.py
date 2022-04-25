

N, L = map(int, input().split())

apples = [L + i for i in range(N)]  # リンゴの味を配列に格納

apples.remove(max(apples))  # 一番苦いリンゴを削除

print(sum(apples))  # 味の合計を出力
