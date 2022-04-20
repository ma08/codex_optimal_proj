
(D, T, S) = map(int, input().split())

if D / S <= T:  # 割り算はfloatになるので注意
    print('Yes')
else:
    print('No')
