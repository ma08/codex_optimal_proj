

n = int(input())
s = input()

total = 1

for i in range(n - 1):
    if s[i] != s[i + 1]:
        total += 1

print(total)
