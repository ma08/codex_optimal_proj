
n = int(input())  # 入力
a = list(map(int, input().split()))  # 入力
a.sort()  # 昇順に並び替え
print(a[n//2] - a[n//2 - 1])  # 中央値の差
