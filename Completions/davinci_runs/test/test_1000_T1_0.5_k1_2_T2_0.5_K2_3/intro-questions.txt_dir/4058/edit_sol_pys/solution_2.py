import sys

def main():
    n, r = map(int, sys.stdin.readline().split())  # read n and r
    a = list(map(int, sys.stdin.readline().split()))
    heaters = []  # array of heaters
    for i in range(n):
        if a[i] == 1:  # if heater is here
            heaters.append(i)
    if len(heaters) == 0:  # if there are no heaters
        print(-1)
        return
    heaters.append(n)  # add right bound
    heaters.insert(0, -r)  # add left bound
    i = 0
    ans = 0  # answer
    while i < len(heaters) - 1:
        if heaters[i] + r - 1 >= heaters[i + 1]:  # if the next heater is in radius of the current heater
            heaters.pop(i)
        else:
            i += 1
            ans += 1  # add 1 to answer
    print(ans)

if __name__ == '__main__':
    main()
