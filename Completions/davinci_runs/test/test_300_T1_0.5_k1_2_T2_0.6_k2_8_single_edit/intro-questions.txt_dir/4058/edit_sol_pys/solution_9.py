import sys

def main():
    n, r, avg = map(int, sys.stdin.readline().split())
    a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    a.sort(key=lambda x: x[0])
    total = r * avg
    current = sum([a[i][1] for i in range(n)])
    ans = 0
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
