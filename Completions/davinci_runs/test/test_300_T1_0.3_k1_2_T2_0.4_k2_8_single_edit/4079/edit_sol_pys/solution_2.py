
import sys

def is_diverse(s):
    if len(s) == 1:
        return True
    if len(set(s)) != len(s):
        return False
    if ord(s[0]) + len(s) - 1 != ord(s[-1]):
        return False
    for i in range(1, len(s)):
        if ord(s[i]) - ord(s[i-1]) != 1:
            return False
    return True

def main():
    n = int(sys.stdin.readline().strip())
    for i in range(n):
        s = sys.stdin.readline().strip()
        print('Yes' if is_diverse(s) else 'No')

if __name__ == '__main__':
    main()
