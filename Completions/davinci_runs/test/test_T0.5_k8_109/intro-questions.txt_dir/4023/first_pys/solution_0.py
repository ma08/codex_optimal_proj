

def main():
    n = int(input())
    a = [int(x) for x in input().split()]

    # find the max height
    max_height = max(a)

    # find the number of parts at max height
    max_parts = a.count(max_height)

    # find the number of parts not at max height
    not_max_parts = n - max_parts

    # if the number of parts not at max height is even and not zero,
    # then we can put bricks at max height
    if not_max_parts % 2 == 0 and not_max_parts != 0:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()