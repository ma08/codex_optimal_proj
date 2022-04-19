
n = int(input())
t = input()

def reverse(str, start, end):
    return str[:start] + str[start:end][::-1] + str[end:]

for i in range(n, 0, -1):
    if n % i == 0:
        t = reverse(t, 0, i)

print(t)
