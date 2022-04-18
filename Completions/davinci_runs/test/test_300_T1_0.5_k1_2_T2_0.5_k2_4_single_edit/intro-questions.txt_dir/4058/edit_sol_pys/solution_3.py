#!/usr/bin/env python3

import sys

def main():
    n, r = map(int, sys.stdin.readline().split()) # n = number of houses, r = radius
    a = list(map(int, sys.stdin.readline().split())) # a = list of houses
    heaters = []
    for i in range(n):
        if a[i] == 1: # if house is heater
            heaters.append(i)
    if len(heaters) == 0:
        print(-1)
        return
    heaters.append(n) # add house n as heater
    heaters.insert(0, -r) # add house -r as heater
    i = 0
    ans = 0
    while i < len(heaters) - 1:
        if heaters[i] + r - 1 >= heaters[i + 1]:
            heaters.pop(i) # if heaters overlap, delete one
        else:
            i += 1
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()
