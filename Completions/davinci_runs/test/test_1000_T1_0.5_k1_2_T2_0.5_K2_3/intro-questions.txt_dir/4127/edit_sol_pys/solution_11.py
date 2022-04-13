
import sys

def main():
    a, b = map(float, sys.stdin.readline().split())
    print(int(a * b)) # print does not need ()

if __name__ == '__main__': # needs two underscores
    main()
