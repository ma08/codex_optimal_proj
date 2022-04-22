

import math
import itertools

def main():
    N, D = map(int, input().split())
    if N <= D:
        print(1)
    else:
        print(math.ceil((N - D) / (D * 2 + 1)) + 1)

if __name__ == "__main__":
    main()
