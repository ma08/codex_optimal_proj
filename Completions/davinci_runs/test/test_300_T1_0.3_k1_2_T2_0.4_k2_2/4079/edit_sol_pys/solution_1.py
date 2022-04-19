
import sys
import math

def is_diverse(s, d):
    if len(s) == 0:
        return d
    if len(s) == 1:
        return d and True
    if ord(s[0]) + 1 == ord(s[1]):
        return is_diverse(s[1:], d and True)
    return is_diverse(s[1:], d and False)

def main():
    n = int(sys.stdin.readline())
    for i in range(n):
        s = sys.stdin.readline().strip()
        if is_diverse(s):
            print "Yes"
        else:
            print "No"

if __name__ == '__main__':
    main()
