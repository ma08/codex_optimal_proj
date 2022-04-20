
n = int(input())
a = list(map(int, input().split()))

l = [None]*n
r = [None]*n

l[0] = 0
for i in range(1, n):
    l[i] = l[i-1]
    if a[i] > a[i-1]:
        l[i] += 1

r[-1] = 0
for i in range(n-2, -1, -1):
    r[i] = r[i+1]
    if a[i] < a[i+1]:
        r[i] += 1

ans = 0
pos = 0
for i in range(n):
    if l[i] + r[i] + 1 > ans:
        ans = l[i] + r[i] + 1
        pos = i

print(ans)
print('L'*(l[pos]+1) + 'R'*r[pos])