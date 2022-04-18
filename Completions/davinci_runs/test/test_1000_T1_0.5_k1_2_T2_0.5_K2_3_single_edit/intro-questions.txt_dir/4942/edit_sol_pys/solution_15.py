
# n = int(input())
# t = list(map(int, input().split()))
#
# t.sort()
#
# max = t[0]
# for i in range(1, n):
#     if max < t[i]:
#         max = t[i]
#     t[i] = max + t[i]
#
# print(t[-1] + 1)
# Solution

n = int(input())
t = list(map(int, input().split()))

t.sort()

max_time = t[0]
for i in range(1, n):
    if max_time < t[i]:
        max_time = t[i]
    t[i] = max_time + t[i]

print(t[-1] + 1)
