
# solution

N = int(input())

if N == 1:
    print(1)
    exit()

A = list(map(int, input().split()))

if A[0] < A[1]:
    flag = 'up'
    else:
    flag = 'down'

cnt = 1
for i in range(1, N-1):
    if A[i] < A[i+1] and flag == 'down':
        cnt += 1
        flag = 'up'
    elif A[i] > A[i+1] and flag == 'up':
        cnt += 1
        flag = 'down'

print(cnt+1)
