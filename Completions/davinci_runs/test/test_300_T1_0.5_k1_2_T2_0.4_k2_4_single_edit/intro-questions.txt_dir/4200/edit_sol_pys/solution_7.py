

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    if max(a) * (4 * m) >= sum(a):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
