
n = int(input())
h = list(map(int, input().split()))

ans = 0
for i in h:
    if i > ans:
        ans = i

print(ans)
