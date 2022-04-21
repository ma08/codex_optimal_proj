

# n = int(input())
# f = [int(x) for x in input().split()]

# # Find friends who don't know who to give gifts to
# # and friends who don't know who gives them gifts
# no_gift_to = []
# no_gift_from = []
# for i in range(n):
#     if f[i] == 0:
#         no_gift_to.append(i)
#     else:
#         if f[f[i] - 1] == 0:
#             no_gift_from.append(f[i] - 1)

# # Give gifts to friends who don't know who gives them gifts
# for i in range(len(no_gift_to)):
#     f[no_gift_from[i]] = no_gift_to[i] + 1

# # Give gifts to friends who don't know who to give gifts to
# for i in range(len(no_gift_to)):
#     f[no_gift_to[i]] = no_gift_from[i] + 1

# print(" ".join(str(x) for x in f))

# for i in range(len(numbers)):
#     print(numbers[i])

# def find_sum(data, target):
#     for i in range(len(data)):
#         for j in range(i + 1, len(data)):
#             if data[i] + data[j] == target:
#                 return data[i], data[j]
#     return None


# numbers = [1, 2, 3, 4, 5]
# x, y = find_sum(numbers, 7)
# print(x, y)

# def find_sum2(data, target):
#     for i in range(len(data)):
#         for j in range(i + 1, len(data)):
#             if data[i] + data[j] == target:
#                 return data[i], data[j]
#     return None

# numbers = [1, 2, 3, 4, 5]
# x, y = find_sum2(numbers, 7)
# print(x, y)

# def find_sum3(data, target):
#     for i in range(len(data)):
#         for j in range(i + 1, len(data)):
#             if data[i] + data[j] == target:
#                 return data[i], data[j]
#     return None


# numbers = [1, 2, 3, 4, 5]
# x, y = find_sum3(numbers, 7)
# print(x, y)

# def find_sum4(data, target):
#     for i in range(len(data)):
#         for j in range(i + 1, len(data)):
#             if data[i] + data[j] == target:
#                 return data[i], data[j]
#     return None


# numbers = [1, 2, 3, 4, 5]
# x, y = find_sum4(numbers, 7)
# print(x, y)


# def find_sum5(data, target):
#     for i in range(len(data)):
#         for j in range(i + 1, len(data)):
#             if data[i] + data[j] == target:
#                 return data[i], data[j]
#     return None


# numbers = [1, 2, 3, 4, 5]
# x, y = find_sum5(numbers, 7)
# print(x, y)

# def find_sum6(data, target):
#     for i in range(len(data)):
#         for j in range(i + 1, len(data)):
#             if data[i] + data[j] == target:
#                 return data[i], data[j]
#     return None


# numbers = [1, 2, 3, 4, 5]
# x, y = find_sum6(numbers, 7)
# print(x, y)


# def find_sum7(data, target):
#     for i in range(len(data)):
#         for j in range(i + 1, len(data)):
#             if data[i] + data[j] == target:
#                 return data[i], data[j]
#     return None


# numbers = [1, 2, 3, 4, 5]
# x, y = find_sum7(numbers, 7)
# print(x, y)


# def find_sum8(data, target):
#     for i in range(len(data)):
#         for j in range(i + 1, len(data)):
#             if data[i] + data[j] == target:
#                 return data[i], data[j]
#     return None


# numbers = [1, 2, 3, 4, 5]
# x, y = find_sum8(numbers, 7)
# print(x, y)
