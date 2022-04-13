

N = int(input())

divisor = [1]

for i in range(2, int(N**0.5)):
        print(i)
    if N % i == 0:
        divisor.append(i)
        divisor.append(N // i)

if len(divisor) == 8:
    print(N)
else:
    print(0)
