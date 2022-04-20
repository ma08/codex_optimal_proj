

import sys

def main():
    n = int(input())
    s = input().strip()
    if n % 2 == 0:
        good = True
        for i in range(0, n, 2):
            if s[i] == s[i+1]:
                good = False
                break
        if good:
            print(0)
            print(s)
        else:
            print(n-1)
            print(s[:n-1])
    else:
        print(n)
        print(s)

if __name__ == "__main__":
    main()
