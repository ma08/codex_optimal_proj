
import random

def main():
    N = int(input())
    A = list(map(int, input().split()))
    while len(A) > 1:
        idx1 = random.randint(0, len(A)-1)
        idx2 = random.randint(0, len(A)-1)
        while idx1 == idx2:
            idx2 = random.randint(0, len(A)-1)
        A[idx1] -= A[idx2]
        if A[idx1] <= 0:
            A.pop(idx1)
    print(A[0])

if __name__ == '__main__':
    main()