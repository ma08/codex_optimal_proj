

import sys

def main():
    n = int(input())
    s = input()
    a = 0
    for i in range(n - 2):
        if s[i] == 'A' and s[i + 1] == 'B' and s[i + 2] == 'C':
            a += 1
    print(a)

if __name__ == '__main__':
    main()
