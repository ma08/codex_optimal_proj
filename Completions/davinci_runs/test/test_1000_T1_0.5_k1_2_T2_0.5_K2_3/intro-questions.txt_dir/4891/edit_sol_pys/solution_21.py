# pieces = list(map(int, input().split()))

# for i in range(6):
#     if i == 0:
#         print(1 - pieces[i], end=' ')
#     elif i == 1:
#         print(1 - pieces[i], end=' ')
#     elif i == 2:
#         print(2 - pieces[i], end=' ')
#     elif i == 3:
#         print(2 - pieces[i], end=' ')
#     elif i == 4:
#         print(2 - pieces[i], end=' ')
#     else:
#         print(8 - pieces[i], end=' ')

from collections import deque

N = int(input())
A = deque(list(map(int, input().split())))

count = 0

while len(A) != 1:
    if A[0] == A[1]:
        A.popleft()
        A.popleft()
        count += 1
    else:
        A.rotate(-1)

if count % 2 == 0:
    print('No')
else:
    print('Yes')
