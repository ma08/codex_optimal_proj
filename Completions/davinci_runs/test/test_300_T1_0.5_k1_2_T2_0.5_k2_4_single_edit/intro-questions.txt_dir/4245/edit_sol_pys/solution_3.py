
import math

def find_min_strips(A, B):
    return math.ceil(B / A) if A > 0 and B > 0 else 0

def main():
    A, B = [int(x) for x in input().split()]
    print(find_min_strips(A, B))

if __name__ == '__main__':
    main()
