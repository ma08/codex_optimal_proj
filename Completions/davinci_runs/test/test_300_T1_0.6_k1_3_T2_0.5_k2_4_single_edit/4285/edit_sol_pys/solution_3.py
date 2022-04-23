

import sys

def main():
    n = int(sys.stdin.readline())
    s = sys.stdin.readline()
    a = 0
    b = 0
    c = 0
    count = 1
    for i in range(n):
        if s[i] == "a":
            a += 1
        elif s[i] == "b":
            b += 1
        elif s[i] == "c":
            c += 1
        else:
            count = (count * 3) % 1000000007
    print ((a * b * c * count) % 1000000007)

if __name__ == '__main__':
    main()
