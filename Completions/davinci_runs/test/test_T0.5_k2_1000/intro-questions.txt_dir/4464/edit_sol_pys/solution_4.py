
import sys

def main():
    a, b, c = map(int, sys.stdin.readline().split())
    if c % b == 0:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
