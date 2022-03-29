

n = int(input())
s = input()
t = input()

count = 0

for i in range(n):
    if s[:i] + s[i+1:] == t:
        count += 1

print(count)