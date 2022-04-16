


def main():
    a, b, c = input().split()
    if b == "North" and (c == "South" or c == "West"):
        print("Yes")
    elif b == "South" and (c == "North" or c == "West"):
        print("Yes")
    elif b == "West" and (c == "East" or c == "South"):
        print("Yes")
    elif b == "East" and (c == "West" or c == "South"):
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
