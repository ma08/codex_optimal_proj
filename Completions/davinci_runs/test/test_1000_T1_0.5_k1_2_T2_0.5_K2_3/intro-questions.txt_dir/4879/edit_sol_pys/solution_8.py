def main():
    a, b, c = input().split()  # a is the value of the number of the street
    # b is the direction of the first street
    # c is the direction of the second street
    if b == "North" and c == "South":
        print("Yes")
    elif b == "South" and c == "North":
        print("Yes")
    elif b == "West" and (c == "East" or c == "South"):
        print("Yes")
    elif b == "East" and (c == "West" or c == "South"):
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
