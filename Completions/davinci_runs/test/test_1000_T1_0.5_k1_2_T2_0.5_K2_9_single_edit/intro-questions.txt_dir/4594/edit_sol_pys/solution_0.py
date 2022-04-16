# coding: utf-8

n = int(input())

# d_list = []
# for i in range(n):
#     d_list.append(int(input()))

# d_set = set(d_list)

# print(len(d_set))

print(len(set([int(input()) for i in range(n)])))
