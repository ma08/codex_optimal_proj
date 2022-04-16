

import sys

def main():
    n = int(sys.stdin.readline().strip())
    if n == 0:
        print("impossible")
    elif n <= 20:
        print("single", n, "points")
    elif n <= 40:
        print("double", n//2, "points")
    elif n <= 60:
        print("single", 20, "points")
        print("double", (n-20)//2, "points")
    elif n <= 80:
        print("double", 20, "points")
        print("single", (n-40)//2, "points")
    elif n <= 90:
        print("triple", n//3, "points")
    elif n <= 110:
        print("single", 20, "points")
        print("triple", (n-20)//3, "points")
    elif n <= 130:
        print("double", 20, "points")
        print("triple", (n-40)//3, "points")
    elif n <= 150:
        print("triple", 20, "points")
        print("single", (n-60)//3, "points")
    elif n <= 180:
        print("triple", 20, "points")
        print("double", (n-60)//3, "points")

if __name__ == '__main__':
    main()
