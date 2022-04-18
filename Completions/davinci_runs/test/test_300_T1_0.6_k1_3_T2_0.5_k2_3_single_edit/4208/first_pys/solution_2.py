

# n = int(input())
# l = input()
# r = input()
#
# pairs = []
#
# for i in range(n):
#     if l[i] != '?' and r[i] != '?':
#         if l[i] == r[i]:
#             pairs.append((i+1, i+1))
#             l[i] = '?'
#             r[i] = '?'
#     elif l[i] != '?':
#         for j in range(n):
#             if r[j] == l[i]:
#                 pairs.append((i+1, j+1))
#                 l[i] = '?'
#                 r[j] = '?'
#                 break
#     elif r[i] != '?':
#         for j in range(n):
#             if l[j] == r[i]:
#                 pairs.append((j+1, i+1))
#                 l[j] = '?'
#                 r[i] = '?'
#                 break
#
# print(len(pairs))
# for p in pairs:
#     print(p[0], p[1])

# def check(x, y):
#     if x == '?' or y == '?':
#         return True
#     elif x == y:
#         return True
#     else:
#         return False
#
# n = int(input())
# l = input()
# r = input()
#
# pairs = []
#
# for i in range(n):
#     for j in range(n):
#         if check(l[i], r[j]):
#             pairs.append((i+1, j+1))
#             l[i] = '?'
#             r[j] = '?'
#             break
#
# print(len(pairs))
# for p in pairs:
#     print(p[0], p[1])

import sys

n = int(input())
l = input()
r = input()

pairs = []

for i in range(n):
    for j in range(n):
        if l[i] != '?' and r[j] != '?':
            if l[i] == r[j]:
                pairs.append((i+1, j+1))
                l[i] = '?'
                r[j] = '?'
                break
        elif l[i] == '?':
            pairs.append((i+1, j+1))
            l[i] = '?'
            r[j] = '?'
            break
        elif r[j] == '?':
            pairs.append((i+1, j+1))
            l[i] = '?'
            r[j] = '?'
            break

print(len(pairs))
for p in pairs:
    print(p[0], p[1])