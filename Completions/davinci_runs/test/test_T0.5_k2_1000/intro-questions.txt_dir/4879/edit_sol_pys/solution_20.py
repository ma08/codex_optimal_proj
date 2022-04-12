


def main():
    a, b, c = input().split()  # split the input
    if b == "North" and c == "South" or b == "South" and c == "North":  # check if the directions are opposite
        print("Yes")
    elif b == "West" and c == "East" or b == "East" and c == "West":  # check if the directions are opposite
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
