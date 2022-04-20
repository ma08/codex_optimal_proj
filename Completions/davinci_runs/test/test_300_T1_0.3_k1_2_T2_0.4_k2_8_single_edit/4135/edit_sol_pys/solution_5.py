
n = int(input())
t = input()

for i in range(n, 0, -1):
    if n % i == 0:
        t = t[:0] + t[0:i][::-1] + t[i:]

print(t)
