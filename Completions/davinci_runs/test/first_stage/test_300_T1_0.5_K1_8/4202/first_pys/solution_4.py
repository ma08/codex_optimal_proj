

import sys

def main():
    l, r = map(int, sys.stdin.readline().split())
    l_mod = l % 2019
    r_mod = r % 2019
    if l_mod <= r_mod:
        print(min(l_mod * (l_mod + 1) % 2019, l_mod * (l_mod + 2) % 2019))
    else:
        print(0)

if __name__ == '__main__':
    main()