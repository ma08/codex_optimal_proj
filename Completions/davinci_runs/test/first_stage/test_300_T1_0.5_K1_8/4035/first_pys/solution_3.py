

import sys

def main():
    a, b = map(int, input().split())
    for i in range(1, 101):
        if int(i * 0.08) == a and int(i * 0.1) == b:
            print(i)
            sys.exit()
    print(-1)

if __name__ == '__main__':
    main()