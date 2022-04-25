# coding: utf-8

def main():
    x, y = map(int, input().split())
    if x == 1:
        print(300000 + y*1000)
    elif x == 2:
        print(200000 + y*1000)
    elif x == 3:
        print(100000 + y*1000)
    else:
        print(y*1000)

if __name__ == '__main__':
    main()
