

#------------------------------------------------------------------------------#

import sys

def main():
    sys.stdin = open('inputs/input.txt', 'r')
    n = int(input())
    prefixes = []
    for _ in range(n-1):
        prefixes.append(input())

    suffixes = []
    for _ in range(n-1):
        suffixes.append(input())

    #print(prefixes, suffixes)

    s = []
    for i in range(1, n):
        p = prefixes[i-1]
        s.append(p[-1])
        prefixes[i] = prefixes[i][:-1]

    s.append(suffixes[-1][0])
    suffixes[-1] = suffixes[-1][1:]

    for i in range(n-2, 0, -1):
        p = suffixes[i]
        s.append(p[0])
        suffixes[i-1] = suffixes[i-1][1:]

    print(''.join(s))


if __name__ == '__main__':
    main()
