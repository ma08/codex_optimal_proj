

def main():
    n, m = map(int, input().split())  # int
    a = list(map(int, input().split()))  # list

    if max(a) >= sum(a) / (4 * m):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
