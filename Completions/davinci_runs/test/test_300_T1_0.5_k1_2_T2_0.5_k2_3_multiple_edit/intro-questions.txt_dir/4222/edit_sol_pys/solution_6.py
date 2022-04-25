N, K = map(int, input().split())

A = set()
for i in range(K): 
    d = int(input()) 
    A.update(list(map(int, input().split())))

ans = N - len(A)
print(ans)
