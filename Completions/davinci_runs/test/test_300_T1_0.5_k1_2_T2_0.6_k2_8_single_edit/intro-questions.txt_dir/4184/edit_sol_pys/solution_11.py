

N, K = map(int, input().split())
a = list(map(int, input().split()))

for i in range(K, N):
    if a[i-K] < a[i]:
        print('Yes')
    else:
        print('No')
