

n = int(input())

def f(n):
    if n % 10 == 0:
        return f(n // 10)
    else:
        return n

s = set()
while n not in s:
    s.add(n)
    n = f(n + 1)
print(len(s))