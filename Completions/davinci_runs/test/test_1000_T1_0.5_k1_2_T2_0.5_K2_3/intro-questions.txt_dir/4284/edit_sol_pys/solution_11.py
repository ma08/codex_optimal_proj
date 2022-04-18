

#-----Solution-----

#The solution is to compute the number of first type turns that can be played,
#the number of second type turns that can be played, and the maximum of the two.

#The number of first type turns that can be played is the maximum n such that
#k-n*a >= 0

#The number of second type turns that can be played is the maximum n such that
#k-n*b >= 0

#If the maximum of the two is less than n, then the answer is -1. Otherwise, the answer is the maximum of the two.

import math

def max_turns(k, n, a, b):
    max_turns_1 = math.floor(k/a)
    max_turns_2 = math.floor(k/b)
    if max(max_turns_1, max_turns_2) < n:
        return -1
    return max(max_turns_1, max_turns_2)

q = int(input())
for _ in range(q):
    k, n, a, b = map(int, input().split())
    print(max_turns(k, n, a, b))
