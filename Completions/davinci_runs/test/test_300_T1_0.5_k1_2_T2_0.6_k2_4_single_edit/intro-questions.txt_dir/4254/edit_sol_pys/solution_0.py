import sys
from itertools import permutations

def main():
    x, y, z = map(int, sys.stdin.readline().split())

    print(list(permutations([x,y,z])))

if __name__ == '__main__':
    main()
