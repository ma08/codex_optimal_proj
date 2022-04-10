

# n = int(input())
# l = []
# for i in range(n):
#     l.append(list(map(int, input().split())))
# l.sort()
#
# max_inter = 0
# for i in range(n):
#     if i == 0:
#         r = l[i][1]
#         while i+1 < n and l[i+1][0] <= r:
#             r = max(r, l[i+1][1])
#             i += 1
#         max_inter = max(max_inter, r-l[0][0])
#     elif i == n-1:
#         l_ = l[i][0]
#         while i-1 >= 0 and l[i-1][1] >= l_:
#             l_ = min(l_, l[i-1][0])
#             i -= 1
#         max_inter = max(max_inter, l[-1][1]-l_)
#     else:
#         l_ = l[i][0]
#         r = l[i][1]
#         while i-1 >= 0 and l[i-1][1] >= l_:
#             l_ = min(l_, l[i-1][0])
#             i -= 1
#         while i+1 < n and l[i+1][0] <= r:
#             r = max(r, l[i+1][1])
#             i += 1
#         max_inter = max(max_inter, r-l_)
#
# print(max_inter)


n = int(input())
l = []
for i in range(n):
    l.append(list(map(int, input().split())))
l.sort()

max_inter = 0
for i in range(n):
    if i == 0:
        r = l[i][1]
        while i+1 < n and l[i+1][0] <= r:
            r = max(r, l[i+1][1])
            i += 1
        max_inter = max(max_inter, r-l[0][0])
    elif i == n-1:
        l_ = l[i][0]
        while i-1 >= 0 and l[i-1][1] >= l_:
            l_ = min(l_, l[i-1][0])
            i -= 1
        max_inter = max(max_inter, l[-1][1]-l_)
    else:
        l_ = l[i][0]
        r = l[i][1]
        while i-1 >= 0 and l[i-1][1] >= l_:
            l_ = min(l_, l[i-1][0])
            i -= 1
        while i+1 < n and l[i+1][0] <= r:
            r = max(r, l[i+1][1])
            i += 1
        max_inter = max(max_inter, r-l_)

print(max_inter)