

import math

def main():
    N,K = map(int, input().split())
    print(math.ceil(N/K)*math.ceil(N/K)*math.ceil(N/K)) # εγδΈγ

if __name__ == '__main__':
    main()
