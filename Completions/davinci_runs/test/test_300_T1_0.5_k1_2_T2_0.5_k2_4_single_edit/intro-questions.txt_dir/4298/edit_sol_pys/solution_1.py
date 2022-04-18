
import math, itertools

def main():
    N, X = map(int, input().split())
    print(min(X - 1, N - X))

if __name__ == "__main__":
    main()
