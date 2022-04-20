

# import sys

# n, m = map(int, sys.stdin.readline().split())

# # stores = []
# # for i in range(n):
# #     stores.append(list(map(int, sys.stdin.readline().split())))

# stores = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

# stores.sort(key=lambda x: x[0])

# cost = 0
# for store in stores:
#     if m <= store[1]:
#         cost += store[0] * m
#         break
#     else:
#         cost += store[0] * store[1]
#         m -= store[1]

# print(cost)


def solution(s):
    if len(s) == 4 or len(s) == 6:
        return s.isdigit()
    return False


print(solution("a234"))
print(solution("1234"))
