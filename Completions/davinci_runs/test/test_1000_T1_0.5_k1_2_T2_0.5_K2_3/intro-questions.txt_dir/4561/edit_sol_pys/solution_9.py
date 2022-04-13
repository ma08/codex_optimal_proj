

# input N
N = int(input())

# input A
A = list(map(int,input().split()))

# input B
B = list(map(int,input().split()))

# input C
C = list(map(int,input().split()))

# count
count = 0

# loop
for i in range(N):
    # add A[i]
    count += A[i]
    # judge B[i]
    if B[i] == A[i]+1:
        count += C[A[i]-1]

# output
print(count)
