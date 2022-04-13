
# a, b = map(int, input().split())
# if a % 3 == 0 or b % 3 == 0 or (a + b) % 3 == 0:
#     print("Possible")
# else: 
#     print("Impossible")


# n = int(input())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# c = list(map(int, input().split()))

# count = 0
# for i in range(n-1):
#     if a[i] == b[i] and b[i] == c[i]:
#         count += 0
#     elif a[i] == b[i] or b[i] == c[i] or c[i] == a[i]:
#         count += 1
#     else:
#         count += 2
# print(count)

# n = int(input())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))

# if a[0] == 0:
#     print(0)
#     exit()

# ans = 0
# for i in range(n):
#     if a[i] <= b[i]:
#         ans += a[i]
#         b[i] -= a[i]
#         a[i] = 0
#     else:
#         ans += b[i]
#         a[i] -= b[i]
#         b[i] = 0

#     if i == n-1:
#         break
    
#     if a[i+1] <= b[i]:
#         ans += a[i+1]
#         b[i] -= a[i+1]
#         a[i+1] = 0
#     else:
#         ans += b[i]
#         a[i+1] -= b[i]
#         b[i] = 0
# print(ans)


n = int(input())
a = list(map(int, input().split()))

ans = 0
for i in range(n-1):
    if a[i] == a[i+1]:
        ans += 1
        a[i+1] = 0
print(ans)


