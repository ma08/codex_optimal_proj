

    a = []
def main():
    n, m = map(int, input().split())
    for _ in range(n):
        a.append(int(input()))
    if max(a) >= sum(a) / (4 * m):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
