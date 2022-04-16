# -*- coding: utf-8 -*-

def main():
    x, y = map(int, input().split())
    if x <= 4 and y <= 4:
        print('Yes')
    if x <= 8 and y <= 8:
        print('Yes')
    if x <= 12 and y <= 12:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
