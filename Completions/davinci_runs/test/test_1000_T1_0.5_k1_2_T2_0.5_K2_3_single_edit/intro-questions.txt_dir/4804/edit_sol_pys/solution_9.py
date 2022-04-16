

import sys

def main():
    s = int(sys.stdin.readline().strip())
    print(s, ":", end="")
    for i in range(2, int(s/2)+1):
        if s % i == 0 and s/i <= i:
            print("", i, int(s/i), end="")
        elif s % i <= i and s/i >= i:
            print("", i, int(s/i), end="")
        elif s % i <= int(s/i) and s/i >= i:
            print("", i, int(s/i), end="")
        elif s % i <= int(s/i) and s/i >= i+1:
            print("", i, int(s/i), end="")

if __name__ == "__main__":
    main()
