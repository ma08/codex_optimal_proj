

import sys

def main():
    n = int(sys.stdin.readline().strip())
    if n == 0:
        print("impossible")
    elif n <= 20:
        print("single", n)
    elif 20 < n <= 40:
        print("double", n//2)
    elif 40 < n <= 60:
        print("single", 20)
        print("double", (n-20)//2)
    elif 60 < n <= 80:
        print("double", 20)
        print("single", (n-40)//2)
    elif 80 < n <= 90:
        print("triple", n//3)
    elif 90 < n <= 110:
        print("single", 20)
        print("triple", (n-20)//3)
    elif 110 < n <= 130:
        print("double", 20)
        print("triple", (n-40)//3)
    elif 130 < n <= 150:
        print("triple", 20)
        print("single", (n-60)//3)
    elif 150 < n <= 180:
        print("triple", 20)
        print("double", (n-60)//3)

if __name__ == '__main__':
    main()
