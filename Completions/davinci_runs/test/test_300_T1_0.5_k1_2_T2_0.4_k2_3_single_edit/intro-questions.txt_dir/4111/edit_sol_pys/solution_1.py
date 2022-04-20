

n = int(input())
a = list(map(int,input().split()))

# def find_good_candies(n, a):
#     odd, even = 0, 0
#     for i in range(n):
#         if i%2 == 0:
#             odd += a[i]
#         else:
#             even += a[i]

#     ans = 0
#     for i in range(n):
#         if i%2 == 0:
#             if odd - a[i] == even:
#                 ans += 1
#         else:
#             if odd == even - a[i]:
#                 ans += 1

#     return ans

# ans = 0
# for i in range(n):
#     ans += find_good_candies(n, a[:i] + a[i+1:])

# print(ans)

odd, even = 0, 0
for i in range(n):
    if i%2 == 0:
        odd += a[i]
    else:
        even += a[i]

ans = 0
for i in range(n):
    if i%2 == 0:
        if odd - a[i] == even:
            ans += 1
    else:
        if odd == even - a[i]:
            ans += 1

print(ans)
