

#-----main-----
N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

#-----function-----
def main(N,A,B):
    total = 0
    for i in range(N):
        total += min(A[i],B[i])
        total += min(A[i+1],B[i]-min(A[i],B[i]))
    return total

print(main(N,A,B))