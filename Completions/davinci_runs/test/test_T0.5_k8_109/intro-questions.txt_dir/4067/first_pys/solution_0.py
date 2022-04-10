

#-----Solution-----

n = int(input())
s = input()

a = s.count("0")
b = s.count("1")
c = s.count("2")

if a > b:
    s = s.replace("0", "3", a-b)
elif a < b:
    s = s.replace("1", "0", b-a)

while c > a:
    s = s.replace("2", "1", 1)
    s = s.replace("1", "0", 1)
    c -= 1

while c > b:
    s = s.replace("2", "0", 1)
    s = s.replace("0", "1", 1)
    c -= 1

if c < a:
    s = s.replace("3", "0", a-c)
elif c < b:
    s = s.replace("3", "1", b-c)

s = s.replace("3", "2")

print(s)