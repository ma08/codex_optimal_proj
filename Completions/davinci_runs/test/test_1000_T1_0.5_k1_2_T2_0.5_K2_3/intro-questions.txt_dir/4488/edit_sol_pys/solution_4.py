
import sys

def main():
    num1 = int(sys.stdin.readline().rstrip())
    num2 = int(sys.stdin.readline().rstrip())

    if num1 > num2:
        print("GREATER")
    elif num1 < num2:
        print("LESS")
    else:
        print("EQUAL")

if __name__ == '__main__':
    main()
