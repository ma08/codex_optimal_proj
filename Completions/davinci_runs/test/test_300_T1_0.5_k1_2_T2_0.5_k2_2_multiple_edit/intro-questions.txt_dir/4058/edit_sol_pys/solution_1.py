import sys

def solve(n, r, a):
    heaters = []
    for i in range(n):
        if a[i] == 1:
            heaters.append(i)
    if len(heaters) == 0:
        return -1
    heaters.append(n)
    heaters.insert(0, -r)
    i = 0
    ans = 0
    while i < len(heaters) - 1:
        if heaters[i] + r - 1 >= heaters[i + 1]:
            heaters.pop(i)
        else:
            i += 1
            ans += 1
    return ans

def main():
    n, r = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    print(solve(n, r, a))

if __name__ == '__main__':
    main()
