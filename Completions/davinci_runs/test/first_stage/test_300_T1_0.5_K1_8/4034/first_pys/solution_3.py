

import sys

if __name__ == "__main__":
    n = int(input())
    s = input()
    if n > 200 or n < 1:
        sys.exit("n out of range")
    if len(s) != n:
        sys.exit("s does not have n characters")
    for c in s:
        if c < 'a' or c > 'z':
            sys.exit("s has non-lowercase characters")
    s = list(s)
    for i in range(1, len(s)):
        if s[i] < s[i - 1]:
            s[i] = '1'
        else:
            s[i] = '0'
    print("YES")
    print("".join(s))