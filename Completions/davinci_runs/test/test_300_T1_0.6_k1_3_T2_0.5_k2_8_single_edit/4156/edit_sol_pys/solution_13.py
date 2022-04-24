

def solve(n, w, a):
    min_passengers = max_passengers = 0
    for i in range(n):
        max_passengers += a[i]
        min_passengers = max(min(min_passengers+a[i], 0), max_passengers)

    if max_passengers > w:
        return 0
    else:
        return w-max_passengers+1-min_passengers


if __name__ == '__main__':
    n, w = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(n, w, a))
