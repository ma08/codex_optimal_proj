

import sys

def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    max_a = max(A)
    min_a = min(A)
    max_diff = max(max_a-min_a, A[-1]-A[0])
    print(max_diff)

if __name__ == '__main__':
    main()