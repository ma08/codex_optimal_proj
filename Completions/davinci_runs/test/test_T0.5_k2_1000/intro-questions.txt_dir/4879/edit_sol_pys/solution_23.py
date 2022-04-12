

def main():
    a, b, c = input().split()  # a is the number of the street, b is the direction of the first house, c is the direction of the second house, and a is the number of the street
    if b == "West" and c == "East":  # if the first house is west and the second house is east, then they are facing each other
        print("Yes")
    elif b == "East" and c == "West":
        print("Yes")
    elif b == "North" and c == "South":
        print("Yes")
    elif b == "South" and c == "North":
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
