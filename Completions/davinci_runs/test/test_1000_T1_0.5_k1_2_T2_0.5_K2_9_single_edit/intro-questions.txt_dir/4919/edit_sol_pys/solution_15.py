
# n = int(input())

# trips = {}
# for i in range(n):
#     country, year = input().split()
#     if country in trips:
#         trips[country].append(int(year))
#     else:
#         trips[country] = [int(year)]

# q = int(input())
# for i in range(q):
#     country, k = input().split()
#     print(sorted(trips[country])[int(k)-1])


# def find_max_min(lst):
#     lst.sort()
#     return [lst[0], lst[-1]]

# print(find_max_min([1, 2, 3, 4]))
# print(find_max_min([4, 2, 9, 11, 2, 1]))


# def find_max_min(lst):
#     return [min(lst), max(lst)]

# print(find_max_min([1, 2, 3, 4]))
# print(find_max_min([4, 2, 9, 11, 2, 1]))


# def find_max_min(lst):
#     min_val, max_val = lst[0], lst[0]
#     for i in lst:
#         if i < min_val:
#             min_val = i
#         if i > max_val:
#             max_val = i
#     return [min_val, max_val]

# print(find_max_min([1, 2, 3, 4]))
# print(find_max_min([4, 2, 9, 11, 2, 1]))


# def find_max_min(lst):
#     if lst[0] == lst[-1]:
#         return [len(lst)]
#     else:
#         return [lst[0], lst[-1]]

# print(find_max_min([1, 2, 3, 4]))
# print(find_max_min([4, 2, 9, 11, 2, 1]))


# def find_max_min(lst):
#     return [lst[0], lst[-1]] if lst[0] != lst[-1] else [len(lst)]

# print(find_max_min([1, 2, 3, 4]))
# print(find_max_min([4, 2, 9, 11, 2, 1]))


# def find_max_min(lst):
#     return [lst[0], lst[-1]] if lst[0] != lst[-1] else [len(lst)]

# print(find_max_min([1, 2, 3, 4]))
# print(find_max_min([4, 2, 9, 11, 2, 1]))


def find_max_min(lst):
    return [lst[0], lst[-1]] if lst[0] != lst[-1] else [len(lst)]

print(find_max_min([1, 2, 3, 4]))
print(find_max_min([4, 2, 9, 11, 2, 1]))
