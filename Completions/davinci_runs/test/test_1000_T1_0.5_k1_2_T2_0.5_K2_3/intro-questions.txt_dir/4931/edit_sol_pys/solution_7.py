
#this is a file
import sys

def main():
    x, y = [int(i) for i in sys.stdin.readline().split()]
    if y == 1:
        print("IMPOSSIBLE")
    elif x == 0:
        print("ALL GOOD")
    else:
        print(int(x / (y - 1)))

if __name__ == "__main__":
    main()
