

#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    a, b, c = input().split()
    if a == b and b != c:
        print('Yes')
    elif a == c and c != b:
        print('Yes')
    elif b == c and c != a:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()