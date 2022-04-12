# 整数の入力(2つ)

n, m = map(int, input().split())

# リストの入力
roads = []
for i in range(m):
    a, b = map(int, input().split())
    roads.append([a, b])

# 出力(リスト)
for i in range(1, n+1):
    count = 0
    for road in roads:
        if i in road:
            count += 1
    print(count)
