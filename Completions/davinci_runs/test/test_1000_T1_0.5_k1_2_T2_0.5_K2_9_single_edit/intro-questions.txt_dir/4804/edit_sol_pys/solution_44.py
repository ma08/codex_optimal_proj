

import sys

def main():
    s = int(sys.stdin.readline())
    print(s, ":")
    if s > 3:
        print("2,1")
        print("2,2")
        print("3,2")
        for i in range(4, int(s/2)+1):
            if s % i == 0 and s/i <= i:
                print(int(s/i), i)
            elif s % i <= i and s/i >= i:
                print(int(s/i), i)
            elif s % i <= int(s/i) and s/i >= i:
                print(int(s/i), i)
            elif s % i <= int(s/i) and s/i >= i+1:
                print(int(s/i), i)

if __name__ == "__main__":
    main()
