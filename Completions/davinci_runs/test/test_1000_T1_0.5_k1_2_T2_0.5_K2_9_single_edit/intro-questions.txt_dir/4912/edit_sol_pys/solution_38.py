
import sys

def main():
    h, w, n = [int(x) for x in sys.stdin.readline().strip().split()]
    bricks = [int(x) for x in sys.stdin.readline().strip().split()]
    print 'YES' if sum(bricks) >= h * w else 'NO'

if __name__ == '__main__':
    main()
