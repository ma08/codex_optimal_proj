

n, l = map(int, input().split())

apple_flavors = [l + i for i in range(n)]  # リンゴの味を配列に格納

apple_flavors.remove(max(apple_flavors))  # 一番苦いリンゴを削除

print(sum(apple_flavors))  # 味の合計を出力
