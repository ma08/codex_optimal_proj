
N, L = map(int, input().split())

apple_flavors = [L + i for i in range(N)]  # 1行でリストの要素を決める

apple_flavors.remove(max(apple_flavors))  # リストの最大値を削除

print(sum(apple_flavors))  # リストの要素の合計
