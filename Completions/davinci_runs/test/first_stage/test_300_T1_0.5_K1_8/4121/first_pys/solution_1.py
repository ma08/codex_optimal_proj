


def main():
    n = int(input())
    a = list(map(int, input().split()))

    if n == 1:
        print("YES")
        return

    # Check if the wall is already complete
    if all(x == a[0] for x in a):
        print("YES")
        return

    # Check if there are any gaps in the wall
    if any(a[i] + 1 != a[i + 1] for i in range(n - 1)):
        print("NO")
        return

    # Check if the wall can be completed using horizontal bricks
    if any(a[i] == a[i + 1] for i in range(n - 1)):
        print("YES")
        return

    # Check if the wall can be completed using vertical bricks
    if any(a[i] == a[i + 1] + 2 for i in range(n - 1)):
        print("YES")
        return

    print("NO")


if __name__ == "__main__":
    main()