

# Solution

n = int(input())
a = list(map(int, input().split()))

s = set()
for i in range(n):
    if a[i] not in s:
        s.add(a[i])
    else:
        s.remove(a[i])

print(n-len(s))
