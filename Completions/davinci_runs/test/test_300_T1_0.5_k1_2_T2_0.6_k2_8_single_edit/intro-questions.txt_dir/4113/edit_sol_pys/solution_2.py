

import math

N = input()

for i in range(int(math.sqrt(int(N))), 0, -1):
    if i * i == int(N):
        print("Yes")
        exit()
print("No") 
