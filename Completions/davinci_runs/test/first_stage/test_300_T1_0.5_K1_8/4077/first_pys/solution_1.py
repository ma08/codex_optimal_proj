

import math

def get_median(numbers):
    numbers = sorted(numbers)
    if len(numbers) % 2 == 0:
        return numbers[int(math.floor(len(numbers) / 2))]
    else:
        return numbers[int(math.floor(len(numbers) / 2))]

def main():
    n, m = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    count = 0
    for i in range(n):
        for j in range(i, n):
            if get_median(a[i:j+1]) == m:
                count += 1
    print(count)

if __name__ == "__main__":
    main()