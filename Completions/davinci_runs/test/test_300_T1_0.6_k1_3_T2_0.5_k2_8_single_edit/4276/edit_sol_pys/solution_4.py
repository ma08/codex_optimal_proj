

# N, T = map(int, input().split())
# d = {i: 10**10 for i in range(1, N+1)}
# for _ in range(N):
#     i, t = map(int, input().split())
#     d[i] = t
# print(min(d, key=lambda x: d[x]))

N, T = map(int, input().split())
d = {i: 10**10 for i in range(1, N+1)}
for _ in range(N):
    i, t = map(int, input().split())
    d[i] = t
if min(d.values()) > T:
    print("TLE")
else:
    print(min(d, key=lambda x: d[x]))
