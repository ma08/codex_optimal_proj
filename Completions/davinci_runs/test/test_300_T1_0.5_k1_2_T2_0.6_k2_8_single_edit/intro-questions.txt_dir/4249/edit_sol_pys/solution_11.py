# def find_min_num(n, m):
#     """
#     :param n:
#     :param m:
#     :return:
#     """
#     days = 0
#     pages = 0
#     for i in range(n):
#         pages += a[i]
#         days += 1
#         if pages >= m:
#             break
#         if i < n - 1:
#             pages -= days - 1
#
#     if pages < m:
#         days = -1
#     return days
#
#
# n, m = map(int, input().split())
# a = list(map(int, input().split()))
#
# a.sort()
#
# print(find_min_num(n, m))


a = [1, 2, 3]
print(a[3:])
