

# n = int(input())
# d = dict()
# for i in range(n):
#     s = input()
#     k = ''.join(sorted(s))
#     if k in d:
#         d[k] += 1
#     else:
#         d[k] = 1
# ans = 0
# for key in d:
#     ans += d[key] * (d[key] - 1) // 2
# print(ans)

n = int(input())
d = dict()
for i in range(n):
    s = input()
    k = ''.join(sorted(s))
    if k in d:
        d[k] += 1
    else:
        d[k] = 1
ans = 0
for key in d:
    ans += d[key] * (d[key] - 1) // 2
print(ans)