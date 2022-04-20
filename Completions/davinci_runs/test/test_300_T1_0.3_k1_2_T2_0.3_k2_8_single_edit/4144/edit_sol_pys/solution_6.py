
import sys

def main():
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    print(a*b*2 + b*c*2 + c*a*2)

if __name__ == "__main__":
    main()
