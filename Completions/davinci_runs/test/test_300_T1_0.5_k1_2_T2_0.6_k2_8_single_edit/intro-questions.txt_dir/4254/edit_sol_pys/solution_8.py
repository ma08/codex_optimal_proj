

import sys

def main():
    sheep, wolves = map(int, sys.stdin.readline().split())

    if sheep < wolves:
        print('unsafe')
    else:
        print('safe')

if __name__ == '__main__':
    main()
