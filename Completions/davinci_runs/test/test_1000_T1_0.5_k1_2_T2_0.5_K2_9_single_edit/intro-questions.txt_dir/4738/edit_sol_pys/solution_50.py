

import sys

def get_k(s):
    if len(s) == 1:
        return 1
    if len(s) == 2:
        if s[0] == s[1]:
            return 1
        return 2
    for i in range(1, len(s)):
        if s[i] == s[0]:
            if s[i:] == s[0] + s[i+1:][::-1]:
                return i
    return len(s) + 1

def main():
    s = sys.stdin.readline().strip()
    print(get_k(s))

if __name__ == '__main__':
    main()
