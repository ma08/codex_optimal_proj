
m = 0
n = int(input())

if n % 3 == 0:
    m = n // 3
    print("triple", m)
elif n % 2 == 0:
    m = n // 2
    print("double", m)
else:
    print("single", n)
