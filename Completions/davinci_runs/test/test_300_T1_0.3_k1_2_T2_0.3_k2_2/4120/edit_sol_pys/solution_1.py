
from sys import stdin

def main():
    n, m, k = [int(x) for x in stdin.readline().split()]
    roads = [[int(x) for x in stdin.readline().split()] for _ in range(m)]
    print(n, m, k)
    print(roads)

if __name__ == "__main__":
    main()
