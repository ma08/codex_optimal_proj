import sys

def main():
    n, r = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    heaters_pos = []
    for i in range(n):
        if a[i] == 1:
            heaters_pos.append(i)
    if len(heaters_pos) == 0:
        print(-1)
        return
    heaters_pos.append(n)
    heaters_pos.insert(0, -r)
    i = 0
    ans = 0
    while i < len(heaters_pos) - 1:
        if heaters_pos[i] + r - 1 >= heaters_pos[i + 1] - r:
            heaters_pos.pop(i)
        else:
            i += 1
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()
