# -*- coding: utf-8 -*-

import sys



# def get_b(s):
#     b = []
#     for i in range(len(s)):
#         b.append(sum([abs(i-j) for j in range(len(s)) if s[j] > s[i]]))
#     return b

# def get_s(b):
#     s = ''
#     for i in range(len(b)):
#         s += chr(ord('a')+i)
#     return s

# def get_t(s, b):
#     t = ''
#     for i in range(len(b)):
#         t += s[b[i]]
#     return t


# def get_t(s, b):
#     t = ''
#     for i in range(len(b)):
#         t += s[b[i]]
#     return t


# for _ in range(int(sys.stdin.readline())):
#     s = sys.stdin.readline().strip()
#     m = int(sys.stdin.readline())
#     b = [int(i) for i in sys.stdin.readline().split()]
#     print(get_t(s, b))


def get_t(s, b):
    return ''.join([s[i] for i in b])


for _ in range(int(sys.stdin.readline())):
    s = sys.stdin.readline().strip()
    m = int(sys.stdin.readline())
    b = [int(i) for i in sys.stdin.readline().split()]
    print(get_t(s, b))
