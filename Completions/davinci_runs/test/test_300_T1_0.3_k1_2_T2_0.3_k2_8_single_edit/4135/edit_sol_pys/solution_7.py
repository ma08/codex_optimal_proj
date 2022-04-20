
n = int(input())
t = input()

def reverse(t, start, end):
    return t[:start] + t[start:end][::-1] + t[end:]

for i in range(n, 0, -1):
    if n % i == 0:
        t = reverse(t, 0, i)

print(t)
