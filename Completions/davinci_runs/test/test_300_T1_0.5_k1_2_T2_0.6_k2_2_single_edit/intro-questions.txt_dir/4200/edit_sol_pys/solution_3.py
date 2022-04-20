

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    if max(a) >= sum(a) / (4.0 * m):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
