
n = int(input())
t = input()

def reverse(string, start, end):
    return string[:start] + string[start:end][::-1] + string[end:]

for i in range(n, 0, -1):
    if n % i == 0:
        t = reverse(t, 0, i)

print(t)
