

# SOLUTION 1

n = int(input())
x = list(map(int,input().split()))
x.sort()
ans = 0
for i in range(1,n):
    ans += abs(x[i]-x[i-1])-1

# SOLUTION 2

n = int(input())
x = list(map(int,input().split()))
x.sort()
ans = 0
for i in range(1,n):
    ans += abs(x[i]-x[i-1])-1
print(ans)
print(ans)
