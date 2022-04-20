

# My Solution

import math

N = int(input())

if N == 1:
    print("No")
else:
    for i in range(2, int(math.sqrt(N)) + 1):
        if N % i == 0:
            if i <= 9 and N // i <= 9:
                print("Yes")
                break
            else:
                print("No")
                break