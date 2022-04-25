
import math
import itertools

def main():
    N, D = map(int, input().split())
    if N <= 2 * D + 1:
        print(1)
    else:
        print(math.ceil((N - D) / (2 * D + 1)) + 1)

if __name__ == "__main__":
    main()
