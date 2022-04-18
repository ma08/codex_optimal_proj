

import sys
sum_digits = 0
n = int(sys.stdin.readline().strip())

while True:
    n += 1
    sum_digits = 0 
    for digit in str(n):
        sum_digits += int(digit)
    if n % sum_digits == 0:
        break

print(n)
