
# n = int(input())
# a = [int(x) for x in input().split()]

# def remove_duplicates(a):
#     b = set()
#     for i in a:
#         b.add(i)
#     return list(b)

# b = remove_duplicates(a)
# print(len(b))
# print(*b)

a = [1, 2, 3]
b = a
b[0] = 5
print(a)
