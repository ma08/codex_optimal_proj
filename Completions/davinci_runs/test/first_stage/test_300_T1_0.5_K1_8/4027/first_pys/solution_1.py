

n = int(input())
a = n * (n + 1) // 2
b = n * (n + 1) // 2
if n % 2 == 0:
    b -= n // 2
else:
    a -= (n + 1) // 2
print(abs(a - b))