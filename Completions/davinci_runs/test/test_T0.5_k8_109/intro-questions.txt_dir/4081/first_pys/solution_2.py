

n = int(input())
a = [int(x) for x in input().split()]

a_sorted = sorted(a)

d = {a_sorted[i]: i for i in range(n)}

ans = []

for i in range(n):
    if d[a[i]] < i:
        ans.append('L')
    else:
        ans.append('R')

print(len(ans))
print(''.join(ans))