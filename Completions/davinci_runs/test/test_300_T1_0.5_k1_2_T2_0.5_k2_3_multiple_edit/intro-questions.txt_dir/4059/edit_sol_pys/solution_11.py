
N = int(input()) # input the number of test cases

count = 0
for a in range(1, N+1):
    for b in range(1, N+1):
        c = N - a*b # c is the number of the third side
        if c > 0:
            count += 1

print(count)
