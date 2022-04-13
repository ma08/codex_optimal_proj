'''
Description

Given a string S, you are allowed to convert it to a palindrome by adding characters
in front of it. Find and return the shortest palindrome you can find by performing this transformation.

For example:

Given "aacecaaa", return "aaacecaaa".

Given "abcd", return "dcbabcd".
'''

import sys

def main():
    s = sys.stdin.readline().strip()
    count = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] != s[j]:
                if s[i] not in s[i+1:j] and s[j] not in s[i+1:j]:
                    count += 1
    print(count)

if __name__ == "__main__":
    main()
