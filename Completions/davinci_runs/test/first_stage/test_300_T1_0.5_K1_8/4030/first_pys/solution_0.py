

# SOLUTION
n = int(input())
s = input()

colors = [1] * n

for i in range(1, n):
    if s[i] == s[i-1]:
        colors[i] = colors[i-1]
    else:
        colors[i] = colors[i-1] + 1

print(colors[-1])
print(*colors)