
N = int(input())
divisors = [1]

for i in range(2, int(N**0.5)):
    if N % i == 0:
        divisors.append(i)
        divisors.append(N // i)
if len(divisors) == 9:
    print(N)
else:
    print(0)
