

n = int(input())
p = list(map(int, input().split()))
# n = 5
# p = [1,3,5,4,2]

ans = 0
for i in range(1,n-1):
    if p[i-1] > p[i] and p[i] < p[i+1]:
        ans += 1
    elif p[i-1] < p[i] and p[i] > p[i+1]:
        ans += 1

print(ans)
