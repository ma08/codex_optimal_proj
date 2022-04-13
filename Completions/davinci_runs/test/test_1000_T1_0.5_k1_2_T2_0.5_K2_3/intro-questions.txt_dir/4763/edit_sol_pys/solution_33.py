
import sys

def main():
    n = int(sys.stdin.readline().strip())
    if n == 0:
        print("impossible", end="")
    elif n <= 20:
        print("single", n, end="")
    elif n <= 40:
        print("double", n//2, end="")
    elif n <= 60:
        print("single", n-20, end="")
        print("double", (n-20)//2, end="")
    elif n <= 80:
        print("double", 20, end="")
        print("single", n-40, end="")
    elif n <= 90:
        print("triple", n//3, end="")
    elif n <= 110:
        print("single", n-20, end="")
        print("triple", (n-20)//3, end="")
    elif n <= 130:
        print("double", n-40, end="")
        print("triple", (n-40)//3, end="")
    elif n <= 150:
        print("triple", 20, end="")
        print("single", n-60, end="")
    elif n <= 180:
        print("triple", 20, end="")
        print("double", n-60, end="")

if __name__ == '__main__':
    main()
