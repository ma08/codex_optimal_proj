

import sys

def main():
    s = input()
    t = input()
    count = 0
    for i in range(len(s) - 1):
        if s[i + 1] != t[i]:
            count += 1
    print(count)

if __name__ == '__main__':
    main()
