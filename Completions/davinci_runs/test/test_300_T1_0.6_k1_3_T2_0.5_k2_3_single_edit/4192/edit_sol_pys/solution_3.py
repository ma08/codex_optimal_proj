
(D, T, S) = map(int, input().split())

if D / S <= T:  # 単純に距離を速さで割るだけ
    print('Yes')
else:
    print('No')
