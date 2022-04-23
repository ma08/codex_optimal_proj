
N,K = map(int,input().split())
a = list(map(int,input().split()))


for i in range(K):
    if a[i] > a[i+1]:
        print(i+1)
        exit()

print(N)
