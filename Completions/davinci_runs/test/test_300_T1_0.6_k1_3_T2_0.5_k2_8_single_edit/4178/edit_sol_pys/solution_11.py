import sys

input = sys.stdin.readline


n = int(input())
h = list(map(int, input().split()))
if n == 1:
    print('Yes')
else:
    if all(h[i] <= h[i+1] for i in range(n-1)) or all(h[i] >= h[i+1] for i in range(n-1)):
        print('Yes') 
    elif all(h[i+1] <= h[i] - 1 for i in range(n-1)) or all(h[i+1] >= h[i] + 1 for i in range(n-1)):
        print('Yes') 
    else: print('No')
