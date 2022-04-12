

import sys

def main():
    n = int(sys.stdin.readline())
    print(n, ":")
    if n > 3:
        print("2,1")
        print("2,2")
        print("3,2")
        for i in range(4, int(n/2)+1):
            if n % i == 0 and n/i <= i:
                print(i, int(n/i))
            elif n % i <= i and n/i >= i:
                print(i, int(n/i))
            elif n % i <= int(n/i) and n/i >= i:
                print(i, int(n/i))
            elif n % i <= int(n/i) and n/i >= i+1:
                print(i, int(n/i))

if __name__ == "__main__":
    main()
