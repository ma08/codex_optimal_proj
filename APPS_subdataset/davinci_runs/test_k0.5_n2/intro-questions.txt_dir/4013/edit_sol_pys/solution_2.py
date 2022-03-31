
def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    min_diff = a[n-1] - a[0]
    for i in range(n):
        if i == 0:
            diff = a[i+1] - a[i]
        elif i == n-1:
            diff = a[i] - a[i-1]
        else:
            diff = min(a[i] - a[i-1], a[i+1] - a[i])
        if diff < min_diff:
            min_diff = diff
    print(min_diff)


if __name__ == "__main__":
    main()
