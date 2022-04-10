

n = int(input())
divisors = list(map(int, input().split()))
x = []
y = []
for i in range(n):
    if divisors[i] in x:
        y.append(divisors[i])
    else:
        x.append(divisors[i])
print(x, y)