

# import sys

# a, b, c = map(int, sys.stdin.readline().rstrip().split())

# if a == 5 and b == 7 and c == 5:
#     print("YES")
# else:
#     print("NO")

# import sys

# a, b, c = map(int, sys.stdin.readline().rstrip().split())

# if a == 5 and b == 7 and c == 5:
#     print("YES")
# else:
#     print("NO")

import sys, string, math

n = int(input())
L = [ int(x) for x in input().split()]
L2 = sorted(L)
#print(L2)
for i in range(0,n) :
    if L[i] != L2[i] :
        print(i)
        break
