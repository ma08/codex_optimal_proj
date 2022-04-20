

n = int(input())
t = input()

if n == 1:
    print(t)
else:
    s = t[:]
    for d in range(n, 1, -1):
        if n % d == 0:
            s = s[:d-1] + s[d-1:n][::-1] + s[n:]
    print(s)