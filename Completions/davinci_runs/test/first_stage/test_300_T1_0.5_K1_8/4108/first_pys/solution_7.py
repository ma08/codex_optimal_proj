

import sys
sys.setrecursionlimit(1000000)

def main():
    s = input()
    t = input()
    if len(s) != len(t):
        print('No')
        exit()
    if s == t:
        print('Yes')
        exit()
    for i in range(len(s)):
        if s[i] != t[i]:
            break
    else:
        print('No')
        exit()
    for i in range(len(s)):
        if s[i] == t[i]:
            continue
        if s[i] != t[0]:
            print('No')
            exit()
        s = s.replace(s[i], t[0], 1)
        if s == t:
            print('Yes')
            exit()
        if s.count(t[0]) > 1:
            print('No')
            exit()
        s = s.replace(t[0], t[1], 1)
        if s == t:
            print('Yes')
            exit()
    print('No')

if __name__ == '__main__':
    main()