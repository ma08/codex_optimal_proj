
def solve(n, r, a):
    heaters = []
    for i in range(n):
        if a[i] == 1:
            heaters.append(i)
    if len(heaters) == 0:
        return -1
    if len(heaters) == 1 and (r < heaters[0] or r > n - heaters[0] - 1):
        return -1
    i = 0
    c = 0
    while i < len(heaters) - 1:
        if heaters[i + 1] - heaters[i] > 2 * r:
            return -1
        if heaters[i + 1] - heaters[i] > r:
            c += 1
            i += 1
        else:
            c += 1
            i += 2
    if i < len(heaters):
        c += 1
    return c

def main():
    n, r = list(map(int, input().split(' ')))
    a = list(map(int, input().split(' ')))
    print(solve(n, r, a))

if __name__ == "__main__":
    main()
