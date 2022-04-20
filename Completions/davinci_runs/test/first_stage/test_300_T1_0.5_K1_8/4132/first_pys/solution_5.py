

import random

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    while len(A) > 1:
        i = random.randint(0, len(A)-1)
        j = random.randint(0, len(A)-1)
        if i != j:
            if A[i] >= A[j]:
                A[i] -= A[j]
                A.pop(j)
            else:
                A[j] -= A[i]
                A.pop(i)
            A.sort()
    print(A[0])

if __name__ == '__main__':
    main()