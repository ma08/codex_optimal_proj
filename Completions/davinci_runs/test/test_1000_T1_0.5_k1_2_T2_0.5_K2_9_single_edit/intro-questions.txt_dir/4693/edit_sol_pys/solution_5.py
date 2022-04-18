

#!/usr/bin/env python3

# get input
num1, num2 = map(int, input().split())

# calculate sum
sum = num1 + num2

# output
if sum >= 10:
    print("Error")
else:
    print(sum)
