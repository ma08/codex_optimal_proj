

import sys

def main():
    n, r = map(int, sys.stdin.readline().split()) # n is the number of houses, r is the range of heaters
    a = list(map(int, sys.stdin.readline().split()))
    heaters = [] # heaters[i] is the index of the i-th heater
    for i in range(n):
        if a[i] == 1: # a[i] is 1 if there is a heater at the i-th house
            heaters.append(i)
    if len(heaters) == 0:
        print(-1)
        return
    heaters.append(n) # heaters[-1] is the index of the last house
    heaters.insert(0, -r) # heaters[0] is the index of the first house minus r
    i = 0
    ans = 0
    while i < len(heaters) - 1:
        if heaters[i] + r - 1 >= heaters[i + 1]: # if the i-th and (i+1)-th heater can cover the houses between them
            heaters.pop(i)
        else:
            i += 1
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()
