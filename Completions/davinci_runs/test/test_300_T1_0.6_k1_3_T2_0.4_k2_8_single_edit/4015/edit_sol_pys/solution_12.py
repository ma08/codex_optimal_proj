
import math
import sys


input_list = sys.stdin.read().split()

n = int(input_list[0])
m = int(input_list[1])

if n == m:
    print(0)
else:
    if m % n != 0:
        print(-1)
    else:
        m = m / n
        count = 0
        while m > 1:
            if m % 2 != 0 and m % 3 != 0:
                print(-1)
                break
            elif m % 2 == 0:
                m = m / 2
                count += 1
            elif m % 3 == 0:
                m = m / 3
                count += 1
        if m == 1:
            print(count)
