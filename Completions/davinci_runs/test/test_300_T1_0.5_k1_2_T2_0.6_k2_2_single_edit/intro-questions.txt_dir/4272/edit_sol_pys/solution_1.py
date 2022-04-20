

n = int(input())
s = input()

count = 0

for i in range(n - 1):
    if s[i] == "A" and s[i + 1] == "B":
        count += 1

print(count)
