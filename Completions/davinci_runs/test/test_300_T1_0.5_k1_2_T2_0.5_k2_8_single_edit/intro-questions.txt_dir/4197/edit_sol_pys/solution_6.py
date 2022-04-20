

N, M = map(int, input().split())
A = [i for i in range(1, N+1)]
cnt = 1
print('<', end='')
while A:
    if cnt % M == 0:
        print(A.pop(0), end='')
        if A:
            print(', ', end='')
    else:
        A.append(A.pop(0))
    cnt += 1

print('>')
