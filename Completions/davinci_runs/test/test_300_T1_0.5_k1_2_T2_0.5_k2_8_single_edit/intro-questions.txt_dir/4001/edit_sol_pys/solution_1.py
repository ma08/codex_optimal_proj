
N = int(input()) - 1
divisors.append(1)
divisors = list(map(int, input().split()))
x = 1
y = 1
for i in range(len(divisors) - 1):
    if divisors[i] == 1:
        continue
    if divisors[i] == divisors[i + 1]:
        x *= divisors[i]
        i += 1
    else:
        y *= divisors[i]
print(x, y)
