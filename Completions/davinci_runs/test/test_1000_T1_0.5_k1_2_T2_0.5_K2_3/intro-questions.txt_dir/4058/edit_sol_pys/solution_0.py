

import sys

def main():
    n, r = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    heaters = [-r]
    for i in range(n):
        if a[i] == 1:
            heaters.append(i)
    if len(heaters) == 1:
        print(-1)
        return
    heaters.append(n)
    i = 0
    ans = 0
    while i < len(heaters) - 1:
        if heaters[i] + r - 1 >= heaters[i + 1]:
            heaters.pop(i)
        else:
            i += 1
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()
