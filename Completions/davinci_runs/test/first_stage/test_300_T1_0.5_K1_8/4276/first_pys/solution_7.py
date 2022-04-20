

# N = int(input())
# T = int(input())
#
# for i in range(N):
#     c, t = map(int, input().split())
#
#     if t <= T:
#         if i == 0:
#             min_cost = c
#         else:
#             min_cost = min(min_cost, c)
#
# if i != 0:
#     print(min_cost)
# else:
#     print("TLE")

N = int(input())
T = int(input())

min_cost = T + 1

for i in range(N):
    c, t = map(int, input().split())

    if t <= T:
        min_cost = min(min_cost, c)

if min_cost <= T:
    print(min_cost)
else:
    print("TLE")