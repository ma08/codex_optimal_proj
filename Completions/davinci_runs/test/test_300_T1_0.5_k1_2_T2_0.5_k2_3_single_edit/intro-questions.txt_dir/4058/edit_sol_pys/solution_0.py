

import sys

def main():
    n, r = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    heaters = []
    for i in range(n):
        if a[i] == 1:
            heaters.append(i)
    if len(heaters) == 0:
        print(0)
        return
    heaters.insert(0, 0)
    i = 0
    ans = 0
    while i < len(heaters) - 1:
        if heaters[i] + r >= heaters[i + 1]:
            heaters.pop(i)
        else:
            i += 1
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()
