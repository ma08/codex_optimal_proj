

# n = int(input())
n = 100000000000000
# n = 18279 
# n = 4
# n = 26

if n <= 26:
    print(chr(n + 96))
else:
    digits = 1
    c = 0
    while n > c:
        c = 26 * (26 ** (digits - 1)) * digits
        digits += 1

    digits -= 1
    c = 26 * (26 ** (digits - 1)) * digits

    n = n - c

    l = []
    for i in range(digits):
        l.append(1)

    for i in range(n):
        l[digits - 1] += 1
        for j in range(digits - 1, 0, -1):
            if l[j] > 26:
                l[j] = 1
                l[j - 1] += 1

    ans = ''
    for i in range(digits):
        ans += chr(l[i] + 96)

    print(ans)
