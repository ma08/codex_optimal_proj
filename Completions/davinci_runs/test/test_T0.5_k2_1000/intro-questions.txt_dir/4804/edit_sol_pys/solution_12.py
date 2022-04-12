

import sys

def main():
    s = int(sys.stdin.readline())
    print(s, ":", sep="")
    if s > 3:
        print("2,1", sep="")
        print("2,2", sep="")
        print("3,2", sep="")
        for i in range(5, int(s/2)+2):
            if s % i == 0 and s/i <= i:
                print(i, int(s/i), sep="")
            elif s % i <= i and s/i >= i:
                print(i, int(s/i), sep="")
            elif s % i <= int(s/i) and s/i >= i:
                print(i, int(s/i), sep="")
            elif s % i <= int(s/i) and s/i >= i+1:
                print(i, int(s/i), sep="")

if __name__ == "__main__":
    main()
