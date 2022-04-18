
# https://open.kattis.com/problems/simonsays
import sys

def main():
    n = int(sys.stdin.readline())
    for i in range(n):
        if sys.stdin.readline()[:10] == 'Simon says':
            print(sys.stdin.readline()[11:])

if __name__ == '__main__':
    main()
