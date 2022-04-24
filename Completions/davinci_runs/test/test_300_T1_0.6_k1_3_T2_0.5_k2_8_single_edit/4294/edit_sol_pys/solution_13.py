

N = int(input())
A = list(map(int, input().split()))

ans = 0
tmp = 0
for a in A:
    if a == tmp:
        ans += 1
        tmp = 0
    else:
        tmp = a
print(ans)
