

import sys

def main():
    N, M = [int(x) for x in sys.stdin.readline().split()]
    A = [int(x) for x in sys.stdin.readline().split()]
    A.sort()
    #print(A)
    count = 0
    for i in range(N):
        if A[i] > M:
            break
        for j in range(i, N):
            if A[j] > M:
                break
            if A[(i+j)//2] == M:
                count += j-i+1
            elif A[(i+j)//2] > M:
                break
    #print(count)
    print(count)

if __name__ == "__main__":
    main()