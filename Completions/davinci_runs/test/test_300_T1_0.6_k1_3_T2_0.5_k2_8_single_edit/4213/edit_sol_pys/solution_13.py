N = int(input())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]

sum_a = sum(A)
sum_b = sum(B)

if sum_b > sum_a:
    print(-1)
    exit()

count = 0
for i in range(N):
    a = A[i]
    b = B[i]
    if a >= b:
        continue
    else:
        count += b - a

print(count)
