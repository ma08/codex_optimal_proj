
# Solution
# input

n = int(input())
a = list(map(int, input().split()))
# set

s = set()
for i in range(n):
    if a[i] not in s:
        s.add(a[i])
    else:
        s.remove(a[i])

# print
print(n - len(s))
