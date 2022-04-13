

# import sys

# [N, S, R] = map(int, sys.stdin.readline().split())
# damaged = map(int, sys.stdin.readline().split())
# reserve = map(int, sys.stdin.readline().split())

# def check(reserve, damaged):
#     for i in damaged:
#         if i-1 in reserve or i+1 in reserve:
#             reserve.remove(i-1)
#             reserve.remove(i+1)
#             damaged.remove(i)
#     return len(damaged)

# print check(reserve, damaged)

# a = [1,2,3]
# b = [1,2,3]
# if a == b:
#     print "yes"
# else:
#     print "no"

a = ['a','b','c']
b = ['a','b','c']
print a == b
