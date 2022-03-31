

def solve(n, r, houses):
    houses = [i for i, x in enumerate(houses) if x == 1]
    houses.sort()
    if not houses:
        return -1
    if houses[0] > r - 1:
        return -1
    if houses[-1] < n - r + 1:
        return -1
    count = 1
    for i in range(1, len(houses)):
        if houses[i] - houses[i - 1] > 2 * r - 1:
            count += 1
    return count

n, r = map(int, input().split())
houses = list(map(int, input().split()))
print(solve(n, r, houses))
