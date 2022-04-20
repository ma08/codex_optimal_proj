
t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    if n % k == 0:
        print(int(n/k))
    else:
        print(int(n/k)+1)