# -*- coding: utf-8 -*-

def main():
    a,b,c = map(int, input().split())
    if a < b:
        if b < c:
            print("Yes")
        else:
            print("No")
    else:
        print("No")

if __name__ == '__main__':
    main()
