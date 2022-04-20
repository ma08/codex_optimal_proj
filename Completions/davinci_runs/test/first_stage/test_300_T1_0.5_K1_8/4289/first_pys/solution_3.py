

n = int(input())
t, a = map(int, input().split())
h = list(map(int, input().split()))
diff = float('inf')
ans = 0
for i in range(n):
    if diff > abs(a - (t - h[i] * 0.006)):
        diff = abs(a - (t - h[i] * 0.006))
        ans = i + 1
print(ans)