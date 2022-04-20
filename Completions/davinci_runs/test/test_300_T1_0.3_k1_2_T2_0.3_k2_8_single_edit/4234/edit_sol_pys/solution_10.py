

import sys

def main():
    n = int(input())
    s = input().strip()
    if n % 2 == 1:
        print(n, s)
    else:
        good = True
        for i in range(0, n, 2):
            if s[i] == s[i+1]:
                good = False
                break
        if good:
            print(0, s)
        else:
            print(n-1, s[:n-1])

if __name__ == "__main__":
    main()
