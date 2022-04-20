

h1, m1 = map(int, input().split(":"))
h2, m2 = map(int, input().split(":"))

if m1 % 2 == 0:
    m1 += 1
else:
    m1 -= 1

if m1 < 0:
    h1 -= 1
    m1 = 59
elif m1 > 59:
    h1 += 1
    m1 = 0

if m1 % 2 == 0:
    m1 += 1
else:
    m1 -= 1

if m1 < 0:
    h1 -= 1
    m1 = 59
elif m1 > 59:
    h1 += 1
    m1 = 0

if m2 % 2 == 0:
    m2 += 1
else:
    m2 -= 1

if m2 < 0:
    h2 -= 1
    m2 = 59
elif m2 > 59:
    h2 += 1
    m2 = 0

if m2 % 2 == 0:
    m2 += 1
else:
    m2 -= 1

if m2 < 0:
    h2 -= 1
    m2 = 59
elif m2 > 59:
    h2 += 1
    m2 = 0

print(h1, m1)
print(h2, m2)

if h1 == h2 and m1 == m2:
    print("{:02d}:{:02d}".format(h1, m1))
else:
    print("{:02d}:{:02d}".format(h1, m1))
    print("{:02d}:{:02d}".format(h2, m2))