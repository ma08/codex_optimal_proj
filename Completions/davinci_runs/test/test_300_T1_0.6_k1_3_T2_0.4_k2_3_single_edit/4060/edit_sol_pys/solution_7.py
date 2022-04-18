n = int(input())
s = input()[::-1]


counts = [0, 0, 0]
for i in range(n):
    counts[0 if s[i] == '(' else 1 if s[i] == ')' else 2] += 1

counts = [0, 0]
for i in range(n):
    counts[0 if s[i] == '(' else 1] += 1

if counts[0] != counts[1]:
    print(0)
else:
    print(n // 2)
