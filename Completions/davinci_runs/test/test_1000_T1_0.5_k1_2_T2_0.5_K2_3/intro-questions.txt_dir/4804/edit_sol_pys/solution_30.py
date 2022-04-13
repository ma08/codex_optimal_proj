

import sys

def main():
    s = int(sys.stdin.readline()) # read from stdin
    print(s, ":")
    if s % 2 == 0:
        for i in range(2, int(s/2)+1):
            if s % i == 0:
                print(i, int(s/i))
    else:
        for i in range(2, int(s/2)+2):
            if s % i == 0:
                print(i, int(s/i))

if __name__ == "__main__":
    main()
