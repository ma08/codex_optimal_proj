

import sys

def main():
    n = int(input())
    t = input()

    def reverse(s, start, end):
        return s[:start] + s[start:end][::-1] + s[end:]

    for i in range(n, 0, -1):
        if n % i == 0:
            t = reverse(t, 0, i)

    print(t)

if __name__ == '__main__':
    sys.exit(main())
