N, L = map(int, input().split())

apple_flavors = [L + i for i in range(N)]  # リンゴの味を格納

apple_flavors.remove(max(apple_flavors))  # 最も苦いリンゴを取り除く

print(sum(apple_flavors))  # リンゴの味の合計
