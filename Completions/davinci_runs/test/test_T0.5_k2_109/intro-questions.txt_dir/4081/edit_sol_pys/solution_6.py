
'''
# SOLUTION 1

n = int(input())
a = list(map(int, input().split()))

l = []
r = []
for i in range(n):
    if i % 2 == 0:
        l.append(a[i])
    else:
        r.append(a[i])

l = sorted(l)
r = sorted(r)

ans = ''
for i in range(n):
    if i % 2 == 0:
        ans += 'L'
    else:
        ans += 'R'

print(n)
print(ans)
'''
# SOLUTION 2
'''
n = int(input())
a = list(map(int, input().split()))

l = []
r = []
for i in range(n):
    if i % 2 == 0:
        l.append(a[i])
    else:
        r.append(a[i])

l.sort()
r.sort()

ans = ''
for i in range(n):
    if i % 2 == 0:
        ans += 'L'
    else:
        ans += 'R'

print(n)
print(ans)
'''
