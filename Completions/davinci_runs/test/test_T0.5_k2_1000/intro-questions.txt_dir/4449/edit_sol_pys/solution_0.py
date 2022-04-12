
# Solution 1 (Brute Force)

import sys

def is_possible(sticks, n):
    for i in range(4*n):
        for j in range(i+1, 4*n):
            if sticks[i] != sticks[j] and sticks[i]*sticks[j] % (sticks[i]+sticks[j]) == 0:
                sticks[i] = sticks[j] = sticks[i]+sticks[j]
                return True
    return False

q = int(input())
for _ in range(q):
    n = int(input())
    sticks = list(map(int, input().split()))
    if is_possible(sticks, n):
        print("YES")
    else:
        print("NO")

# Solution 2 (Recursion)
import sys

def is_possible(sticks, n):
    sticks.sort()
    if sticks[0] == sticks[-1]:
        return True
    if sticks[0]*sticks[-1] % (sticks[0]+sticks[-1]) != 0:
        return False
    sticks[0] += sticks[-1]
    return is_possible(sticks, n)

q = int(input())
for _ in range(q):
    n = int(input())
    sticks = list(map(int, input().split()))
    if is_possible(sticks, n):
        print("YES")
    else:
        print("NO")
