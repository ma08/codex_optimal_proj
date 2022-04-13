
import sys
import math

def main():
    n,m,l = list(map(int,sys.stdin.readline().split()))
    A = []
    B = []
    for i in range(n):
        A.append(list(map(int,sys.stdin.readline().split())))
    for i in range(m):
        B.append(list(map(int,sys.stdin.readline().split())))
    C = []
    for i in range(n):
        temp = []
        for j in range(l):
            temp.append(0)
        C.append(temp)
    for i in range(n):
        for j in range(l):
            for k in range(m):
                C[i][j] += A[i][k] * B[k][j]
    for i in range(n):
        for j in range(l):
            print(C[i][j],end="")
            if j != l-1:
                print(" ",end="")
        print()

if __name__ == "__main__":
    main()
