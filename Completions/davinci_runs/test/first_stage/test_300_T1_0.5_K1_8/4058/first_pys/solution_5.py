

import sys

def main():
    n, r = [int(x) for x in sys.stdin.readline().split()]
    a = [int(x) for x in sys.stdin.readline().split()]

    heaters = []
    for i in range(n):
        if a[i] == 1:
            heaters.append(i)

    if len(heaters) == 0:
        print(-1)
        return

    ans = 1
    prev = heaters[0]
    for i in range(1, len(heaters)):
        if heaters[i] - prev > r:
            ans += 1
            prev = heaters[i]

    print(ans)

if __name__ == '__main__':
    main()