
n = int(input())
divisor = list(map(int, input().split()))
a = divisor[0]
b = divisor[0]
for i in range(n):
    if divisor[i] == 1:
        pass
    elif divisor[i] == divisor[i + 1]:
        a *= divisor[i]
    elif divisor[i] != divisor[i + 1]:
        b *= divisor[i]
print(a, b)
