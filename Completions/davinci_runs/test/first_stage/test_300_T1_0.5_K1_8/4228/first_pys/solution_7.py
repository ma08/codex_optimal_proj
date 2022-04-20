

n,l = map(int,input().split())

apple = [l+i for i in range(1,n+1)]

print(sum(apple) - min(apple, key=lambda x:abs(x)))