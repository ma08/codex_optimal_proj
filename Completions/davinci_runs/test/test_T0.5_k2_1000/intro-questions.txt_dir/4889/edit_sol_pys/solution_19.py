
import sys

def main():
    n = int(sys.stdin.readline())
    for i in range(n): 
        x,y = map(int, sys.stdin.readline().split())
        print(x+y)

if __name__ == '__main__':
    main()
