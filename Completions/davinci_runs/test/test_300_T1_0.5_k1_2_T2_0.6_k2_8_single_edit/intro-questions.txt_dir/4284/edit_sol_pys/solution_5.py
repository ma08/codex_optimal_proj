#-----Solution-----


#The solution is to split the number into the number of elements of the first
#type and the number of elements of the second type. Then, the answer is the
#minimum of the number of elements that can be removed from the first type and
#the number of elements that can be removed from the second type.

#The number of elements that can be removed from the first type is the maximum
#number of elements of the second type that can be added such that the number of
#elements of the second type is less than or equal to the target number of
#elements of the second type.

#The number of elements that can be removed from the second type is the maximum
#number of elements of the first type that can be added such that the number of
#elements of the second type is less than or equal to the target number of
#elements of the second type.

#If the minimum of the two is less than n, then the answer is -1. Otherwise, the
#answer is the minimum of the two.

def max_turns(n, a, b, c, d):
    max_turns_1 = d//b - a
    max_turns_2 = c//a - b
    if min(max_turns_1, max_turns_2) < n:
        return -1
    return min(max_turns_1, max_turns_2)

q = int(input())
for _ in range(q):
    n, a, b, c, d = map(int, input().split())
    print(max_turns(n, a, b, c, d))

#The solution is to compute the number of first type turns that can be played
#and the number of second type turns that can be played. The maximum will be the
#maximum of the two.

#The number of first type turns that can be played is the maximum n such that
#k-n*a >= 0

#The number of second type turns that can be played is the maximum n such that
#k-n*b >= 0

#If the maximum of the two is less than n, then the answer is -1. Otherwise, the
#answer is the maximum of the two.

import math
#
# def max_turns(k, n, a, b):
#     max_turns_1 = math.floor(k/a)
#     max_turns_2 = math.floor(k/b)
#     if max(max_turns_1, max_turns_2) < n:
#         return -1
#     return max(max_turns_1, max_turns_2)
#
# q = int(input())
# for _ in range(q):
#     k, n, a, b = map(int, input().split())
#     print(max_turns(k, n, a, b))
