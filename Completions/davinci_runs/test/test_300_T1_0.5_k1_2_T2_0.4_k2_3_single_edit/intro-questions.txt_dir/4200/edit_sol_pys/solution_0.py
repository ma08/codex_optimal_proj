

def main():
    a = list(map(int, input().split()))
    n, m = map(int, input().split())
    a.sort(reverse=True)

    if max(a) >= sum(a) / (4 * m):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
