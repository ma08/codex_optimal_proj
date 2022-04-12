

import sys

def main():
    s = int(sys.stdin.readline())
    print(s, ":")
    if s == 1:
        print("1,1")
    elif s == 2:
        print("2,1")
    elif s == 3:
        print("3,1")
        print("2,2")
    else:
        for i in range(2, int(s/2)+2):
            if s % i == 0 and s/i <= i: print(i, int(s/i))
            elif s % i <= i and s/i >= i: print(i, int(s/i))
            elif s % i <= int(s/i) and s/i >= i: print(i, int(s/i))
            elif s % i <= int(s/i) and s/i >= i+1: print(i, int(s/i))

if __name__ == "__main__":
    main()
