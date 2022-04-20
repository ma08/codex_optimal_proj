

N, M = map(int, input().split())

numbers = [0] * N

for _ in range(M):
    s, c = map(int, input().split())
    numbers[s-1] = c

if numbers[0] == 0 and N > 1:
    print(-1)
else:
    print(''.join([str(num) for num in numbers]))