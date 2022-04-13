
import sys

def main():
    h, w, n = [int(x) for x in sys.stdin.readline().strip().split()]
    bricks = [int(x) for x in sys.stdin.readline().strip().split()]
    if sum(bricks) >= h * w:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()
