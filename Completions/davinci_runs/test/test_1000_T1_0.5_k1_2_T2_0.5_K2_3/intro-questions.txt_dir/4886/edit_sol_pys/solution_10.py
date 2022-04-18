
import sys

def main():
    n, k = map(int, sys.stdin.readline().split())
    print("Your wish is granted!" if k >= n else "You will become a flying monkey!")

if __name__ == '__main__':
    main()
