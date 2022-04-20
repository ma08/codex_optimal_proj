

N, M = map(int, input().split())
A = list(map(int, input().split()))
if max(A) >= sum(A) / (4 * M): 
    print('Yes')
else:
    print('No')
