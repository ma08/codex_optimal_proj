

n,k = map(int,input().split())

if n%2==0:
    print('YES')
    for i in range(n//2):
        print(i+1,k-i)
        print(k-i,i+1)
else:
    print('NO')