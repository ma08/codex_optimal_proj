


def main():
    a, b, c = input().split()
    if b == "North" and c == "South" or b == "South" and c == "North" or b == "West" and (c == "East" or c == "South") or b == "East" and (c == "West" or c == "South"):
        print("YES")
    print("NO")


if __name__ == '__main__':
    main()
