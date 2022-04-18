
import sys

def main():
    print('yes' if len(set(sys.stdin.readline().strip().split())) == len(sys.stdin.readline().strip().split()) else 'no')

if __name__ == '__main__':
    main()
