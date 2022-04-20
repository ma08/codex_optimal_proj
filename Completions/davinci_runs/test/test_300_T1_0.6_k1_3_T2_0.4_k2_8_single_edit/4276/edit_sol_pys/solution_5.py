

# N, T = map(int, input().split())
# d = {}
# for i in range(N):
#     c, t = map(int, input().split())
#     if t <= T:
#         if c in d.keys():
#             d[c] = min(d[c], t)
#         else:
#             d[c] = t
# if len(d) == 0:
#     print("TLE")
# else:
#     print(min(d.keys()))

# N, T = map(int, input().split())
# d = []
# for i in range(N):
#     c, t = map(int, input().split())
#     if t <= T:
#         if c in d:
#             d[d.index(c)] = min(d[d.index(c)], t)
#         else:
#             d.append(c)
# if len(d) == []:
#     print("TLE")
# else:
#     d = sorted(d)
#     print(d[0])

N, T = map(int, input().split())
d = []
for i in range(N):
    c, t = map(int, input().split())
    if t <= T:
        if c in d:
            d[d.index(c)] = min(d[d.index(c)], t)
        else:
            d.append(c)
if len(d) == []:
    print("TLE")
else:
    d = sorted(d)
    print(d[0])
