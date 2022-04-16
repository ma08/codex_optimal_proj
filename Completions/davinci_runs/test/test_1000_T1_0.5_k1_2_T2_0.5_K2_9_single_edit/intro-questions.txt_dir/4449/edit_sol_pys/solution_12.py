

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
