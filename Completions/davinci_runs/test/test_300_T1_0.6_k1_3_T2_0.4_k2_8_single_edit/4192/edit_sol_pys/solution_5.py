
(D, T, S) = map(int, input().split())

if D / (T - S) <= T:
    print('Yes')
else:
    print('No')
