

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    if max(a) >= sum(a) / (4 * m):
        print("Yes")  # ????????
    else:


def main2():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    # ????
    a.sort(reverse=True)
    # ?????
    a = a[:m]

    if a[-1] >= sum(a) / (4 * m):
        print("Yes")
    else:
        print("No")  # ????????


if __name__ == "__main__":
    main()
