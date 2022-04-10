

n = int(input())
a = list(map(int, input().split()))

GCD = 0

for i in range(n - 1):
    for j in range(i + 1, n):
        gcd = a[i]
        for k in range(i + 1, j + 1):
            gcd = gcd * a[k] // gCD(gcd, a[k])
            if gcd == 1:
                break
        if gcd == 1:
            print(i + 1, j + 1)
            exit()
        elif GCD == 0:
            GCD = gcd
        elif gcd < GCD:
            GCD = gcd
            first = i + 1
            second = j + 1

print(first, second)