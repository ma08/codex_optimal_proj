

n = int(input())

for i in range(n):
    s = input()
    a = b = c = 0
    for j in range(len(s)):
        if s[j] == 'a':
            a += 1
        elif s[j] == 'b':
            b += 1
        elif s[j] == 'c':
            c += 1

    print(a, b, c)
