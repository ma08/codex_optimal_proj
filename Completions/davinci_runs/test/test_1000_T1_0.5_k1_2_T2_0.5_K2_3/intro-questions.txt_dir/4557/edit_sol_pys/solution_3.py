


# a, b, x = map(int, input().split())
# if a + b >= x and a <= x:
#     print("YES")
# else:
#     print("NO")

# a, b = map(int, input().split())

# n = int(input())
# a = list(map(int, input().split()))
# ans = 0
# for i in range(n):
#     for j in range(i + 1, n):
#         for k in range(j + 1, n):
#             if a[i] == a[j] or a[i] == a[k] or a[j] == a[k]:
#                 continue
#             if a[i] + a[j] > a[k] and a[i] + a[k] > a[j] and a[j] + a[k] > a[i]:
#                 ans += 1
# print(ans)

# n = int(input())
# a = list(map(int, input().split()))
# ans = 0
# for i in range(n):
#     for j in range(i + 1, n):
#         for k in range(j + 1, n):
#             if a[i] == a[j] or a[i] == a[k] or a[j] == a[k]:
#                 continue
#             if a[i] + a[j] > a[k] and a[i] + a[k] > a[j] and a[j] + a[k] > a[i]:
#                 ans += 1
# print(ans)
# print(a * b if a < b else a)
