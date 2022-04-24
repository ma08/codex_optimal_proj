

n, m = map(int, input().split())

# 偶数を2個選び、奇数を1個選ぶ組み合わせの通り数と、その逆
print((n*(n-1)//2) + n*m, (m*(m-1)//2) + n*m)
