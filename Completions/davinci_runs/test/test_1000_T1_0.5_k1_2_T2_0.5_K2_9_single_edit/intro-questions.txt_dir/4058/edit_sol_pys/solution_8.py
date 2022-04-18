
import sys

def main():
    n, r = map(int, sys.stdin.readline().split())  # read number of houses and radius
    a = list(map(int, sys.stdin.readline().split()))
    heaters = []
    for i in range(n):
        if a[i] == 1:  # if house has heater
            heaters.append(i)
    if len(heaters) == 0:  # if no house has heater
        print(-1)
        return
    heaters.append(n)  # add last house number
    heaters.insert(0, -r)  # add first house number
    i = 0
    ans = 0
    while i < len(heaters) - 1:
        if heaters[i] + r - 1 >= heaters[i + 1]:  # if it can cover next heater
            heaters.pop(i)
        else:
            i += 1
            ans += 1  # add new heater
    print(ans)

if __name__ == '__main__':
    main()
