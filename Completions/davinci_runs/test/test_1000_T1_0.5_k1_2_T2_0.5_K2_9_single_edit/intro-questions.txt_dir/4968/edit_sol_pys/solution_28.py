

# import sys

# [N, S, R] = map(int, sys.stdin.readline().split())
# damaged = map(int, sys.stdin.readline().split())
# reserve = map(int, sys.stdin.readline().split())

# def check(reserve, damaged):
#     for i in damaged:
#         if i-1 in reserve or i+1 in reserve:
#             reserve.remove(i-1)
#             reserve.remove(i+1)
#             damaged.remove(i)
#     return len(damaged)

# print check(reserve, damaged)


# def find_closest(x, y, x_list, y_list):
#     min_distance = max(x_list) + max(y_list)
#     for i in range(len(x_list)):
#         for j in range(len(y_list)):
#             distance = abs(x_list[i] - x) + abs(y_list[j] - y)
#             if min_distance > distance:
#                 min_distance = distance
#     return min_distance

# def find_closest(x, y, x_list, y_list):
#     min_distance = max(x_list) + max(y_list)
#     for i in range(len(x_list)):
#         distance = abs(x_list[i] - x) + abs(y_list[i] - y)
#         if min_distance > distance:
#             min_distance = distance
#     return min_distance

# def find_closest(x, y, x_list, y_list):
#     min_distance = max(x_list) + max(y_list)
#     for i in range(len(x_list)):
#         distance = abs(x_list[i] - x) + abs(y_list[i] - y)
#         if min_distance > distance:
#             min_distance = distance
#     return min_distance

# def find_closest(x, y, x_list, y_list):
#     min_distance = max(x_list) + max(y_list)
#     for i in range(len(x_list)):
#         distance = abs(x_list[i] - x) + abs(y_list[i] - y)
#         if min_distance > distance:
#             min_distance = distance
#     return min_distance
