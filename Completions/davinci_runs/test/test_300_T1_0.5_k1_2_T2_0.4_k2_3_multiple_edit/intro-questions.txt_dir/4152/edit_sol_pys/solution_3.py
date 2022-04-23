
# Solution

# n = int(input())
# a = list(map(int, input().split()))

# s = set()
# for i in range(n):
#     if a[i] not in s:
#         s.add(a[i])
#     else:
#         s.remove(a[i])

# print(n-len(s))

# Solution

n = int(input())
a = list(map(int, input().split()))
a.sort()
for i in range(n-1):
    if a[i] == a[i+1]:
        print(a[i])
        break
