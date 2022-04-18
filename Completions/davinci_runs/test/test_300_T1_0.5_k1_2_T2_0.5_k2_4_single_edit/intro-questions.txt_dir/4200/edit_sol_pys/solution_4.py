

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    if max(a) >= sum(a) / (4 * m):


def main2():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()

    if a[-1] < b[0]:
        print("Yes")
    else:
        print("No")

        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
