

import sys

def main():
    n = int(input())
    glasses = list(map(int, input().split()))
    glasses.sort()
    limes = list(range(1, n + 1))
    limes.sort()
    lime_sum = sum(limes)
    glass_sum = sum(glasses)
    if glass_sum < lime_sum:
        print('impossible')
        return
    i = 0
    j = 0
    while i < n and j < n:
        if glasses[i] >= limes[j]:
            lime_sum -= limes[j]
            glass_sum -= glasses[i]
            i += 1
            j += 1
        else:
            glass_sum -= glasses[i]
            i += 1
    if glass_sum < lime_sum:
        print('impossible')
        return
    print(lime_sum / sum(limes))

if __name__ == "__main__":
    main()
