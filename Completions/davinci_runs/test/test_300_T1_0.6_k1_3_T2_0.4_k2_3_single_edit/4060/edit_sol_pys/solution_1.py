
n = int(input())
s = input()

counts = [0, 0]
for i in range(n):
    counts[0 if s[i] == '(' else 1] += 1

if counts[0] != counts[1]:
    print(0)
else:
    print(n // 2)
