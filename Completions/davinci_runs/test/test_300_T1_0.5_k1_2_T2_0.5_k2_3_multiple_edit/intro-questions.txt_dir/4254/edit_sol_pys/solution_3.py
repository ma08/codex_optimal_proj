

import sys

def main():
    sheep, wolfs = map(int, sys.stdin.readline().split())
    if sheep < wolfs:
        print("unsafe")
    else:
        print("safe")
 
if __name__ == '__main__':
    main()
