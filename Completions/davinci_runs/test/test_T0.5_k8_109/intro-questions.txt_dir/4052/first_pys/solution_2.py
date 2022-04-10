

n = int(input())
s = input()
t = input()

if s == t:
    print(0)
    exit()

# check if it is possible to transform s to t
for i in range(n):
    if s[i] != t[i]:
        break

if i == n - 1:
    print(-1)
    exit()

# find the first occurrence of a letter in t that is not in s
for j in range(i + 1, n):
    if t[j] not in s[i:j]:
        break

# find the first occurrence of the letter in s
for k in range(i, j):
    if s[k] == t[j]:
        break

# swap the letters
s = s[:k] + t[j] + s[k + 1:j] + s[k] + s[j + 1:]

# print the number of moves and the indices of the letters to be swapped
print(1)
print(k, j)