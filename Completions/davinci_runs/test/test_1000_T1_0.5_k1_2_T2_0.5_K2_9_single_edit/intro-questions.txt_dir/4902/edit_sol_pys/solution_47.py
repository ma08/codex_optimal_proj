

import sys

def main():
    s = sys.stdin.readline().strip()
    dict = {}
    for c in s:
        if c not in dict:
            dict[c] = 1
        else:
            dict[c] += 1
    count = 0
    odd = 0
    for c in dict:
        if dict[c] % 2 != 0:
            odd += 1
    if odd == 0:
        print(0)
    else:
        print(odd - 1)

if __name__ == '__main__':
    main()
