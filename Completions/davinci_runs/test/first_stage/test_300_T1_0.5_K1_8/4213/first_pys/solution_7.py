

N = int(input())
A = [int(i) for i in input().split()]

max_difference = 0
for i in range(N-1):
    for j in range(i+1, N):
        diff = abs(A[i]-A[j])
        if diff > max_difference:
            max_difference = diff

print(max_difference)