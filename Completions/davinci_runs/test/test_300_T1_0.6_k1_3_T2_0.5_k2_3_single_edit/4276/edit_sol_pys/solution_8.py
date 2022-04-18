

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
#     d = sorted(d.items(), key=lambda x: x[0])
#     print(d[0][0])

N, T = map(int, input().split())
d = {}
for i in range(N):
    c, t = map(int, input().split())
    if t <= T:
        if c in d.keys():
            d[c] = min(d[c], t)
        else:
            d[c] = t
if len(d) == 0:
    print("TLE")
else:
    d = sorted(d.items(), key=lambda x: x[0])
    print(d[0][0])

# Sample Input 1 
# 5 5
# 20 2
# 30 5
# 10 3
# 10 2
# 10 4
# Sample Output 1 
# 10
# Sample Input 2 
# 5 10
# 50 9
# 20 9
# 10 5
# 10 6
# 10 7
# Sample Output 2 
# 10
# Sample Input 3 
# 5 10
# 50 9
# 20 9
# 10 5
# 10 6
# 10 7
# Sample Output 3 
# 10
# Sample Input 4 
# 5 10
# 50 9
# 20 9
# 10 5
# 10 6
# 10 7
# Sample Output 4 
# 10
