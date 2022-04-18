import bisect


n = int(input())
a = list(map(int, input().split()))
a.sort()
a = a[::-1]
ans = 0
for i in range(n):
    if a[i] > i+1:
        ans = i+1
        break
else:
    ans = n
print(ans)

# n = int(input())
# a = list(map(int, input().split()))
# a.sort()
# a = a[::-1]
# ans = 0
# for i in range(n):
#     if a[i] > i+1:
#         ans = i+1
#         break
# else:
#     ans = n
# print(ans)
