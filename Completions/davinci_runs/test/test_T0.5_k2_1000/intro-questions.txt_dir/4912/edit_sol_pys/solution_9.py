
#
import sys

def main():
    h, w, n = [int(x) for x in sys.stdin.readline().strip().split()] # read the first line
    bricks = [int(x) for x in sys.stdin.readline().strip().split()] # read the second line
    if sum(bricks) >= h * w: # check if the number of bricks is enough
        print 'YES'
    else:
        print 'NO'

if __name__ == '__main__':
    main()
