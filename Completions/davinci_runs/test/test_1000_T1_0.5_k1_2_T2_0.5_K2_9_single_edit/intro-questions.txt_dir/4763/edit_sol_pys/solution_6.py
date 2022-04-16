

import sys

def main():
    n = int(sys.stdin.readline().strip())
    if n == 0:
        print("impossible")
    elif n <= 20:
        print("single", n)
    elif n <= 40:
        print("double", n//2)
    elif n <= 60:
        print("single", 20)
        print("double", (n-20)//2)
    elif n <= 80:
        print("double", 20)
        print("single", (n-40)//2)
    elif n <= 90:
        print("triple", n//3)
    elif n <= 110:
        print("single", 20)
        print("triple", (n-20)//3)
    elif n <= 130:
        print("double", 20)
        print("triple", (n-40)//3)
    elif n <= 150:
        print("triple", 20)
        print("single", (n-60)//3)
    elif n <= 180:
        print("triple", 20)
        print("double", (n-60)//3

if __name__ == '__main__':
    main()
