

# SOLUTION
n = int(input())
a = list(map(int, input().split()))

inc = [0] * n
dec = [0] * n

inc[0] = 1
dec[-1] = 1

for i in range(1, n):
    inc[i] = inc[i - 1] + 1 if a[i] > a[i - 1] else 1
    dec[-i - 1] = dec[-i] + 1 if a[-i - 1] > a[-i] else 1

mx = 0
for i in range(n):
    mx = max(mx, inc[i], dec[i])
    if i > 0 and i < n - 1 and a[i - 1] < a[i + 1]:
        mx = max(mx, inc[i - 1] + dec[i + 1])

print(mx)