

import sys

def is_palindrome(s):
    return s == s[::-1]

def is_strong_palindrome(s):
    return (is_palindrome(s) and
            is_palindrome(s[0:((len(s)-1)//2)]) and
            is_palindrome(s[((len(s)+3)//2)-1:]))

def main():
    s = sys.stdin.readline().rstrip()
    if is_strong_palindrome(s):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()