

import sys

def main():
    n = int(input())
    s = input()
    good = True
    i = n-1
    while i >= 0:
        if s[i] == s[i-1]:
            good = False 
            i -= 2
    if good:
        print(0)
        print(s)
    else:
        print(n-i-1)
        print(s[:i-1] + s[i+1:])

if __name__ == '__main__':
    main()
