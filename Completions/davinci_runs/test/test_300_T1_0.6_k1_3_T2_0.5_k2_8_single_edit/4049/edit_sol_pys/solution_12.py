

# n = int(input())
# a = list(map(int,input().split()))
# b = list(map(int,input().split()))
#
# min_win = 0
# max_win = 0
#
# for i in range(3):
#     for j in range(3):
#         if a[i] == 0 or b[j] == 0:
#             continue
#         else:
#             if (i - j)%3 == 1:
#                 min_win += min(a[i],b[j])
#             elif (i - j)%3 == 2:
#                 max_win += min(a[i],b[j])
#
# print(min_win,max_win)

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

ans = 0

for i in range(3):
    if a[i] == n or b[i] == n:
        continue
    else:
        if (i - i)%3 == 1:
            ans += min(a[i],b[i])
        elif (i - i)%3 == 2:
            ans += min(a[i],b[i])

print(ans,n-ans)

# a = list(map(int,input().split()))
# b = list(map(int,input().split()))
#
# c = [0,0,0]
#
# for i in range(3):
#     for j in range(3):
#         if a[i] == 0 or b[j] == 0:
#             continue
#         else:
#             if (i - j)%3 == 1:
#                 c[0] += min(a[i],b[j])
#             elif (i - j)%3 == 2:
#                 c[2] += min(a[i],b[j])
#             else:
#                 c[1] += min(a[i],b[j])
#
# print(c[0],c[1],c[2])
