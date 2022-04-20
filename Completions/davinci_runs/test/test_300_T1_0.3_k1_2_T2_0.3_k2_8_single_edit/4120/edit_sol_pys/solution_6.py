
import sys

def main():
    n, m, k = [int(x) for x in input().split()]
    roads = [[int(x) for x in input().split()] for _ in range(m)]
    print(roads[0])

if __name__ == "__main__":
    main()
