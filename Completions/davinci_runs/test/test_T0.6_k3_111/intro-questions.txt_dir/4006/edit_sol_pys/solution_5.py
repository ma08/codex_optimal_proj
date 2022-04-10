n = int(input())

s = set()
while True:
    s.add(n)
    n = f(n + 1)
print(len(s))
