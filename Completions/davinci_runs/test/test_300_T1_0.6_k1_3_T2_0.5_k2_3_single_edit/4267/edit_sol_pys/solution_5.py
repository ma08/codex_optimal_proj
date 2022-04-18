
import sys

def main():
    a = int(sys.stdin.readline())
    b = int(sys.stdin.readline())
    if a >= 30 and b >= 30:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
