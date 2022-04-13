

import sys

def main():
    n = int(input())
    glasses = list(map(int, input().split()))
    glasses.sort(reverse=True)
    limes = list(range(1, n + 1))
    limes.sort(reverse=True)
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
    if glass_sum >= lime_sum:
        print(lime_sum / sum(limes) * 100)
    else:
        print('impossible')

if __name__ == "__main__":
    main()
