
n = int(input())
a = list(map(int, input().split()))

# 辺の長さが小さい順にソートする
a.sort()

# 4本の辺を選ぶのは、それぞれの辺が異なるようにするため
# 先頭から2本の辺と、末尾から2本の辺を選ぶ
# それぞれの辺の長さの積の最大値を求める
print(max(a[0]*a[1], a[-2]*a[-1]))
