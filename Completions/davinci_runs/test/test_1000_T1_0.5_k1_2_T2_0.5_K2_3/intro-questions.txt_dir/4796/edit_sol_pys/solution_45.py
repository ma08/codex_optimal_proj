import numpy as np

def solve(N,M,X,Y):
    X -= 1
    Y -= 1
    for i in range(N):
        for j in range(M):
            print(i*M+j, end = ' ')
        print()



def main():
    N,M,X,Y = map(int,input().split())
    solve(N,M,X,Y)

main()
