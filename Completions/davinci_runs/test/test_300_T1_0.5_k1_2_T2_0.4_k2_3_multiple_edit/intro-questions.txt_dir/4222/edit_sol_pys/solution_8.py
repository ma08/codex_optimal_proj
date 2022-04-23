
import sys

def main():
    n, k = map(int, sys.stdin.readline().split())
    victims = set(range(1, n+1))
    for _ in range(k):
        d = int(sys.stdin.readline())
        victims -= set(map(int, sys.stdin.readline().split()))
    print(len(victims))

if __name__ == '__main__':
    main()
