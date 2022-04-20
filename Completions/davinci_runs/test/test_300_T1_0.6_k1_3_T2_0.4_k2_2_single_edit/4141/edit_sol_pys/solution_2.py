

N = int(input())
A = []
for i in range(N):
    A.append(int(input()))

for i in A:
    if i % 2 == 0 and (i % 3 != 0 or i % 5 != 0):
        print('DENIED')
        exit(0)
print('APPROVED')
