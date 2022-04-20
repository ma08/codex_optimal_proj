

#!/usr/bin/python
#-----SOLUTION-----

N = int(input())
A = list(map(int, input().split()))

#N = 5
#A = [1, 2, 4, 3, 2]

def solve(N, A):
    L = [None] * N
    R = [None] * N
    L[0] = 1
    R[N-1] = 1
    for i in range(1, N):
        if A[i] > A[i-1]:
            L[i] = L[i-1] + 1
        else:
            L[i] = 1
    for i in range(N-2, -1, -1):
        if A[i] < A[i+1]:
            R[i] = R[i+1] + 1
        else:
            R[i] = 1
    
    
    #print(L, R)
    
    best_len = 0
    best_index = None
    for i in range(N):
        if (L[i] + R[i] - 1) > best_len:
            best_len = L[i] + R[i] - 1
            best_index = i
            
    #print(best_len, best_index)
    
    moves = []
    for i in range(best_index - L[best_index] + 1, best_index + 1):
        moves.append('L')
    for i in range(best_index + 1, best_index + R[best_index]):
        moves.append('R')
        
    print(best_len)
    print(''.join(moves))
    
solve(N, A)
