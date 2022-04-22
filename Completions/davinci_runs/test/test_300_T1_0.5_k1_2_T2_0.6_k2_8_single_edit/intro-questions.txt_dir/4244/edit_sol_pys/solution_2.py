N = int(input())
A = list(map(int, input().split()))
 
ans = float('inf')
for i in range(1, 101):
    j = 0
    for a in A:
        j += (a - i) ** 2
    ans = min(ans, j)
print(ans)
