

import math

N = int(input())
a = list(map(int, input().split()))

# count the number of each element
count = {}
for i in range(N):
    if(a[i] in count):
        count[a[i]] += 1
    else:
        count[a[i]] = 1

ans = 0
for k, v in count.items():
    # if the element is even
    if k % 2 == 0:
        ans += v
    # if the element is odd and the number of it is even
    elif k % 2 == 1 and v % 2 == 0:
        ans += v
        # if the element is odd and the number of it is odd
    elif k % 2 == 1 and v % 2 == 1:
        ans += v - 1

print(ans)
