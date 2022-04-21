

n = int(input())
h = list(map(int, input().split()))

ans = 0
for i in range(n):
    if h[i] > 0:
        ans += 1
        for j in range(i+1, n):
            if h[j] > 0:
                h[j] -= 1



n = int(input())
h = list(map(int, input().split()))

ans = 0
for i in range(n):
    if h[i] > 0:
        ans += 1
        for j in range(i+1, n):
            if h[j] > 0:
                h[j] -= 1

print(ans)
print(ans)
