
import math
import sys

def main():
    n = int(sys.stdin.readline().strip())
    a = [int(i) for i in sys.stdin.readline().strip().split(' ')]
    a.sort()
    sum_a = sum(a)
    max_a = max(a)
    min_a = min(a)

    if sum_a % n == 0:
        print(0)
    else:
        mean = math.floor(sum_a / n)
        max_a_count = a.count(max_a)
        min_a_count = a.count(min_a)
        if max_a_count > 1:
            print(max_a - mean)
        elif min_a_count > 1:
            print(mean - min_a)
        else:
            print(max(max_a - mean, mean - min_a))

main()
