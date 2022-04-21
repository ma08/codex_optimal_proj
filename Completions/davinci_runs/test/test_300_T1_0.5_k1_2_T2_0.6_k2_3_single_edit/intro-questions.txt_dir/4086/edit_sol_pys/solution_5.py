# from sys import stdin, stdout


# n = int(stdin.readline())
# a = [int(x) for x in stdin.readline().split()]
# b = []

# def remove_duplicates(a):
#     b = []
#     for i in range(len(a)):
#         if a[i] in b:
#             continue
#         else:
#             b.append(a[i])
#     return b

# b = remove_duplicates(a)
# stdout.write(str(len(b)) + '\n')
# stdout.write(' '.join(map(str, b)))

# from sys import stdin, stdout

# n = int(stdin.readline())
# a = [int(x) for x in stdin.readline().split()]
# # b = []

# def remove_duplicates(a):
#     b = []
#     for i in range(len(a)):
#         if a[i] in b:
#             continue
#         else:
#             b.append(a[i])
#     return b

# b = remove_duplicates(a)
# stdout.write(str(len(b)) + '\n')
# stdout.write(' '.join(map(str, b)))


n = int(input())
a = [int(x) for x in input().split()]
# b = []

def remove_duplicates(a):
    b = []
    for i in range(len(a)):
        if a[i] in b:
            continue
        else:
            b.append(a[i])
    return b

b = remove_duplicates(a)
# print(len(b))
print(*b)
