

n = int(input())
s = input()

count = 0
for i in range(n - 2):
    if s[i] == s[i + 1] == s[i + 2] == "x":
        count += 1

print(count)
