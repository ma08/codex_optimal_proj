

n = int(input())
a = list(map(int, input().split()))

# a.sort()

# i = 0
# j = n - 1
# ans = 0
# while i < j:
#     if a[i] == a[j]:
#         i += 1
#         j -= 1
#     elif a[i] < a[j]:
#         a[i] += 1
#         ans += 1
#     else:
#         a[j] += 1
#         ans += 1

# print(ans)

# or

d = {}
for i in range(1, 101):
    d[i] = 0

for i in a:
    d[i] += 1

ans = 0
for i in range(1, 101):
    ans += d[i] // 2

print(ans)