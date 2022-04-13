

import sys

def main():
    s = int(sys.stdin.readline())
    print(s, ":")
    for i in range(1, int(s/2)+1):
        if s % i == 0 and s/i <= i:
            print(i, int(s/i))
        elif s % i <= i and s/i >= i:
            print(i, int(s/i))
        elif s % i <= int(s/i) and s/i >= i:
            print(i, int(s/i))
        elif s % i <= int(s/i) and s/i >= i+1:
            print(i, int(s/i))

if __name__ == "__main__":
    main()
