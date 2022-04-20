

import math
from collections import Counter

def median(numbers):
    numbers.sort()
    if len(numbers) % 2 == 0:
        return numbers[int(len(numbers)/2)-1]
    else:
        return numbers[int(math.floor(len(numbers)/2))]

def find_median(perm, m):
    count = 0
    for i in range(len(perm)):
        for j in range(i, len(perm)):
            if median(perm[i:j+1]) == m:
                count += 1
    return count

def main():
    n, m = [int(x) for x in input().split()]
    perm = [int(x) for x in input().split()]
    print(find_median(perm, m))

if __name__ == "__main__":
    main()