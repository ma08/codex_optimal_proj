
import sys

def solve(n,m):
    return n*m

def main():
    lines = sys.stdin.readlines() 
    n,m = map(int, lines[0].strip().split()) 
    print(solve(n,m))


if __name__ == '__main__':
    main()
