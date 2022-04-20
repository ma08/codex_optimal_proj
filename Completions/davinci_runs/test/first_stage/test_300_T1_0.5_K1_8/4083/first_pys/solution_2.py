

n, k = map(int, input().split())
a = list(map(int, input().split()))

# min_num = min(a)
# max_num = max(a)
# max_occ = a.count(max_num)
#
# if max_occ >= k:
#     print(0)
# else:
#     print(max(0, max_num - min_num - (k - max_occ)))

# def get_min_max(a):
#     min_num = a[0]
#     max_num = a[0]
#     for i in range(1, len(a)):
#         if a[i] < min_num:
#             min_num = a[i]
#         if a[i] > max_num:
#             max_num = a[i]
#     return min_num, max_num
#
#
# def get_max_occ(a):
#     max_num = a[0]
#     max_occ = 1
#     for i in range(1, len(a)):
#         if a.count(a[i]) > max_occ:
#             max_num = a[i]
#             max_occ = a.count(a[i])
#     return max_num, max_occ
#
#
# def get_num_of_ops(a):
#     min_num, max_num = get_min_max(a)
#     max_num, max_occ = get_max_occ(a)
#     if max_occ >= k:
#         return 0
#     else:
#         return max(0, max_num - min_num - (k - max_occ))
#
#
# print(get_num_of_ops(a))

def get_min_max(a):
    min_num = a[0]
    max_num = a[0]
    for i in range(1, len(a)):
        if a[i] < min_num:
            min_num = a[i]
        if a[i] > max_num:
            max_num = a[i]
    return min_num, max_num


def get_max_occ(a):
    max_num = a[0]
    max_occ = 1
    for i in range(1, len(a)):
        if a.count(a[i]) > max_occ:
            max_num = a[i]
            max_occ = a.count(a[i])
    return max_num, max_occ


def get_num_of_ops(a):
    min_num, max_num = get_min_max(a)
    max_num, max_occ = get_max_occ(a)
    if max_occ >= k:
        return 0
    else:
        return max(0, max_num - min_num - (k - max_occ))


print(get_num_of_ops(a))