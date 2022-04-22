

import sys

def main():
    s = sys.stdin.readline().rstrip()
    t = sys.stdin.readline().rstrip()
    count = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            count += 1
    print(count, end="")

if __name__ == '__main__':
    main()
