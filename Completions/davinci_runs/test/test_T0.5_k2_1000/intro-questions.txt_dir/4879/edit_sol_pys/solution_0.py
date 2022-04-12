


def main():
    a, b, c = input().split()
    if (b == "North" and c == "South") or (b == "South" and c == "North"):
        print("Yes")
    elif (b == "West" and c == "East") or (b == "East" and c == "West"):
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
