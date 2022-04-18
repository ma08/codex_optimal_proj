N = int(input())

a = N // 1000
b = (N // 100) % 10
c = (N // 10) % 10
d = N % 10

print("Yes" if a == d and b == c else "No")
