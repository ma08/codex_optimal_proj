

n = int(input())
a = list(map(int, input().split()))

# s = [0]*(n+1)
# for i in range(1, n+1):
#     s[i] = s[i-1] + a[i-1]
#
# d = {}
# for i in range(n+1):
#     if s[i] in d:
#         d[s[i]].append(i)
#     else:
#         d[s[i]] = [i]
#
# ans = 0
# for k in d:
#     if len(d[k]) > 1:
#         ans += len(d[k])-1
#
# print(ans)

s = [0]*(n+1)
for i in range(1, n+1):
    s[i] = s[i-1] + a[i-1]

d = {}
for i in range(n+1):
    if s[i] in d:
        d[s[i]].append(i)
    else:
        d[s[i]] = [i]

ans = 0
for k in d:
    if len(d[k]) > 1:
        ans += len(d[k])-1

print(ans)