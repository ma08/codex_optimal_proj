
N = int(input())
A = []
for i in range(N):
    A.append(int(input()))

for a in A:
    if a % 2 == 0 and (a % 3 != 0 and a % 5 != 0):
        print('DENIED')
        exit(0)
print('APPROVED')
