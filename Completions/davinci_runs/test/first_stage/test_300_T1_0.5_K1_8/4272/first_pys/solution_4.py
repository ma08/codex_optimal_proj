

n = int(input())
s = input()

count = 0

for i in range(n):
    if s[i] == "A":
        for j in range(i + 1, n):
            if s[j] == "B":
                for k in range(j + 1, n):
                    if s[k] == "C":
                        count += 1

print(count)