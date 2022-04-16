
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
x = []
y = []
for i in range(n):
    for j in range(m):
        x.append(a[i] + b[j])
for i in range(m):
    for j in range(m):
        y.append(b[i] + c[j])
x.sort()
y.sort()
ans = 0
i = 0
j = len(y) - 1
while i < len(x) and j >= 0:
    if x[i] + y[j] == 0:
        a = x[i]
        cnt1 = 1
        cnt2 = 1
        i += 1
        j -= 1
        while i < len(x) and x[i] == a:
            cnt1 += 1
            i += 1
        while j >= 0 and y[j] == -a:
            cnt2 += 1
            j -= 1
        ans += cnt1 * cnt2
    elif x[i] + y[j] > 0:
        j -= 1
    else:
        i += 1
print(ans)
