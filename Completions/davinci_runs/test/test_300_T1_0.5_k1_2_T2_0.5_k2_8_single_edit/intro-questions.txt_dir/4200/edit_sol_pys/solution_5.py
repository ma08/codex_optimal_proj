
def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    print("Yes" if max(a) >= sum(a) / (4 * m) else "No")


if __name__ == "__main__":
    main()
