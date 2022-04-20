
import sys

def main():
    n, m = [int(x) for x in sys.stdin.readline().split()]
    roads = [[int(x) for x in sys.stdin.readline().split()] for _ in range(n)]
    print(n, m)
    for i in range(n):
        print(roads[i])

if __name__ == "__main__":
    main()
