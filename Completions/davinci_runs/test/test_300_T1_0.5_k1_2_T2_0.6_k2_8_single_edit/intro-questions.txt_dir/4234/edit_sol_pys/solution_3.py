

import sys

def main():
    n = int(input())
    s = input()
    i = 0
    while i < n-1:
        if s[i] == s[i+1]:
            print(n-i)
            print(s[:i] + s[i+1:])
            return
        i += 2
    print(0)
    print(s)

if __name__ == '__main__':
    main()
