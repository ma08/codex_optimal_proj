

# N,K = map(int,input().split())
N,K = 3,2

count = 0
for a in range(1,N+1):
    for b in range(1,N+1):
        for c in range(1,N+1):
            if (a+b)%K == 0 and (b+c)%K == 0 and (c+a)%K == 0:
                count += 1

print(count)