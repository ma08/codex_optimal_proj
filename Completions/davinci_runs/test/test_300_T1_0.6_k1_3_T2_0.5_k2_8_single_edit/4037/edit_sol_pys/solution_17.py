# https://codeforces.com/contest/1206/submission/59559046


n, r = map(int, input().split())
p = [list(map(int, input().split())) for _ in range(n)]
p.sort(key=lambda x: x[1] / x[0], reverse=True)
for i in range(n):
    r -= p[i][0]
    if r < 0:
        print(i)
        exit()
    r += p[i][1]
print(n)

# def get_max(lst, x):
#     for i in range(len(lst)):
#         if lst[i][0] > x:
#             continue
#         else:
#             return i
#
# n, r = map(int, input().split())
# lst = [list(map(int, input().split())) for _ in range(n)]
# lst.sort(key=lambda x: x[1] / x[0], reverse=True)
#
# ans = 0
# while lst:
#     num = get_max(lst, r)
#     if num is None:
#         break
#     for i in range(num + 1):
#         r -= lst[i][0]
#         r += lst[i][1]
#     lst = lst[num + 1:]
#     ans += 1
# print(ans)
