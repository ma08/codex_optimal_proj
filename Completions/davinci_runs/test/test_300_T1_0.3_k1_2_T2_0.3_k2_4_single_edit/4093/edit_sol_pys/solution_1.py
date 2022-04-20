
import sys

def main():
    for _ in range(int(sys.stdin.readline())):
        n, m = map(int, sys.stdin.readline().split())
        print(m-1 if m else n-1)

if __name__ == "__main__":
    main()
