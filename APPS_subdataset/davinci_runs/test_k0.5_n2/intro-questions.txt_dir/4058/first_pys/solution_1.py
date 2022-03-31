

def solve(n, r, heaters):
    heaters = [i for i, x in enumerate(heaters) if x == 1]
    heaters.sort()
    if not heaters:
        return -1
    if heaters[0] > r - 1:
        return -1
    if heaters[-1] < n - r:
        return -1
    count = 1
    for i in range(1, len(heaters)):
        if heaters[i] - heaters[i - 1] > 2 * r - 1:
            count += 1
    return count

n, r = map(int, input().split())
heaters = list(map(int, input().split()))
print(solve(n, r, heaters))