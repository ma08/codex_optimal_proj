

import sys, string

def main():
    s = input()
    t = input()
    d = dict()
    for c in string.ascii_lowercase:
        d[c] = -1
    for i, c in enumerate(s):
        if d[c] == -1:
            d[c] = t[i]
        elif d[c] != t[i]:
            print('No')
            return
    for c in string.ascii_lowercase:
        if d[c] == -1:
            d[c] = c
    print('Yes')
    for c in s:
        print(d[c], end='')
    print()

if __name__ == '__main__':
    main()
