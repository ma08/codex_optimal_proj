
n = int(input())
s = input()

count = 0
a = 0
b = 0
c = 0

for i in range(n):
    if s[i] == "A":
        a += 1
    if s[i] == "B":
        b += 1
    if s[i] == "C":
        c += 1

    if s[i - 1] == "A" and s[i] == "B" and s[i + 1] == "C":
        count += 1

if a == 0 or b == 0 or c == 0:
    count = 0

print(count)
