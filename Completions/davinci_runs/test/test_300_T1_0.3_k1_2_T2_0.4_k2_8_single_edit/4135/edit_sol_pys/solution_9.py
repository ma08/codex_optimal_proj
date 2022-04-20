
n = int(input())
s = input()

def reverse(s, start, end):
    return s[:start] + s[start:end][::-1] + s[end:]

for i in range(n, 1, -1):
    if n % i == 0:
        s = reverse(s, 0, i)

print(s)
