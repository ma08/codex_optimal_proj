n = int(input())
s = input()
t = input()

if len(set(t)) == 1:
    if t == s:
        print(n)
    else:
        print(0)
    exit()

max_len = 0
for i in range(n):
    for j in range(i, n):
        if t[i] == t[j]:
            if s[i:j+1] == t[i:j+1]:
                max_len = max(max_len, j - i + 1)

print(max_len)
