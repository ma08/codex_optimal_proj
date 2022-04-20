

# n = int(input())
# a = list(map(int, input().split()))
#
#
# def solve(n, a):
#     a_set = set()
#     count = 0
#     max_count = 0
#     for i in range(n):
#         if a[i] in a_set:
#             a_set.remove(a[i])
#             count -= 1
#         else:
#             a_set.add(a[i])
#             count += 1
#
#         if a[i] + 1 in a_set:
#             a_set.remove(a[i] + 1)
#             count -= 1
#         else:
#             a_set.add(a[i] + 1)
#             count += 1
#
#         if a[i] - 1 in a_set:
#             a_set.remove(a[i] - 1)
#             count -= 1
#         else:
#             a_set.add(a[i] - 1)
#             count += 1
#
#         if count > max_count:
#             max_count = count
#     return max_count
#
#
# print(solve(n, a))

# def solve(n, a):
#     a_set = set()
#     count = 0
#     max_count = 0
#     for i in range(n):
#         if a[i] in a_set:
#             a_set.remove(a[i])
#             count -= 1
#         else:
#             a_set.add(a[i])
#             count += 1
#
#         if a[i] + 1 in a_set:
#             a_set.remove(a[i] + 1)
#             count -= 1
#         else:
#             a_set.add(a[i] + 1)
#             count += 1
#
#         if a[i] - 1 in a_set:
#             a_set.remove(a[i] - 1)
#             count -= 1
#         else:
#             a_set.add(a[i] - 1)
#             count += 1
#
#         if count > max_count:
#             max_count = count
#     return max_count
#
#
# n = int(input())
# a = list(map(int, input().split()))
# print(solve(n, a))


def solve(n, a):
    a_set = set()
    count = 0
    max_count = 0
    for i in range(n):
        if a[i] in a_set:
            a_set.remove(a[i])
            count -= 1
        else:
            a_set.add(a[i])
            count += 1

        if a[i] + 1 in a_set:
            a_set.remove(a[i] + 1)
            count -= 1
        else:
            a_set.add(a[i] + 1)
            count += 1

        if a[i] - 1 in a_set:
            a_set.remove(a[i] - 1)
            count -= 1
        else:
            a_set.add(a[i] - 1)
            count += 1

        if count > max_count:
            max_count = count
    return max_count


n = int(input())
a = list(map(int, input().split()))
print(solve(n, a))