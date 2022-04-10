

def main():
    n, x, y = map(int, input().split())
    a = list(map(int, input()))
    if a[y] == a[x]:
        a[x] = 1 - a[x]
    print(sum(a))


if __name__ == "__main__":
    main()