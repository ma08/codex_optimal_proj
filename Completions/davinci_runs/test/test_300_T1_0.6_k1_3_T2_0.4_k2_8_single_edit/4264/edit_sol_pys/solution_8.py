

n = int(input())

if n < 10:
    print(n)
elif n < 100:
    print(n - 9)
elif n < 1000:
    print(n - 189)
elif n < 10000:
    print(n - 2889)
elif n < 100000:
    print(n - 38889)
else:
    print(n - 488889)
