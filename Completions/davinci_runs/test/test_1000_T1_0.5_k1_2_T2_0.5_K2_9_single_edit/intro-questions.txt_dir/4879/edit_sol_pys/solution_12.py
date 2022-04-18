

def main():
    a, b, c = input().split()  # a is a number and b and c are direction
    if b == "West" and c == "East":  # if the direction is west and east
        print("Yes")
    elif b == "East" and c == "West":  # if the direction is east and west
        print("Yes")
    elif b == "North" and c == "South":
        print("Yes")
    elif b == "South" and c == "North":
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
