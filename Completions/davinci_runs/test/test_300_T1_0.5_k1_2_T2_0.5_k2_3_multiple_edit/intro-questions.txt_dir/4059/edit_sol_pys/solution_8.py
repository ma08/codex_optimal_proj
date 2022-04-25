

N = int(input()) # input the number of sides

count = 0
for a in range(1, N+1):
    for b in range(1, N+1):
        c = N - a*b # c is the number of the third side, c > 0
        if c > 0:
            count += 1

print(count)
