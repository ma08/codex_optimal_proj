
import sys

def main():
    sheep, wolves = map(int, sys.stdin.readline().split())
    if sheep >= wolves:
        print('safe')
        return
    print('unsafe')

if __name__ == '__main__':
    main()
