

import sys

def main():
    x, y = [int(i) for i in sys.stdin.readline().split()]
    # x = number of cookies, y = number of people
    if y == 1: # if there is only 1 person, then it is impossible to share
        print("IMPOSSIBLE")
    elif x == 0:
        print("ALL GOOD")
    else:
        print(x / (y - 1))

if __name__ == "__main__":
    main()
