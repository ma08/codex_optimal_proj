

n = int(input())
a = list(map(int, input().split()))
c = [0] * 7
for i in range(n):
    c[a[i]] += 1

if max(c) == 0:
    print('none')
else:
    print(c.index(max(c)))
