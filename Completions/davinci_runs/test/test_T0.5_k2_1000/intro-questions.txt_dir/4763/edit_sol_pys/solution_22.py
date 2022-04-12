

import sys

def main():
    n = int(sys.stdin.readline().strip())
    if n == 0:
        print("impossible")
    elif n <= 20:
        print("single", n)
    elif n <= 40 and n % 2 == 0:
        print("double", n//2)
    elif n <= 60 and n % 2 == 0:
        print("single", 20)
        print("double", (n-20)//2)
    elif n <= 80 and n % 2 == 0:
        print("double", 20)
        print("single", (n-40)//2)
    elif n <= 90 and n % 3 == 0:
        print("triple", n//3)
    elif n <= 110 and n % 3 == 0:
        print("single", 20)
        print("triple", (n-20)//3)
    elif n <= 130 and n % 3 == 0:
        print("double", 20)
        print("triple", (n-40)//3)
    elif n <= 150 and n % 3 == 0:
        print("triple", 20)
        print("single", (n-60)//3)
    elif n <= 180 and n % 2 == 0:
        print("triple", 20)
        print("double", (n-60)//2)

if __name__ == '__main__':
    main()
