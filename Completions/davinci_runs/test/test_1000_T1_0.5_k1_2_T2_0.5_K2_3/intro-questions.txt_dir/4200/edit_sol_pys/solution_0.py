

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    if max(a) >= sum(a) / (4 * m) or n < m:
        print("NO")
    else:
        print("YES")


if __name__ == "__main__":
    main()
