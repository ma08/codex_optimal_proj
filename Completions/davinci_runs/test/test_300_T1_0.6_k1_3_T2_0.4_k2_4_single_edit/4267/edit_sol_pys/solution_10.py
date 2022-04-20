
import sys

def main():
    for x in sys.stdin:
        x = int(x)
        if x >= 30:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()
