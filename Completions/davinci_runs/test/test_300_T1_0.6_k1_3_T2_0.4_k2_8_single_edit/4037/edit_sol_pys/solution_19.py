

# Not my solution, but I understand it and it's so damn clever and fast
# https://codeforces.com/contest/1206/submission/59559046

# n, r = map(int, input().split())
# p = [list(map(int, input().split())) for _ in range(n)]
# p.sort(key=lambda x: x[1] / x[0], reverse=True)
# for i in range(n):
#     r -= p[i][0]
#     if r < 0:
#         print(i)
#         exit()
#     r += p[i][1]
# print(n)

# My solution

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

# It's the same solution as above, but the code is a bit more compact
# https://codeforces.com/contest/1206/submission/59560137

n, r = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
a.sort(key=lambda x: x[1] / x[0], reverse=True)
for i, j in a:
    r -= i
    if r < 0:
        print(i + 1)
        break
    r += j
else:
    print(n)
