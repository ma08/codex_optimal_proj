

import sys

def main():
    a, b, x = map(int, sys.stdin.readline().split())
    s = "0" * a + "1" * b + "0" * a
    for i in range(x):
        s = s[:i] + s[i+1] + s[i] + s[i+2]
    print(s)

if __name__ == "__main__":
    main()
