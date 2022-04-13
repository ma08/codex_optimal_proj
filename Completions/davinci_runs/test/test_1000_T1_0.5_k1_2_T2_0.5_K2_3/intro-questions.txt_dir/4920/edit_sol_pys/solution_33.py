'''
Description

Given a string S, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.

For example:

Given "aacecaaa", return "aaacecaaa".

Given "abcd", return "dcbabcd".
'''

import sys

def main():
    s = sys.stdin.readline().strip()
    s = s[::-1]
    print(s)

if __name__ == "__main__":
    main()
