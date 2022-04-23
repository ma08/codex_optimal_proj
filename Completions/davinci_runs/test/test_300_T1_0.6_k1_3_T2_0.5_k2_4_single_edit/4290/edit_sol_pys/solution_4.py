

n, m = map(int, input().split())

# 偶数を2個選び、奇数を1個選ぶ組み合わせの通り数

print((n*(n-1)//2) + n*m)
