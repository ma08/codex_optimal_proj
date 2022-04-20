

# TODO: write your solution here
h1, m1 = input().split(':')
h2, m2 = input().split(':')

m = int(m1) + int(m2)
h = int(h1) + int(h2)

if m >= 60:
    m = m - 60
    h = h + 1

if h >= 24:
    h = h - 24

if m % 2 == 0:
    m = m / 2
else:
    m = (m + 1) / 2

print("{0:02d}:{1:02d}".format(h, m))