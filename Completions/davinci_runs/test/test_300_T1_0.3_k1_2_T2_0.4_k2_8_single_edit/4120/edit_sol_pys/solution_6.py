import sys



class Graph:
    def __init__(self, n, m, k, roads):
        self.n = n
        self.m = m
        self.k = k
        self.roads = roads


def main():
    n, m, k = [int(x) for x in sys.stdin.readline().split()]
    roads = [[int(x) for x in sys.stdin.readline().split()] for _ in range(m)]
    print(n, m, k)
    print(roads)


if __name__ == "__main__":
    main()
