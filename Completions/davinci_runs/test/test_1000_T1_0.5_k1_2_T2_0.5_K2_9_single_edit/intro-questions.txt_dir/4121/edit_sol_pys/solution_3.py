

def main():
    n = int(input())
    a = sorted(list(map(int, input().split())))
    if a[n-1] != a[n-2]:
        print(a[n-1])
    else:
        print(a[n-2])


if __name__ == "__main__":
    main()
