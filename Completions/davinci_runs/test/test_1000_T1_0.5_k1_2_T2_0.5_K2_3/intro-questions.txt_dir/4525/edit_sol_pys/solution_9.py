import math
t = int(input())

for _ in range(t):
    n = int(input())
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            print("NO", end=" ")
            break
    else:
        print("YES")
