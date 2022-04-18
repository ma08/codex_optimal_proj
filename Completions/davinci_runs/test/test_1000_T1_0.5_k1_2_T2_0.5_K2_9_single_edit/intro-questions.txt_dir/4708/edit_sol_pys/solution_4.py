

n = int(input("n: "))
k = int(input("k: "))
x = int(input("x: "))
y = int(input("y: "))

if (n <= k):
    print(n * x)
else:
    print(k * x + (n - k) * y)
