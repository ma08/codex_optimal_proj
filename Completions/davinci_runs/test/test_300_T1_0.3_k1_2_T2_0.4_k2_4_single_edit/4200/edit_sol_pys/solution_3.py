

n, m = map(int, input().split())  # n: 都市の数 m: 道路の数
a = list(map(int, input().split()))  # a: 都市の人口
a.sort(reverse=True)  # 降順にソート

if a[m-1] >= sum(a)/(4*m):  # 道路がm本の場合の最小人口が平均人口の4倍以上
    print("Yes")
else:
    print("No")
