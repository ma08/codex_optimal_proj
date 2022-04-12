
import sys

def main():
    n = int(sys.stdin.readline().strip())
    rooms = [int(x) for x in sys.stdin.readline().strip().split()]

    if n == 2:
        if rooms[0] == 1 and rooms[1] == 1:
            print("1 2")
        elif rooms[0] == 1 and rooms[1] == 2:
            print("2 1")
        elif rooms[0] == 2 and rooms[1] == 1:
            print("1 2")
        elif rooms[0] == 2 and rooms[1] == 2:
            print("Impossible")
        else:
            print("Impossible")
    elif n == 3:
        if rooms[0] == 1 and rooms[1] == 1 and rooms[2] == 1:
            print("1 2 3")
        elif rooms[0] == 1 and rooms[1] == 1 and rooms[2] == 2:
            print("2 3 1")
        elif rooms[0] == 1 and rooms[1] == 2 and rooms[2] == 1:
            print("1 3 2")
        elif rooms[0] == 1 and rooms[1] == 2 and rooms[2] == 2:
            print("2 1 3")
        elif rooms[0] == 2 and rooms[1] == 1 and rooms[2] == 1:
            print("1 2 3")
        elif rooms[0] == 2 and rooms[1] == 1 and rooms[2] == 2:
            print("1 3 2")
        elif rooms[0] == 2 and rooms[1] == 2 and rooms[2] == 1:
            print("1 2 3")
        elif rooms[0] == 2 and rooms[1] == 2 and rooms[2] == 2:
            print("Impossible")
        else:
            print("Impossible")
    elif n == 4:
        if rooms[0] == 1 and rooms[1] == 1 and rooms[2] == 1 and rooms[3] == 1:
            print("1 2 3 4")
        elif rooms[0] == 1 and rooms[1] == 1 and rooms[2] == 1 and rooms[3] == 2:
            print("2 3 4 1")
        elif rooms[0] == 1 and rooms[1] == 1 and rooms[2] == 2 and rooms[3] == 1:
            print("1 3 4 2")
        elif rooms[0] == 1 and rooms[1] == 1 and rooms[2] == 2 and rooms[3] == 2:
            print("2 1 4 3")
        elif rooms[0] == 1 and rooms[1] == 2 and rooms[2] == 1 and rooms[3] == 1:
            print("1 3 4 2")
        elif rooms[0] == 1 and rooms[1] == 2 and rooms[2] == 1 and rooms[3] == 2:
            print("1 4 3 2")
        elif rooms[0] == 1 and rooms[1] == 2 and rooms[2] == 2 and rooms[3] == 1:
            print("1 3 2 4")
        elif rooms[0] == 1 and rooms[1] == 2 and rooms[2] == 2 and rooms[3] == 2:
            print("2 1 4 3")
        elif rooms[0] == 2 and rooms[1] == 1 and rooms[2] == 1 and rooms[3] == 1:
            print("1 2 3 4")
        elif rooms[0] == 2 and rooms[1] == 1 and rooms[2] == 1 and rooms[3] == 2:
            print("1 3 4 2")
        elif rooms[0] == 2 and rooms[1] == 1 and rooms[2] == 2 and rooms[3] == 1:
            print("1 3 2 4")
        elif rooms[0] == 2 and rooms[1] == 1 and rooms[2] == 2 and rooms[3] == 2:
            print("1 2 4 3")
        elif rooms[0] == 2 and rooms[1] == 2 and rooms[2] == 1 and rooms[3] == 1:
            print("1 3 4 2")
        elif rooms[0] == 2 and rooms[1] == 2 and rooms[2] == 1 and rooms[3] == 2:
            print("1 2 4 3")
        elif rooms[0] == 2 and rooms[1] == 2 and rooms[2] == 2 and rooms[3] == 1:
            print("1 2 3 4")
        elif rooms[0] == 2 and rooms[1] == 2 and rooms[2] == 2 and rooms[3] == 2:
            print("Impossible")
        else:
            print("Impossible")
    else:
        print("Impossible")


if __name__ == "__main__":
    main()
