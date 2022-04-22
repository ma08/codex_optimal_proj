
from sys import stdin

def solve(n, k, x, a):
    return -1 

def main():
    n, k, x = map(int, stdin.readline().split())
    a = list(map(int, stdin.readline().split()))
    print(solve(n, k, x, a))

if __name__ == "__main__":
    main()
