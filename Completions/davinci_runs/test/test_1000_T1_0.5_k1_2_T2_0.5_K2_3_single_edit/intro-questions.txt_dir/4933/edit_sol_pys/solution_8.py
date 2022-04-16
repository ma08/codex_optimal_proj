
import sys

def main():
    x, y, z = map(int, sys.stdin.readline().split())
    
    if x == y:
        print(z)
    elif y == z:
        print(x)
    else:
        print(y)

if __name__ == '__main__':
    main()
