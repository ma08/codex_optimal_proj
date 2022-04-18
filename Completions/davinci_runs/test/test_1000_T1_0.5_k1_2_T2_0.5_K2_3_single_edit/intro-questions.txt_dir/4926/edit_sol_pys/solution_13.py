

N = int(input())

e = 1
for n in range(1, N+1):
    e += 1 / factorial(n)

print(e)
